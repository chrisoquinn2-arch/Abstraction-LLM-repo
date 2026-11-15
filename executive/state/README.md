# Executive state — live discoverability
**Parent:** [executive](../README.md) · **Status:** prototype navigator, not a replacement for GitHub issue history.

The canonical live working state is in [GitHub Issues](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/issues); document changes and approvals are in [Pull Requests](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/pulls). Search Issues for markers `[work]`, `[forum]`, `[challenge]`, `[exercise]`; inspect title, description, comments, assignee/owner and referenced PR. These markers remain usable if GitHub labels are unavailable.

## Startup and recovery
A new agent starts at root, reads its assigned Issue, the relevant role and domain README, and the latest handoff comment. If no assignment is known, Executive triages new/unowned Issues and [forum/dropbox/](../../forum/dropbox/README.md). On broken links or empty inbox, do not invent state; report source and limitation.

## Current architecture exercise
- [Architectural choice](../../governance/decisions/2026-11-14-file-native-architecture-proposal.md) — proposed, under Director review.
- [Verification](../../operations/tests/README.md) — find test evidence and planned adverse cases.
- The legacy [SQLite PR](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/pull/1) is separate; do not treat it as adopted.

Maintenance: when creating work, link a responsible role, source records and requested response. When finishing, preserve the final disposition and link related knowledge/decisions. Recheck this page whenever the set of canonical interfaces changes.

