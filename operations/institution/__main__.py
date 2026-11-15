"""Root entry point for the institutional exercise."""

import argparse
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import time

from . import forum, govern, resources, views, work
from .store import DOMAINS, TABLES, RuleError, Store, require

DEFAULT_DB = views.ROOT / ".institution" / "state.sqlite3"


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--actor", help="registered exercise identity")
    commands = parser.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init", help="initialize an isolated exercise ledger")
    init.add_argument("--exercise", required=True, action="store_true")
    init.add_argument("--director", required=True)
    init.add_argument("--reviewer", required=True)
    add = commands.add_parser("register", help="register a participant identity")
    add.add_argument("member")

    resource = commands.add_parser("revise", help="make an ordinary local resource revision")
    revision_arguments(resource)
    submit = commands.add_parser("submit", help="propose an independently reviewed change")
    submit.add_argument("proposal")
    submit.add_argument("collection", choices=("roles", "grants", "resources"))
    revision_arguments(submit)
    submit.add_argument("--supersedes")
    review = commands.add_parser("review", help="approve or reject a proposed change")
    review.add_argument("proposal")
    review.add_argument("decision", choices=("approved", "rejected"))
    review.add_argument("reason")
    apply = commands.add_parser("apply", help="enact an authorized, reviewed change")
    apply.add_argument("proposal")
    apply.add_argument("reason")

    dispatch = commands.add_parser("dispatch", help="queue a task for a durable role")
    dispatch.add_argument("task")
    dispatch.add_argument("role")
    dispatch.add_argument("title")
    dispatch.add_argument("objective")
    dispatch.add_argument("--priority", type=int, default=0)
    dispatch.add_argument("--ref", action="append", default=[])
    dispatch.add_argument("--thread")
    redirect = commands.add_parser("redispatch", help="resume blocked work or transfer it to a successor role")
    redirect.add_argument("task")
    redirect.add_argument("expected", type=int)
    redirect.add_argument("role")
    redirect.add_argument("reason")
    claim = commands.add_parser("claim", help="claim or recover an available task")
    claim.add_argument("task")
    claim.add_argument("--seconds", type=int, default=900)
    for operation in ("checkpoint", "release", "block", "finish", "renew"):
        update = commands.add_parser(operation, help=f"{operation} work under the current task lease")
        update.add_argument("task")
        update.add_argument("lease")
        if operation == "renew":
            update.add_argument("seconds", type=int)
        else:
            update.add_argument("message")
    worker = commands.add_parser("worker", help="lease one task and start a fresh local worker subprocess")
    worker.add_argument("--seconds", type=int, default=900)
    worker.add_argument("role")
    worker.add_argument("argv", nargs=argparse.REMAINDER,
                        help="after ROLE, pass -- followed by the executable and arguments")

    thread = commands.add_parser("open", help="open a feedback or cross-domain thread")
    thread.add_argument("thread")
    thread.add_argument("domain", choices=DOMAINS)
    thread.add_argument("target", help="record ID, repository path, or responsibility under challenge")
    thread.add_argument("title")
    thread.add_argument("body")
    thread.add_argument("--ref", action="append", default=[])
    thread.add_argument("--window", type=int, default=3600)
    for operation in ("route", "acknowledge", "close", "escalate", "reopen", "reply"):
        response = commands.add_parser(operation, help=f"{operation} a forum thread")
        response.add_argument("thread")
        if operation != "reply":
            response.add_argument("expected", type=int)
        if operation == "route":
            response.add_argument("owner")
        response.add_argument("message")

    boot = commands.add_parser("boot", help="recover the task, owner, navigation and source pointers")
    boot.add_argument("task")
    show = commands.add_parser("show", help="read a specific canonical record")
    show.add_argument("collection", choices=sorted(TABLES))
    show.add_argument("key")
    inbox = commands.add_parser("inbox", help="read a bounded domain queue")
    inbox.add_argument("domain", choices=DOMAINS)
    inbox.add_argument("--limit", type=int, default=12)
    history = commands.add_parser("history", help="read append-only evidence of recorded actions")
    history.add_argument("target", nargs="?")
    history.add_argument("--limit", type=int, default=20)
    packet = commands.add_parser("decision-packet", help="read the grounds, source links and proposed changes")
    packet.add_argument("proposal")
    commands.add_parser("audit", help="detect stranded work, stale authority, inputs and notices")
    commands.add_parser("metrics", help="read observed routing, worker cost and action counts")
    export = commands.add_parser("export", help="publish a derived, linked Markdown snapshot")
    export.add_argument("directory", type=Path)
    commands.add_parser("check-index", help="verify repository indexes and Markdown links")
    return parser.parse_args()


def revision_arguments(parser):
    parser.add_argument("target")
    parser.add_argument("expected", type=int, help="0 for creation; current revision for changes")
    spec = parser.add_mutually_exclusive_group(required=True)
    spec.add_argument("--spec", type=json.loads, help="JSON object")
    spec.add_argument("--file", type=Path, help="file containing a JSON object")
    parser.add_argument("--reason", required=True)


def run_worker(store, actor, role, seconds, command):
    require(command, "supply a local worker command after --")
    with store.transaction(write=True):
        options = work.available(store, actor, role)
        if not options:
            return {"role": role, "state": "idle"}
        task = work.claim(store, actor, options[0]["id"], seconds)
        packet = views.task_packet(store, task["id"])
        packet.update(actor=actor, database=str(store.path.resolve()), lease=task["lease"])
    payload = json.dumps(packet, ensure_ascii=False)
    start = time.monotonic()
    try:
        result = subprocess.run(command, cwd=views.ROOT, input=payload, text=True,
                                timeout=seconds, check=False, stdout=sys.stderr)
        exit_code = result.returncode
        failure = f"worker exit {exit_code}"
    except (OSError, subprocess.TimeoutExpired) as error:
        exit_code = None
        failure = str(error)
    report = dict(role=role, task=task["id"], worker_exit=exit_code,
                  input_bytes=len(payload.encode("utf-8")), seconds=round(time.monotonic() - start, 3))
    with store.transaction(write=True):
        current = store.get("tasks", task["id"])
        if current["lease"] == task["lease"] and work.live_lease(store, current):
            current = work.update(store, actor, task["id"], task["lease"], "release",
                                  f"{failure}; yielded unfinished work")
        report["state"] = current["state"]
        if exit_code != 0:
            report["failure"] = failure
        store.event(actor, "worker-run", f"tasks/{task['id']}", report, task["authority"])
    return report


def handle(args):
    cmd = args.command
    if cmd == "check-index":
        result = subprocess.run(["git", "ls-files", "-z", "-c", "-o", "--exclude-standard"],
                                cwd=views.ROOT, capture_output=True, check=True)
        files = [views.ROOT / os.fsdecode(path) for path in result.stdout.split(b"\0") if path]
        issues = views.check_indexes(views.ROOT, [file for file in files if file.is_file()])
        return {"issues": issues, "paths_checked": len(files)}, bool(issues)
    store = Store(args.db)
    actor = args.actor or os.getenv("INSTITUTION_ACTOR")
    mutating = cmd not in {"boot", "show", "history", "decision-packet", "audit", "metrics", "export", "inbox"}
    if (mutating and cmd != "init") or cmd == "inbox":
        require(actor, "specify --actor before the command or set INSTITUTION_ACTOR")
    if cmd == "worker":
        report = run_worker(store, actor, args.role, args.seconds, args.argv[1:] if args.argv[:1] == ["--"] else args.argv)
        return report, "failure" in report

    with store.transaction(write=mutating, initialize=cmd == "init"):
        return execute(store, actor, cmd, args), False


def execute(store, actor, cmd, args):
    if cmd == "init":
        return store.initialize(args.director, args.reviewer)
    if cmd == "register":
        return store.participant(actor, args.member)
    if cmd in {"revise", "submit"}:
        spec = json.loads(args.file.read_text(encoding="utf-8")) if args.file else args.spec
        if cmd == "revise":
            return resources.revise(store, actor, args.target, args.expected, spec, args.reason)
        return govern.submit(store, actor, args.proposal, args.collection, args.target,
                             args.expected, spec, args.reason, args.supersedes)
    if cmd == "review":
        return govern.review(store, actor, args.proposal, args.decision, args.reason)
    if cmd == "apply":
        return govern.apply(store, actor, args.proposal, args.reason)
    if cmd == "dispatch":
        return work.dispatch(store, actor, args.task, args.role, args.title, args.objective,
                             args.priority, args.ref, args.thread)
    if cmd == "redispatch":
        return work.retarget(store, actor, args.task, args.expected, args.role, args.reason)
    if cmd == "claim":
        return work.claim(store, actor, args.task, args.seconds)
    if cmd in {"checkpoint", "release", "block", "finish", "renew"}:
        return work.update(store, actor, args.task, args.lease, cmd,
                           getattr(args, "message", None), getattr(args, "seconds", None))
    if cmd == "open":
        return forum.open_thread(store, actor, args.thread, args.domain, args.target, args.title,
                                 args.body, args.ref, args.window)
    if cmd in {"route", "acknowledge", "close", "escalate", "reopen", "reply"}:
        return forum.respond(store, actor, args.thread, cmd, getattr(args, "expected", None),
                             args.message, getattr(args, "owner", None))
    if cmd == "boot":
        return views.task_packet(store, args.task)
    if cmd == "show":
        record = store.get(args.collection, args.key)
        if args.collection == "tasks":
            return work.public(record)
        if args.collection == "grants":
            return dict(record, effective=store.grant_valid(record))
        if args.collection == "resources":
            return dict(record, reconciliation=resources.dependency_problems(store, record))
        return record
    if cmd == "inbox":
        return views.inbox(store, actor, args.domain, args.limit)
    if cmd == "history":
        return store.history(args.target, args.limit)
    if cmd == "decision-packet":
        return views.review_packet(store, args.proposal)
    if cmd == "audit":
        return {"findings": views.audit(store)}
    if cmd == "metrics":
        return views.metrics(store)
    if cmd == "export":
        return views.export(store, args.directory)
    raise AssertionError(f"unhandled command {cmd}")


def main():
    try:
        result, failed = handle(parse_args())
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return int(failed)
    except (RuleError, OSError, ValueError, sqlite3.Error, subprocess.CalledProcessError) as error:
        print(f"institution: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
