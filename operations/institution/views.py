"""Bounded entry packets, reconciliation findings and portable snapshots."""

import json
import os
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

from . import govern, resources, work
from .store import DOMAINS, RuleError, domain_name, require

ROOT = Path(__file__).resolve().parents[2]
ENTRY = ["README.md", "CHARTER.md", "governance/protocols/README.md"]
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(<([^>]+)>\)|(?<!!)\[[^\]\n]+\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")


def task_packet(store, key):
    task = store.get("tasks", key)
    role = store.get("roles", task["role"])
    links = [{"id": ref["id"], "kind": ref["kind"], "state": ref["state"],
              "title": ref["title"], "version": ref["version"]}
             for ref in resources.validate_refs(store, task["refs"])]
    thread = store.get("threads", task["thread"]) if task["thread"] else None
    history = [{field: event[field] for field in ("seq", "actor", "action", "time")}
               for event in store.history(f"tasks/{key}", 5)]
    return dict(entry=ENTRY, domain_index=f"{role['domain']}/README.md", role=role,
                state=work.public(task), lease_current=work.live_lease(store, task),
                input_issues=resources.unavailable_refs(store, task["refs"]),
                resources=links, thread=brief(thread, "owner", "due") if thread else None,
                recent_events=history, history_target=f"tasks/{key}")


def brief(record, *fields):
    return {key: record[key] for key in ("id", "version", "state", "title", *fields) if key in record}


def inbox(store, actor, domain, limit):
    domain_name(domain)
    store.get("actors", actor)
    require(1 <= limit <= 50, "inbox limit must be between 1 and 50")
    now = store.clock()
    grants = [grant for grant in store.list("grants") if store.grant_valid(grant)]
    holder_roles = {grant["role"] for grant in grants if grant["actor"] == actor}
    if domain == "executive":
        threads = [row for row in store.list("threads") if row["state"] != "closed"
                   and (row["state"] == "unrouted" or row["due"] <= now or row["escalations"]
                        or not any(grant["role"] == row["owner"] and "respond" in grant["capabilities"]
                                   for grant in grants))]
    else:
        threads = [row for row in store.list("threads", domain=domain) if row["state"] != "closed"]
        threads.sort(key=lambda row: row["owner"] not in holder_roles)
    threads.sort(key=lambda row: (row["due"], row["id"]))
    tasks = [task for task in store.list("tasks", domain=domain) if task["state"] != "done"]
    tasks.sort(key=lambda row: (-row["priority"], row["updated"], row["id"]))
    proposals = [row for row in store.list("proposals", domain=domain)
                 if row["state"] in {"submitted", "approved"}]
    return dict(entry=ENTRY, domain_index=f"{domain}/README.md", actor_roles=sorted(holder_roles - {None}),
                threads=[brief(row, "domain", "owner", "due", "escalations") for row in threads[:limit]],
                tasks=[brief(task, "role", "holder", "priority") for task in tasks[:limit]],
                proposals=[brief(row, "collection", "target", "proposer") for row in proposals[:limit]],
                counts=dict(threads=len(threads), tasks=len(tasks), proposals=len(proposals)))


def audit(store, root=ROOT):
    now = store.clock()
    findings = []
    def report(code, collection, record, detail):
        findings.append(dict(code=code, record=f"{collection}/{record['id']}", detail=detail))

    valid_grants = [grant for grant in store.list("grants") if store.grant_valid(grant)]
    work_roles = {g["role"] for g in valid_grants if "work" in g["capabilities"]}
    respond_roles = {g["role"] for g in valid_grants if "respond" in g["capabilities"]}
    for grant in store.list("grants", state="active"):
        if not store.grant_valid(grant):
            report("stale-grant", "grants", grant, "review role and parent revisions")
    for role in store.list("roles", state="active"):
        if role["id"] not in work_roles and "work" in role["capabilities"]:
            report("unfilled-role", "roles", role, "no currently delegated worker")
        for guide in role["guides"]:
            if not (root / guide).is_file():
                report("missing-role-guide", "roles", role, guide)
    for task in store.list("tasks"):
        if task["state"] == "done":
            continue
        if task["role"] not in work_roles:
            report("unowned-task", "tasks", task, "dispatch has no authorized current holder")
        elif task["state"] == "running" and not work.live_lease(store, task):
            report("interrupted-task", "tasks", task, "eligible for recovery, subject to inputs")
        input_problems = resources.unavailable_refs(store, task["refs"])
        if task["state"] == "running":
            input_problems.extend(f"{key} acquired at v{version}" for key, version in task["inputs"].items()
                                  if store.get("resources", key)["version"] != version)
        if input_problems:
            report("stale-task-inputs", "tasks", task, input_problems)
    for thread in store.list("threads"):
        if thread["state"] == "closed":
            continue
        if thread["owner"] not in respond_roles:
            report("unowned-thread", "threads", thread, "Executive must route or restore a recipient")
        if thread["due"] <= now:
            report("overdue-thread", "threads", thread, "Executive must follow up")
    for record in store.list("resources"):
        if record["state"] in {"retired", "withdrawn"}:
            continue
        problems = resources.dependency_problems(store, record)
        if problems:
            report("stale-resource", "resources", record, problems)
    for proposal in store.list("proposals"):
        if proposal["state"] in {"submitted", "approved"}:
            try:
                govern.recheck(store, proposal)
            except RuleError as error:
                report("stale-proposal", "proposals", proposal, str(error))
    return findings


def review_packet(store, key):
    proposal = store.get("proposals", key)
    candidate = proposal["candidate"]
    table = proposal["collection"]
    current = store.get(table, proposal["target"], optional=True)
    try:
        if proposal["state"] in {"submitted", "approved"}:
            govern.recheck(store, proposal)
        blocker = None
    except RuleError as error:
        blocker = str(error)
    meaningful = set(candidate) - {"id", "version"}
    changes = {field: {"before": current.get(field) if current else None, "after": candidate[field]}
               for field in sorted(meaningful)
               if (current.get(field) if current else None) != candidate[field]}
    for field in ("body",):
        if field in changes:
            for direction, value in changes[field].items():
                if isinstance(value, str) and len(value) > 1400:
                    changes[field][direction] = value[:1400] + "… (read the source record)"
    return {"entry": ENTRY, "proposal": f"proposals/{key}",
            "target": f"{table}/{proposal['target']}", "expected": proposal["expected"],
            "proposer": proposal["proposer"], "state": proposal["state"],
            "reason": proposal["reason"], "review": proposal["review"],
            "changes": changes, "dependency_sources": candidate.get("dependencies", {}),
            "provenance_sources": candidate.get("sources", []), "blocker": blocker}


def metrics(store):
    actions = dict(store.db.execute("SELECT action, COUNT(*) FROM events GROUP BY action"))
    latencies = [row["routed"] - row["opened"] for row in store.list("threads")
                 if row["routed"] is not None]
    worker_runs = [json.loads(row[0]) for row in
                   store.db.execute("SELECT data FROM events WHERE action='worker-run' ORDER BY seq")]
    return dict(action_counts=actions, route_samples=len(latencies),
                average_route_seconds=sum(latencies)/len(latencies) if latencies else None,
                worker_runs=len(worker_runs), worker_input_bytes=sum(row["input_bytes"] for row in worker_runs),
                worker_seconds=round(sum(row["seconds"] for row in worker_runs), 3))


def markdown_links(file):
    fenced = False
    for line in file.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
        if not fenced:
            for match in LINK.finditer(line):
                yield match[1] or match[2]


def check_indexes(root, paths):
    root = root.resolve()
    problems = []
    files = set(paths)
    directories = {root}
    for file in files:
        directories.update(parent for parent in file.parents if parent.is_relative_to(root))
        if file.suffix != ".md":
            continue
        for target in markdown_links(file):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (file.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                problems.append(f"{file.relative_to(root)} has a broken link to {target}")
    for directory in sorted(directories):
        index = directory / "README.md"
        if index not in files:
            problems.append(f"{directory.relative_to(root)} needs README.md")
        if directory == root or not index.is_file():
            continue
        parent = directory.parent / "README.md"
        if parent.is_file() and not any(
            (parent.parent / unquote(urlsplit(link).path)).resolve() in {index, directory}
            for link in markdown_links(parent) if not urlsplit(link).scheme and urlsplit(link).path
        ):
            problems.append(f"{parent.relative_to(root)} does not index {index.relative_to(root)}")
    return sorted(problems)


def export(store, destination):
    """Publish a new immutable browse snapshot with links stable across category changes."""
    destination = Path(destination).resolve()
    require(not destination.exists(), "choose a new snapshot destination")
    require(destination.parent.is_dir(), "snapshot destination parent must already exist")
    temporary = Path(tempfile.mkdtemp(prefix=".institution-export-", dir=destination.parent))
    try:
        canonical = temporary / "_records"
        canonical.mkdir()
        directories = {temporary, canonical} | {temporary / domain for domain in DOMAINS}
        listings = {canonical: []}
        for resource in store.list("resources"):
            location = temporary / resource["location"]
            directories.update(parent for parent in (location, *location.parents)
                               if parent.is_relative_to(temporary))
            file = canonical / f"{resource['id']}.md"
            sources = "\n".join(f"- {source}" for source in resource["sources"])
            dependencies = "\n".join(f"- [{key}](./{key}.md), consulted at v{version}"
                                     for key, version in resource["dependencies"].items())
            issues = resources.dependency_problems(store, resource)
            file.write_text(f"# {resource['title']}\n\nExercise record · {resource['kind']} · "
                            f"{resource['state']} · v{resource['version']}\n\n{resource['body']}\n\n"
                            f"## Provenance\n\n{sources or 'No external source listed.'}\n\n"
                            f"## Dependencies\n\n{dependencies or 'No record dependencies.'}\n\n"
                            f"## Reconciliation\n\n{'; '.join(issues) or 'Current at export.'}\n",
                            encoding="utf-8")
            listings[canonical].append(file)
            if resource["state"] not in {"retired", "withdrawn"}:
                listings.setdefault(location, []).append(file)
        for directory in sorted(directories):
            directory.mkdir(exist_ok=True)
            entries = [*sorted(child / "README.md" for child in directories if child.parent == directory),
                       *listings.get(directory, [])]
            links = "\n".join(f"- [{file.parent.name if file.name == 'README.md' else file.stem}]"
                              f"({os.path.relpath(file, directory)})" for file in entries)
            parent = "[Parent index](../README.md)\n\n" if directory != temporary else ""
            (directory / "README.md").write_text(f"# {directory.name if parent else 'Exercise snapshot'}"
                "\n\nDerived, read-only view of the exercise ledger. Refer to the current ledger for decisions.\n\n"
                + parent + links + "\n", encoding="utf-8")
        temporary.rename(destination)
    except BaseException:
        shutil.rmtree(temporary, ignore_errors=True)
        raise
    return {"path": str(destination), "records": len(listings[canonical])}
