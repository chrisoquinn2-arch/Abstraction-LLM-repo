# Human-native research institution — architectural contract
**Status:** proposed prototype design; not ratified institutional law.
**Authority:** Charter v0.3.1, Article VIII outset task 1, Director authorization to construct a substantial prototype for review.
**Decision:** [ADR-HN-01](governance/decisions/2026-11-14-file-native-architecture-proposal.md).

## The actual workplace
GitHub is the human/agent shared institution, not just the development host for another application.
- **Git Markdown files** are canonical for governing documents, long-form knowledge, indexes, role contracts, project context, decisions, and reproducible methods.
- **GitHub Issues and their comments** are canonical for live discussion, feedback, dispatchable tasks, acknowledgments, and escalation. They have human-facing web editing, author identity and history. Issues must link to their department's files, and local indexes link to issue searches or specific threads.
- **Pull requests** are canonical change proposals for versioned documents, executable procedures and other changes requiring review; a commit by itself does not ratify a rule.
- **GitHub Actions and optional scripts** *observe, index and check* these records; they must not maintain a second hidden authoritative ledger. Agents can operate with GitHub connectors and humans with browser UI. Automation is replaceable.

An issue is a record of discussion, **not** binding policy or accepted evidence. The binding effect of a change requires the charter's actual authorization and an explicit recorded disposition. Draft protocol text is not binding.

## Four responsibilities, not four stages
| Responsibility | Owns | Does not thereby control |
| --- | --- | --- |
| Governance | Ideals, normative standards, powers, rationale, constitutional and subordinate change procedures | Science or every operational detail |
| Executive | Transport of context/information, issue receipt, ownerless work, dispatch, escalation and cross-domain decision routing | Scientific findings or law by mere routing |
| Operations | Feasibility, infrastructure, implementation, maintenance, cost, live execution and progress | Authority to change a standard |
| Research | Questions, directions, experiments, understanding, interpretations and epistemic limitations | Program-wide allocation merely by scientific interest |

Each domain has its own README, protocols, skills, tests and discussion affordances where relevant. Common interfaces remain common. Routing is not a hierarchy of truth. Departments exchange reasons, source links, status and requests both ways.

## Startup and human drop-in
1. Enter [root README](README.md); identify charter, current outset stage and whether a document is ratified, draft, exercise or archival.
2. Choose a domain README, then topic/project README. Do not ingest every other folder.
3. To **talk**, open or comment on an Issue using the [Forum](forum/README.md) (browser-based), or add an initial Markdown post in [forum/dropbox](forum/dropbox/README.md). The post-to-issue automation is optional and subject to validation; even when it fails, the submission remains in Git for manual executive triage.
4. To **change a document**, use GitHub's Edit/Pull request UI. Ordinary authorized maintenance can be delegated; normative effect follows authority and review, not merge alone.
5. To **work**, find the Executive's live issue board and roles. Claim/assign an Issue, keep durable status and links, and leave a handoff. A new agent can recover from GitHub and issue history without the former session transcript.

## Object schema and authoritative state
- **README**: one per directory, with purpose, parent/authority, children, where to work, maintenance, outstanding concerns.
- **Role record**: purpose/open-ended success condition, domain, scope, authority, current interpretation, holder (possibly unassigned), obligations, dependencies, status.
- **Issue**: native author/created timestamp, type and target, department, responsible role or pending assignment, relevant links, explicit next step and status. Labels are navigation aids; inspect the issue history to understand revisions.
- **Decision record**: ID, category, sources, alternatives, decision authority, rationale, status, effective scope/date, review and downstream reconciliation. Design records cannot self-ratify.
- **Evidence/research record**: epistemic state, source and provenance, what it does/doesn't establish, dependencies, objections and later revisions.
- **Handoff**: link to Issue, authoritative record versions/commits, status, actions performed, blockers, unresolved objections, next responsible role.

## Interfaces and feedback
All actors may challenge any file, rule, role, or process by opening an Issue. Executive owns delivery and assignment; Governance interprets legal effect; a scientific claim is judged through Research, not by an issue label. Cross-domain disagreements remain visible. A message must not vanish merely because it arrived under the wrong category.

For intake, assign **one accountable coordinating owner** and *zero or more consulted/recipient domains*. Do not bind the sender's initial category as immutable jurisdiction. Executive must acknowledge unowned and overdue issues; domain recipients give substantive disposition. Independent disagreement and rejected alternatives remain linked.

## Risks and trade-offs
Git provides provenance and editable files, but merges are not transactional across unrelated documents. Issues give accessible threads but fragment live state from long-form files. Automation needs GitHub permissions and must not silently change governing authority. Search/labels can go stale. High-volume programs may need a different platform; evaluate actual navigation, routing latency, human effort, agent tool cost, concurrent editing and archive portability before a migration. No comparative platform test has yet been run.

## Verification and gate
See [test index](operations/tests/README.md) and [verifier](tools/README.md). Required adverse cases: new human and fresh LLM cold start; wrong-domain notice; dissent against law; conflicting edits; role turnover; directory migration; authority change and dependent review; broken link; unresolved issue detection; experiment provenance; handoff without prior chat. Exercise artifacts must remain identifiable as exercises during Outset Task 1. The Director reviews the resulting PR; this specification and implementation are not gate approval.

