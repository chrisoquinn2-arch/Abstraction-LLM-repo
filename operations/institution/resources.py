"""Institutional records, epistemic state and versioned dependencies."""

from pathlib import PurePosixPath

from .store import bounded, domain_name, identifier, require

KIND_DOMAIN = {
    "standard": "governance", "priority": "executive", "plan": "operations",
    "question": "research", "hypothesis": "research", "experiment": "research",
    "evidence": "research", "interpretation": "research", "claim": "research",
    "skill": None, "index": None, "context": None, "procedure": None, "test": None,
}
STATES = {
    "question": {"open", "narrowed", "answered", "withdrawn"},
    "hypothesis": {"provisional", "contested", "withdrawn"},
    "experiment": {"proposed", "ready", "run", "withdrawn"},
    "evidence": {"recorded", "withdrawn"},
    "interpretation": {"provisional", "contested", "withdrawn"},
    "claim": {"provisional", "contested", "supported", "withdrawn"},
}


def safe_relative(path):
    require(isinstance(path, str) and len(path) <= 160, "relative path is too long")
    parts = path.split("/")
    require(all(part and part not in {".", ".."} and
                all(char.isascii() and (char.isalnum() or char in "-_.") for char in part)
                for part in parts), f"unsafe relative path {path!r}")
    return PurePosixPath(path)


def dependency_problems(store, record, active=frozenset()):
    if record["id"] in active:
        return [f"dependency cycle through {record['id']}"]
    active = active | {record["id"]}
    problems = []
    for key, expected in record["dependencies"].items():
        dependency = store.get("resources", key)
        if dependency["version"] != expected:
            problems.append(f"{key} expected v{expected}, current v{dependency['version']}")
        elif dependency["state"] in {"retired", "withdrawn"}:
            problems.append(f"{key} is {dependency['state']}")
        else:
            problems.extend(dependency_problems(store, dependency, active))
    return sorted(set(problems))


def validate_refs(store, refs):
    require(isinstance(refs, list) and len(refs) <= 20 and len(set(refs)) == len(refs),
            "provide at most 20 distinct resource IDs")
    return [store.get("resources", identifier(ref)) for ref in refs]


def unavailable_refs(store, refs):
    problems = []
    for resource in validate_refs(store, refs):
        if resource["state"] in {"retired", "withdrawn"}:
            problems.append(f"{resource['id']} is {resource['state']}")
        problems.extend(dependency_problems(store, resource))
    return sorted(set(problems))


def prepare(store, key, expected, spec, *, reviewed):
    identifier(key)
    require(isinstance(spec, dict), "resource specification must be an object")
    allowed = {"domain", "kind", "state", "title", "body", "location", "sources", "dependencies"}
    require(set(spec) <= allowed, "unknown resource fields")
    current = store.get("resources", key, optional=True)
    require((current["version"] if current else 0) == expected,
            f"stale target resources/{key}; fetch the current revision")
    if current:
        require(current["state"] not in {"withdrawn", "retired"},
                "retired records remain available as historical sources; create a successor")
    def value(field, default=None):
        return spec.get(field, current.get(field, default) if current else default)

    domain = domain_name(value("domain"))
    kind = value("kind")
    require(kind in KIND_DOMAIN and KIND_DOMAIN[kind] in {None, domain},
            f"{kind!r} cannot be owned by {domain}")
    if current:
        require(domain == current["domain"] and kind == current["kind"],
                "create a successor to change a resource's domain or kind")
    state = value("state", "active")
    require(state in STATES.get(kind, {"active", "retired"}), f"invalid {kind} state {state!r}")
    path = safe_relative(value("location", f"{domain}/{kind}"))
    require(path.parts[0] == domain, "the resource location must belong to its domain")
    require(reviewed or (kind != "standard" and state not in {"supported", "ready", "answered",
                                                            "withdrawn", "retired"}
                         and (not current or current["state"] != "supported")),
            "this transition requires a reviewed proposal")
    locations = spec.get("dependencies")
    if locations is None:
        dependencies = dict(current["dependencies"]) if current else {}
    else:
        dependencies = {dep["id"]: dep["version"] for dep in validate_refs(store, locations)}
    sources = value("sources", [])
    require(isinstance(sources, list) and len(sources) <= 12, "provide up to 12 provenance sources")
    sources = [bounded(source, "provenance source", 500) for source in sources]
    require(kind != "evidence" or sources, "evidence requires a source or collection reference")
    record = dict(id=key, version=expected or 1, domain=domain, kind=kind, state=state,
                  title=bounded(value("title"), "title", 160), body=bounded(value("body"), "body", 8000),
                  location=str(path), sources=sources, dependencies=dependencies)
    problems = dependency_problems(store, record)
    require(not problems, "reconcile dependencies: " + "; ".join(problems))
    if state == "supported":
        require(any(store.get("resources", dep)["kind"] == "evidence" for dep in dependencies),
                "a supported claim requires at least one direct evidence reference")
    return record


def revise(store, actor, key, expected, spec, reason):
    record = prepare(store, key, expected, spec, reviewed=False)
    authority = store.authority(actor, "resource", record["domain"])
    reason = bounded(reason, "revision rationale")
    record["reason"] = reason
    return store.save("resources", record, actor, "revise-resource", authority, create=expected == 0)
