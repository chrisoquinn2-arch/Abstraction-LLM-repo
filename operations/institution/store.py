"""Storage and live authority for the isolated institutional exercise."""

import contextlib
import json
import re
import sqlite3
import time
from pathlib import Path

DOMAINS = ("governance", "executive", "operations", "research")
LOCAL = frozenset({"resource", "review", "work", "respond"})
CAPABILITIES = {
    "governance": LOCAL | {"propose-authority", "delegate"},
    "executive": LOCAL | {"dispatch", "route", "register", "delegate"},
    "operations": LOCAL | {"delegate"},
    "research": LOCAL | {"delegate"},
}
SEED_ROLES = {
    "governance": "Maintain coherent, justified and revisable institutional standards and delegations.",
    "executive": "Discover responsibility gaps, coordinate priorities and ensure work and context reach owners.",
    "operations": "Keep execution and infrastructure reliable and make costs and failures discoverable.",
    "research": "Discover scientific directions and maintain the evidence, limits and uncertainties of conclusions.",
}
TABLES = frozenset({"actors", "roles", "grants", "tasks", "threads", "resources", "proposals"})
SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS actors (id TEXT PRIMARY KEY, data TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS roles (id TEXT PRIMARY KEY, data TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS grants (id TEXT PRIMARY KEY, data TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, data TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS threads (id TEXT PRIMARY KEY, data TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS resources (id TEXT PRIMARY KEY, data TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS proposals (id TEXT PRIMARY KEY, data TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS events (
    seq INTEGER PRIMARY KEY, time REAL NOT NULL, actor TEXT NOT NULL,
    action TEXT NOT NULL, target TEXT NOT NULL, authority TEXT, data TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS event_target ON events(target, seq);
CREATE INDEX IF NOT EXISTS event_action ON events(action, seq);
CREATE INDEX IF NOT EXISTS task_dispatch ON tasks(
    json_extract(data, '$.role'), json_extract(data, '$.state'),
    json_extract(data, '$.priority') DESC
);
CREATE TRIGGER IF NOT EXISTS preserve_events_update BEFORE UPDATE ON events
BEGIN SELECT RAISE(ABORT, 'events are append-only'); END;
CREATE TRIGGER IF NOT EXISTS preserve_events_delete BEFORE DELETE ON events
BEGIN SELECT RAISE(ABORT, 'events are append-only'); END;
"""


class RuleError(Exception):
    """An invalid request or a conflict with the institution's current state."""


def require(condition, message):
    if not condition:
        raise RuleError(message)


def identifier(value):
    require(isinstance(value, str) and re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", value),
            "IDs use 1–64 lowercase letters, digits or hyphens, and start alphanumerically")
    return value


def bounded(value, label, limit=2400):
    require(isinstance(value, str) and 0 < len(value.strip()) <= limit,
            f"{label} must contain 1–{limit} characters")
    return value.strip()


def domain_name(value):
    require(value in DOMAINS, f"unknown domain {value!r}")
    return value


def pack(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def stamp(record):
    return {"id": record["id"], "version": record["version"]}


class Store:
    def __init__(self, db, clock=time.time):
        self.path = Path(db)
        self.clock = clock
        self.db = None

    @contextlib.contextmanager
    def transaction(self, *, write=False, initialize=False):
        if initialize:
            self.path.parent.mkdir(parents=True, exist_ok=True)
        else:
            require(self.path.is_file(), "ledger missing. Start at the repository README")
        mode = "rwc" if initialize else "rw" if write else "ro"
        conn = sqlite3.connect(f"{self.path.resolve().as_uri()}?mode={mode}", uri=True,
                               timeout=10, isolation_level=None)
        self.db = conn
        conn.row_factory = sqlite3.Row
        try:
            if initialize:
                conn.executescript("BEGIN IMMEDIATE;\n" + SCHEMA)
            else:
                conn.execute("BEGIN IMMEDIATE" if write else "BEGIN")
                row = conn.execute("SELECT value FROM meta WHERE key='format'").fetchone()
                require(row is not None and row[0] == "1", "unsupported ledger format")
            yield self
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            self.db = None
            conn.close()

    def get(self, table, key, optional=False):
        require(table in TABLES, f"unknown collection {table}")
        row = self.db.execute(f"SELECT data FROM {table} WHERE id=?", (key,)).fetchone()
        if row is None:
            require(optional, f"{table}/{key} does not exist")
            return None
        return json.loads(row[0])

    def list(self, table, **filters):
        require(table in TABLES, f"unknown collection {table}")
        query = f"SELECT data FROM {table}"
        if filters:
            query += " WHERE " + " AND ".join("json_extract(data, ?) = ?" for _ in filters)
        parameters = [item for key, value in filters.items() for item in (f"$.{key}", value)]
        return [json.loads(row[0]) for row in self.db.execute(query + " ORDER BY id", parameters)]

    def save(self, table, record, actor, action, authority=None, *, create=False):
        require(table in TABLES, f"unknown collection {table}")
        if create:
            require(self.get(table, record["id"], optional=True) is None,
                    f"{table}/{record['id']} already exists")
            self.db.execute(f"INSERT INTO {table} VALUES (?, ?)", (record["id"], pack(record)))
        else:
            current = self.get(table, record["id"])
            record["version"] = current["version"] + 1
            self.db.execute(f"UPDATE {table} SET data=? WHERE id=?",
                            (pack(record), record["id"]))
        event_data = {key: val for key, val in record.items() if key != "lease"}
        self.event(actor, action, f"{table}/{record['id']}", event_data, authority)
        return record

    def event(self, actor, action, target, data, authority=None):
        self.db.execute(
            "INSERT INTO events(time, actor, action, target, authority, data) VALUES (?, ?, ?, ?, ?, ?)",
            (self.clock(), actor, action, target, pack(authority) if authority else None, pack(data)),
        )

    def history(self, target=None, limit=20):
        require(1 <= limit <= 100, "history limit must be between 1 and 100")
        query = "SELECT * FROM events"
        parameters = (limit,)
        if target:
            query += " WHERE target = ?"
            parameters = (target, limit)
        rows = self.db.execute(query + " ORDER BY seq DESC LIMIT ?", parameters)
        return [dict(row, data=json.loads(row["data"]), authority=json.loads(row["authority"])
                     if row["authority"] else None) for row in rows]

    def initialize(self, director, reviewer):
        identifier(director)
        identifier(reviewer)
        require(director != reviewer, "the exercise needs distinct Director and founding reviewer identities")
        require(self.db.execute("SELECT 1 FROM meta WHERE key='format'").fetchone() is None,
                "ledger already initialized")
        self.db.execute("INSERT INTO meta VALUES ('format', '1'), ('mode', 'isolated-exercise')")
        self.save("actors", {"id": director, "version": 1, "kind": "exercise-director"},
                  director, "initialize", create=True)
        for domain, mission in SEED_ROLES.items():
            role = dict(id=domain, version=1, domain=domain, mission=mission,
                        interpretation="Discover missing duties and route boundary problems.",
                        guides=[f"{domain}/skills/README.md"], state="active", predecessors=[],
                        capabilities=sorted(CAPABILITIES[domain]))
            self.save("roles", role, director, "seed-role", create=True)
        self.save("grants", dict(id="director-root", version=1, actor=director, role=None,
                                 parent=None, role_version=None, capabilities=["*"], state="active"),
                  director, "seed-exercise-authority", create=True)
        self.save("roles", dict(id="exercise-founding-review", version=1, domain="governance",
                                mission="Provide an independent review path during exercise bootstrap.",
                                interpretation="Review governance changes within the exercise.",
                                guides=["governance/skills/README.md"], state="active", predecessors=[],
                                capabilities=["review"]), director, "seed-founding-review-role", create=True)
        self.save("actors", {"id": reviewer, "version": 1, "kind": "participant"},
                  director, "seed-founding-reviewer", create=True)
        self.save("grants", dict(id="founding-reviewer", version=1, actor=reviewer, role="exercise-founding-review",
                                 parent={"id": "director-root", "version": 1}, role_version=1,
                                 capabilities=["review"], state="active"),
                  director, "seed-exercise-authority", {"id": "director-root", "version": 1}, create=True)
        return {"director": director, "reviewer": reviewer, "mode": "isolated-exercise"}

    def grant_valid(self, grant, seen=frozenset()):
        if not grant or grant["state"] != "active" or grant["id"] in seen:
            return False
        if grant["id"] == "director-root":
            return True
        role = self.get("roles", grant["role"])
        if role["state"] != "active" or role["version"] != grant["role_version"]:
            return False
        parent = self.get("grants", grant["parent"]["id"])
        if parent["version"] != grant["parent"]["version"]:
            return False
        if not self.grant_valid(parent, seen | {grant["id"]}):
            return False
        scope = set(grant["capabilities"])
        return scope <= set(role["capabilities"]) and (
            parent["id"] == "director-root" or
            (scope <= set(parent["capabilities"]) and "delegate" in parent["capabilities"]
             and self.get("roles", parent["role"])["domain"] == role["domain"])
        )

    def authority(self, actor, capability, domain=None, role=None, required=True):
        self.get("actors", actor)
        for grant in self.list("grants", actor=actor):
            if not self.grant_valid(grant):
                continue
            if grant["id"] == "director-root":
                if role is None:
                    return stamp(grant)
                continue
            if capability not in grant["capabilities"]:
                continue
            definition = self.get("roles", grant["role"])
            if (domain is None or domain == definition["domain"]) and (
                    role is None or role == definition["id"]):
                return stamp(grant)
        require(not required, f"{actor} lacks current {capability} authority"
                f"{' for ' + (role or domain) if role or domain else ''}")
        return None

    def live_stamp(self, reference):
        if not reference:
            return False
        grant = self.get("grants", reference["id"])
        return grant["version"] == reference["version"] and self.grant_valid(grant)

    def participant(self, actor, member):
        authority = self.authority(actor, "register", "executive")
        identifier(member)
        return self.save("actors", {"id": member, "version": 1, "kind": "participant"},
                         actor, "register", authority, create=True)
