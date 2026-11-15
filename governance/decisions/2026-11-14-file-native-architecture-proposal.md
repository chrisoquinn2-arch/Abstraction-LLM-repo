# ADR-HN-01 — Shared human/agent work in GitHub (proposed)
**Date:** 2026-11-14 · **Status:** PROPOSED for Director audit, **not binding** · **Authority to design:** Director's authorization of an integrated institutional prototype within Charter Article VIII task 1. **Authority to ratify:** reserved by the charter. **Related:** [architecture](../../ARCHITECTURE.md), [PR reviews](../reviews/README.md).

## Problem
The initial scaffold contained navigable Markdown but no working coordination. A separate proposal introduced a local SQLite ledger as canonical for roles, discussions, decisions and state; [Governance rejected that branch for adoption](../reviews/2026-11-14-pr1-governance-disposition.md) because it was not adequately justified against human access and file-first collaboration. The institution must serve people and agents as **participants**, not only as users of software.

## Requirements / constraints
H1. Human opens a department, finds relevant work, adds a discussion or edits a resource using a browser. A GitHub account identity/commit history provides traceability.
H2. Fresh agent finds the same shared records using GitHub tools, without hidden local data or prior chat context.
H3. Roles own responsibilities, including executive routing. Proposals can contradict any policy, but enactment follows valid authority.
H4. Subject hierarchies and localized procedures grow and migrate without losing references.
H5. Concurrent work, evidence status and interrupted work remain inspectable; avoid invented success or silent fallback.
H6. Original chartered outset sequence remains controlling.

## Alternatives and trade-offs
| Alternative | Advantages | Costs / unproved points |
| --- | --- | --- |
| Git Markdown only (including discussion files) | Easiest direct editing and Git provenance; portable, searchable | Hard to notify and coordinate live discussions, conflicts when editing one file, awkward subscriptions |
| GitHub Markdown + Issues + PRs (**selected for trial**) | Native human UI; issue comments, identities, assignments, searchable activity; PR review for file changes; agents have connected tooling | Two linked kinds of record; labels/indexes and routing need maintenance; git merges are not multi-file transactions; GitHub dependence |
| Local SQLite canonical + Git docs | Transactional ledger, concise task lease/recovery semantics | Human participation requires custom UI and consistent export/import, host-local state, opaque without tooling; not adopted |
| GitLab wiki/issues/repo, Notion, Teams/SharePoint | Strong alternate human collaboration affordances | Need connector and authority/provenance evaluation, costs and migration tests; no evidence of superiority yet |

**Decision scope:** Use GitHub as the trial work medium; Git files canonical for institutional documents, Issues for discussions/tasks, PRs for reviewable file changes. No hidden operational database. Automation can check or mirror but not quietly become authority.

## Interaction consequences
- Humans may create a forum Issue through a browser issue template, or create a Markdown intake post (converted to a trackable Issue through an optional GitHub Action after merge; manual intake is a fallback with visible owner).
- Agents maintain role and issue records, not internal private conversations. Executive is responsible for unassigned work and cross-domain notification.
- Documents and related Issue/PR references are bidirectionally linked; a PR does not enact an authority change without the applicable recorded approval.
- Fresh sessions navigate root -> local README -> assignment and linked thread; no CLI required for a human.
- Distinguish errors in GitHub's provider UI, index staleness, insufficient permissions and incorrect scientific content; tests must exercise each relevant boundary.

## Objections and missing proof
Still to verify: agent connector can retrieve all needed issue comments/PR changes across sessions; relevant notifications are actually seen; GitHub Actions permissions for intake; human usability under high volume; costs; link integrity on migration; reliable role/authority reconciliation. Do not convert this proposed ADR to approved law by merging. Record dissent at [Forum](../../forum/README.md) and review in [Governance reviews](../reviews/README.md).

