# Institutional prototype design

Start with the [construction decision](../decisions/2026-11-14-institutional-prototype.md) and [governing contract](../protocols/README.md). This design describes an exercise institution under Outset Task 1.

## Ownership and interaction

| Source | Transfers | Receiving obligation |
| --- | --- | --- |
| Research | A discrepancy with evidence and limits on what can be inferred | Executive finds the affected domain and tracks receipt. Governance handles rule adequacy; Operations handles implementation defects. |
| Executive | Assigned work, priority rationale, unresolved notices | Each domain acknowledges and records its own judgment. Executive checks overdue and ownerless work. |
| Operations | Feasibility, implementation failures, costs, repair and recovery | Governance reviews consequences for standards. Executive updates commitments. Research evaluates the consequences for interpretation. |
| Governance | Effective revisions with independent review and impacted dependencies | Domain maintainers reconcile dependent resources; Executive exposes stranded work; Research revisits conclusions only as evidence warrants. |
| Any participant | An observation, disagreement, challenge or proposed revision | The thread remains open until an accountable recipient records disposition. |
| Director | Decisions applying a reviewed exercise change and separately, any real gate decision | The runtime records only the exercise decision. Program-wide adoption follows the charter. |

## Representations and invariants

- Git supplies root navigation, role guides and formal design records. The local ledger is canonical for exercise roles, delegations, tasks, notices, proposals and versioned resources. Views, exports and packets point back to these records.
- The ledger records actor, authority where applicable, target, revision and grounds in the same transaction as each change. Public IDs identify durable records. An assignment's short-lived lease includes a separate session token; a fresh holder reads checkpoint history and obtains a new token.
- Current authority is the intersection of a role's allowed capabilities, the grant scope and its live parent chain. A stale role or parent revision suspends derived grants. Changing authority never rewrites the authority recorded for earlier actions.
- A proposal pins its target version and consulted dependencies. It requires a separate reviewer. The system rechecks authority and current revisions when applying a change. The code treats review of a role or grant as governance work even if its operational effect is elsewhere.
- Resource dependencies store stable IDs and the versions consulted. A moved resource retains its ID. Staleness is derived recursively. A worker sees blockers before relying on a stale source, while checkpoints or a release can still preserve work.
- The institution uses small referenced context packets for each domain and task. Durable discussion and reasons remain available by ID. Shared indexes carry pointers and local maintenance instructions.
- Run the prototype with cooperating workers on one machine using a shared checkout and ledger. A worker can be a human, an existing agent client, or a subprocess invoked through the worker entry point. A valid actor ID is an attribution mechanism for a trusted local group. Operating-system access controls govern access to the checkout and ledger.

## Failure paths and review

Worker interruption leaves an expiring lease and durable checkpoints. Overlapping writes use SQLite writer transactions and version checks. Stale or withdrawn authority appears in the consistency audit and blocks further use. Unacknowledged and unresolved threads remain discoverable. Consequential changes are held for independent review. Closing a thread records a disposition and leaves the scientific resource's epistemic status to the Research path.

The [runtime guide](../../operations/institution/README.md) defines recovery commands, operating procedures, fixture execution and review. See [Operations tests](../../operations/tests/README.md) for implemented verification and review limits. Evidence of model judgment and human review cost belongs in the audit record when collected.
