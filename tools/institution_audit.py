#!/usr/bin/env python3
"""Read-only audit of the file-native institution's navigational contracts.

This tool checks *structural claims* only. It cannot establish lawful authority,
scientific truth, human accessibility, or reliability of unattended GitHub Actions.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(<([^>]+)>\)|(?<!!)\[[^\]\n]+\]\(([^\s)]+)(?:\s+[^)]*)?\)")
SKIP = {".git", ".venv", "__pycache__", ".pytest_cache", ".institution", "node_modules", ".mypy_cache"}
REQUIRED_FORMS = {"discussion.yml", "challenge.yml", "work.yml"}


def links_from_text(text: str) -> list[str]:
    """Extract local Markdown targets, ignoring fenced code."""
    fenced = False
    found: list[str] = []
    for line in text.splitlines():
        if line.lstrip().startswith(("~~~", "```")):
            fenced = not fenced
            continue
        if not fenced:
            found.extend((m.group(1) or m.group(2)) for m in LINK.finditer(line))
    return found


def local_target(path: Path, target: str) -> Path | None:
    url = urlsplit(target)
    if url.scheme or url.netloc or target.startswith("#") or not url.path:
        return None
    return (path.parent / unquote(url.path)).resolve()


def check(root: Path) -> list[str]:
    """Check links, directory indexing, decision records, and human issue entry."""
    root = root.resolve()
    problems: list[str] = []
    if not (root / "CHARTER.md").is_file():
        problems.append("root: CHARTER.md missing")
    if not (root / "README.md").is_file():
        problems.append("root: README.md missing")
    files = [p for p in root.rglob("*") if p.is_file()
             and not set(p.relative_to(root).parts).intersection(SKIP)]
    dirs = sorted({root} | {ancestor for p in files for ancestor in p.parents
                           if ancestor == root or root in ancestor.parents})
    for directory in dirs:
        rd = directory / "README.md"
        rel = directory.relative_to(root)
        if not rd.is_file():
            problems.append(f"{rel}: missing README.md")
            continue
        text = rd.read_text(encoding="utf-8")
        if len(text.strip()) < 45 or "maintenance" not in text.lower():
            problems.append(f"{rel}: README lacks useful context/maintenance")
        if directory != root:
            parent = directory.parent / "README.md"
            if parent.is_file():
                child = rd.resolve()
                targets = {local_target(parent, x) for x in
                           links_from_text(parent.read_text(encoding="utf-8"))}
                if child not in targets and directory.resolve() not in targets:
                    problems.append(f"{parent.relative_to(root)}: does not index {rd.relative_to(root)}")
    for file in files:
        if file.suffix.lower() != ".md":
            continue
        for href in links_from_text(file.read_text(encoding="utf-8")):
            target = local_target(file, href)
            if target is not None and (not target.is_relative_to(root) or not target.exists()):
                problems.append(f"{file.relative_to(root)}: broken local link {href}")
    decisions = root / "governance" / "decisions"
    if decisions.is_dir():
        for file in decisions.glob("*.md"):
            if file.name == "README.md":
                continue
            content = file.read_text(encoding="utf-8")
            if not re.search(r"\bStatus\s*:", content[:1800], re.I):
                problems.append(f"{file.relative_to(root)}: decision needs explicit Status")
            if not re.search(r"\bAuthority\b|\bDirector\b", content[:2600], re.I):
                problems.append(f"{file.relative_to(root)}: decision needs authority provenance")
    forms = root / ".github" / "ISSUE_TEMPLATE"
    for name in REQUIRED_FORMS:
        path = forms / name
        if not path.is_file():
            problems.append(f".github/ISSUE_TEMPLATE/{name}: missing browser issue form")
        elif not all(x in path.read_text(encoding="utf-8") for x in ("name:", "description:", "body:")):
            problems.append(f".github/ISSUE_TEMPLATE/{name}: malformed issue form")
    for post in (root / "forum" / "dropbox").glob("*.md"):
        if post.name == "README.md":
            continue
        text = post.read_text(encoding="utf-8")
        if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9-]+\.md", post.name):
            problems.append(f"{post.relative_to(root)}: use dated slug naming")
        if not re.search(r"^#\s+\S", text, re.M):
            problems.append(f"{post.relative_to(root)}: post needs title")
        for required in ("Author", "Contribution", "Requested response"):
            if required.lower() not in text.lower():
                problems.append(f"{post.relative_to(root)}: post needs {required}")
    return sorted(set(problems))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check",))
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings = check(args.root)
    if args.json:
        print(json.dumps({"status": "pass" if not findings else "fail", "findings": findings}, indent=2))
    else:
        for finding in findings:
            print("FAIL:", finding)
        print(f"{len(findings)} structural issue(s).")
        if not findings:
            print("Structural checks pass; human/agent governance interactions remain unverified.")
    return int(bool(findings))


if __name__ == "__main__":
    raise SystemExit(main())

