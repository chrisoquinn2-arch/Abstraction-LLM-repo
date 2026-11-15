"""Executive dispatch and recoverable task execution."""

import secrets

from . import resources
from .store import bounded, identifier, require

MAX_LEASE = 3600


def public(task):
    return {key: value for key, value in task.items() if key != "lease"}


def live_lease(store, task):
    return task["state"] == "running" and task["expires"] > store.clock() and (
        store.live_stamp(task["authority"])
    )


def dispatch(store, actor, key, role_id, title, objective, priority, refs, thread=None):
    identifier(key)
    authority = store.authority(actor, "dispatch", "executive")
    role = store.get("roles", role_id)
    require(role["state"] == "active" and "work" in role["capabilities"], "role cannot do work")
    require(-100 <= priority <= 100, "priority must be in [-100, 100]")
    resources.validate_refs(store, refs)
    if thread:
        store.get("threads", thread)
    task = dict(id=key, version=1, domain=role["domain"], role=role_id,
                title=bounded(title, "title", 160), objective=bounded(objective, "objective"),
                priority=priority, refs=refs, thread=thread, state="queued", holder=None,
                authority=None, lease=None, expires=None, checkpoint=None, inputs={},
                outcome=None, updated=store.clock())
    return public(store.save("tasks", task, actor, "dispatch", authority, create=True))


def retarget(store, actor, key, expected, role_id, reason):
    authority = store.authority(actor, "dispatch", "executive")
    task = store.get("tasks", key)
    require(task["version"] == expected, "task revision changed")
    require(not live_lease(store, task) and task["state"] != "done",
            "wait for the active lease to release before redispatching")
    role = store.get("roles", role_id)
    require(role["state"] == "active" and role["domain"] == task["domain"]
            and "work" in role["capabilities"], "choose an active work role in this domain")
    task.update(role=role_id, state="queued", holder=None, authority=None, lease=None,
                expires=None, inputs={}, outcome=bounded(reason, "redispatch rationale"), updated=store.clock())
    return public(store.save("tasks", task, actor, "redispatch", authority))


def claim(store, actor, key, seconds):
    task = store.get("tasks", key)
    authority = store.authority(actor, "work", task["domain"], task["role"])
    require(1 <= seconds <= MAX_LEASE, f"lease must last 1–{MAX_LEASE} seconds")
    require(task["state"] in {"queued", "running"} and not live_lease(store, task),
            "task is unavailable; inspect the current state or request redispatch")
    problems = resources.unavailable_refs(store, task["refs"])
    require(not problems, "task inputs need reconciliation: " + "; ".join(problems))
    task.update(state="running", holder=actor, authority=authority, lease=secrets.token_urlsafe(24),
                expires=store.clock() + seconds,
                inputs={ref["id"]: ref["version"] for ref in resources.validate_refs(store, task["refs"])},
                updated=store.clock())
    return store.save("tasks", task, actor, "claim-task", authority)


def available(store, actor, role):
    definition = store.get("roles", role)
    store.authority(actor, "work", definition["domain"], role)
    eligible = (task for task in store.list("tasks", role=role)
                if task["state"] in {"queued", "running"} and not live_lease(store, task)
                and not resources.unavailable_refs(store, task["refs"]))
    return sorted(eligible, key=lambda task: (-task["priority"], task["updated"], task["id"]))


def update(store, actor, key, token, operation, message, seconds=None):
    task = store.get("tasks", key)
    require(isinstance(token, str) and task["holder"] == actor and live_lease(store, task)
            and secrets.compare_digest(task["lease"], token),
            "task lease has expired, been replaced, or lost authority")
    authority = task["authority"]
    if operation == "checkpoint":
        task["checkpoint"] = bounded(message, "checkpoint")
    elif operation == "renew":
        require(isinstance(seconds, int) and 1 <= seconds <= MAX_LEASE,
                f"lease must last 1–{MAX_LEASE} seconds")
        task["expires"] = store.clock() + seconds
    elif operation in {"release", "block", "finish"}:
        if operation == "finish":
            problems = resources.unavailable_refs(store, task["refs"])
            for ref, version in task["inputs"].items():
                if store.get("resources", ref)["version"] != version:
                    problems.append(f"{ref} changed during this lease")
            require(not problems,
                    "record a checkpoint and release or block before taking new inputs: " +
                    "; ".join(problems))
        task.update(state={"release": "queued", "block": "blocked", "finish": "done"}[operation],
                    outcome=bounded(message, "outcome"), lease=None, expires=None)
    else:
        require(False, f"unknown task operation {operation}")
    task["updated"] = store.clock()
    return public(store.save("tasks", task, actor, operation, authority))
