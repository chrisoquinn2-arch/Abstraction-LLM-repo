"""Prepare, independently review and enact exercise changes."""

from . import resources
from .store import CAPABILITIES, bounded, domain_name, identifier, require, stamp


def normalize_role(store, key, expected, spec):
    require(key != "exercise-founding-review", "the exercise founding review role is fixed")
    current = store.get("roles", key, optional=True)
    def value(field, default=None):
        return spec.get(field, current.get(field, default) if current else default)

    require(set(spec) <= {"domain", "mission", "interpretation", "guides",
                          "state", "capabilities", "predecessors"}, "unknown role fields")
    domain = domain_name(value("domain"))
    require(not current or domain == current["domain"], "form a successor for a changed domain")
    state = value("state", "active")
    require(state in {"active", "retired"} and (not current or current["state"] == "active"),
            "only active roles can be revised or retired")
    caps = value("capabilities", sorted(CAPABILITIES[domain]))
    require(isinstance(caps, list) and set(caps) <= CAPABILITIES[domain],
            "role capabilities must belong to its domain")
    guides = value("guides", [f"{domain}/skills/README.md"])
    require(isinstance(guides, list) and 0 < len(guides) <= 5, "provide one to five role guides")
    for guide in guides:
        path = resources.safe_relative(guide)
        require(path.parts[0] == domain and path.suffix == ".md", "guide must be a domain Markdown path")
    predecessors = value("predecessors", [])
    require(isinstance(predecessors, list) and len(predecessors) <= 8 and key not in predecessors,
            "provide up to eight other predecessor roles")
    for predecessor in predecessors:
        require(store.get("roles", predecessor)["domain"] == domain, "predecessor domain disagrees")
    return dict(id=key, version=expected or 1, domain=domain, state=state,
                mission=bounded(value("mission"), "role mission"),
                interpretation=bounded(value("interpretation"), "role interpretation"),
                capabilities=sorted(set(caps)), guides=guides, predecessors=predecessors)


def normalize_grant(store, actor, key, expected, spec):
    require(key != "director-root", "the real charter and exercise root are outside this change path")
    current = store.get("grants", key, optional=True)
    if spec.get("state") == "revoked":
        require(set(spec) == {"state"} and current and current["state"] == "active",
                "specify only revoked state for an active grant")
        parent = store.get("grants", current["parent"]["id"])
        require(store.authority(actor, "apply-authority", required=False) or (
            parent["actor"] == actor and store.grant_valid(parent)
        ), "only the exercise Director or current issuing authority may propose revocation")
        return dict(current, state="revoked")
    require(set(spec) <= {"actor", "role", "parent", "capabilities", "state"} and
            spec.get("state", "active") == "active", "invalid grant specification")
    member = store.get("actors", spec.get("actor"))
    role = store.get("roles", spec.get("role"))
    parent = store.get("grants", spec.get("parent", "director-root"))
    require(parent["id"] != key and store.grant_valid(parent) and parent["actor"] == actor,
            "the grant must cite your live issuing grant")
    require(role["state"] == "active", "role is retired")
    capabilities = spec.get("capabilities", role["capabilities"])
    require(isinstance(capabilities, list) and capabilities and
            set(capabilities) <= set(role["capabilities"]), "grant scope exceeds the role")
    if parent["id"] != "director-root":
        parent_role = store.get("roles", parent["role"])
        require(role["domain"] == parent_role["domain"] and "delegate" in parent["capabilities"]
                and set(capabilities) <= set(parent["capabilities"]),
                "delegation exceeds the current issuer's domain or capabilities")
    return dict(id=key, version=expected or 1, actor=member["id"], role=role["id"],
                parent=stamp(parent), role_version=role["version"],
                capabilities=sorted(set(capabilities)), state="active")


def candidate(store, actor, table, key, expected, spec):
    identifier(key)
    require(table in {"roles", "grants", "resources"}, "proposals target roles, grants or resources")
    require(isinstance(spec, dict), "proposal spec must be an object")
    current = store.get(table, key, optional=True)
    require((current["version"] if current else 0) == expected,
            f"stale target {table}/{key}; fetch the current revision")
    if table == "roles":
        return normalize_role(store, key, expected, spec), "governance"
    if table == "grants":
        return normalize_grant(store, actor, key, expected, spec), "governance"
    record = resources.prepare(store, key, expected, spec, reviewed=True)
    return record, record["domain"]


def submit(store, actor, key, table, target, expected, spec, reason, supersedes=None):
    identifier(key)
    record, domain = candidate(store, actor, table, target, expected, spec)
    if table == "grants":
        authority = store.authority(actor, "delegate")
        if record["state"] == "active":
            authority = record["parent"]
    else:
        authority = store.authority(actor, "propose-authority" if table == "roles" else "resource",
                                    domain)
    if supersedes:
        older = store.get("proposals", supersedes)
        require(older["collection"] == table and older["target"] == target,
                "a successor proposal must concern the same target")
    proposal = dict(id=key, version=1, collection=table, target=target, expected=expected,
                    domain=domain, spec=spec, candidate=record, proposer=actor,
                    source_authority=authority, reason=bounded(reason, "proposal rationale"),
                    state="submitted", review=None, supersedes=supersedes)
    return store.save("proposals", proposal, actor, "submit", authority, create=True)


def review(store, actor, key, decision, reason):
    proposal = store.get("proposals", key)
    require(proposal["state"] == "submitted", "proposal is no longer awaiting review")
    require(actor != proposal["proposer"], "proposal requires an independent reviewer")
    authority = store.authority(actor, "review", proposal["domain"])
    require(decision in {"approved", "rejected"}, "review must approve or reject")
    if decision == "approved":
        recheck(store, proposal)
    proposal["review"] = dict(actor=actor, authority=authority, reason=bounded(reason, "review rationale"))
    proposal["state"] = decision
    return store.save("proposals", proposal, actor, "review", authority)


def recheck(store, proposal):
    require(store.live_stamp(proposal["source_authority"]), "proposal's originating authority is stale")
    live, _ = candidate(store, proposal["proposer"], proposal["collection"], proposal["target"],
                        proposal["expected"], proposal["spec"])
    require(live == proposal["candidate"], "dependencies changed; submit a successor proposal")
    if proposal["review"]:
        require(store.live_stamp(proposal["review"]["authority"]), "review authority is stale")
    return live


def apply(store, actor, key, reason):
    proposal = store.get("proposals", key)
    require(proposal["state"] == "approved", "proposal requires a current independent approval")
    table = proposal["collection"]
    record = recheck(store, proposal)
    applies_authority = table != "resources" or record["kind"] == "standard"
    authority = store.authority(actor, "apply-authority" if applies_authority else "resource",
                                proposal["domain"])
    record.update(decision=key, reason=bounded(reason, "application rationale"))
    store.save(table, record, actor, "apply-proposal", authority, create=proposal["expected"] == 0)
    if table in {"roles", "grants"}:
        director = store.get("grants", "director-root")["actor"]
        reviewers = {grant["actor"] for grant in store.list("grants")
                     if grant["role"] is not None and "review" in grant["capabilities"]
                     and store.get("roles", grant["role"])["domain"] == "governance"
                     and store.grant_valid(grant)}
        require(reviewers - {director}, "preserve at least one independent governance reviewer")
    proposal.update(state="applied", applied_version=record["version"], application_reason=record["reason"])
    store.save("proposals", proposal, actor, "enact", authority)
    return record
