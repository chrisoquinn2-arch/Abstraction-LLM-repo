"""Discussion, routing, receipt and accountable disposition."""

from .resources import validate_refs
from .store import bounded, domain_name, identifier, require


def open_thread(store, actor, key, domain, target, title, body, refs, window=3600):
    store.get("actors", actor)
    identifier(key)
    validate_refs(store, refs)
    require(1 <= window <= 30 * 86400, "response window must be between one second and 30 days")
    thread = dict(id=key, version=1, domain=domain_name(domain), state="unrouted", owner=None,
                  author=actor, target=bounded(target, "challenge target", 240),
                  title=bounded(title, "title", 160), body=bounded(body, "opening grounds"),
                  refs=refs, opened=store.clock(), routed=None, due=store.clock() + window,
                  window=window, acknowledged=None, resolution=None, escalations=0)
    return store.save("threads", thread, actor, "open-thread", create=True)


def respond(store, actor, key, operation, expected, message, owner=None):
    store.get("actors", actor)
    thread = store.get("threads", key)
    message = bounded(message, "forum message")
    if operation == "reply":
        store.event(actor, "reply", f"threads/{key}", {"body": message})
        return {"thread": key, "state": thread["state"]}
    require(expected == thread["version"], "thread revision changed")
    if operation in {"route", "escalate", "reopen"}:
        authority = store.authority(actor, "route", "executive")
        if operation == "route":
            require(thread["state"] != "closed", "reopen the thread before routing")
            role = store.get("roles", owner)
            require(role["domain"] == thread["domain"] and role["state"] == "active"
                    and "respond" in role["capabilities"], "route to an active recipient in this domain")
            thread.update(owner=owner, state="routed", acknowledged=None, routed=store.clock(),
                          due=store.clock() + thread["window"])
        elif operation == "escalate":
            require(thread["state"] != "closed", "thread is closed")
            thread["escalations"] += 1
        else:
            require(thread["state"] == "closed", "only closed threads can reopen")
            thread.update(owner=None, state="unrouted", acknowledged=None, resolution=None,
                          routed=None, due=store.clock() + thread["window"])
    else:
        require(thread["owner"] is not None, "Executive must route the thread first")
        authority = store.authority(actor, "respond", thread["domain"], thread["owner"])
        if operation == "acknowledge":
            require(thread["state"] == "routed", "thread is not awaiting acknowledgment")
            thread.update(state="acknowledged", acknowledged=store.clock(),
                          due=store.clock() + thread["window"])
        elif operation == "close":
            require(thread["state"] == "acknowledged", "acknowledge the thread before closure")
            thread.update(state="closed", resolution=message, closed=store.clock())
        else:
            require(False, f"unknown forum operation {operation}")
    thread["last_reason"] = message
    return store.save("threads", thread, actor, operation, authority)
