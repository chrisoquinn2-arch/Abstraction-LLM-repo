# Requirements, provenance, and proposed verification

**Status:** preliminary requirements derived from the director's comments and tabletop reasoning; **no test execution yet**.

## Requirement provenance
- **D** = expressed by Research Director as design direction.
- **C** = charter requirement.
- **I** = inference from scenarios; subject to challenge.
- **O** = open option rather than requirement.

| ID | Status | Requirement or candidate | Verification question |
| --- | --- | --- | --- |
| R01 | D | Every folder offers README orientation/context and maintenance expectations | Can unfamiliar agents navigate a newly nested topic without full-tree ingestion? |
| R02 | D | Every fresh task session starts at repository root | Can a context-limited agent recover authority and relevant path? |
| R03 | D | Repository organization can be nested, split, merged, revised, and consolidated | Does migration preserve links, authority, and active work? |
| R04 | D | Skills have bounded discoverable contracts and are maintainable (split/merge/generalize/specialize) | Can a new agent select and execute one without loading all skills? |
| R05 | D | Persistent roles hold open-ended responsibilities; not every agent can hold every role | Can a role be dispatched, interpreted, handed off, and revised over several sessions? |
| R06 | D | Every part of the system admits feedback, critique, and proposed change, even contradicting existing law | Can an unauthorized agent raise a challenge without secretly changing the law? |
| R07 | D | Agents can notify and discuss cross-department consequences | Can nonlocal relevant agents see and respond, without reading all traffic? |
| R08 | C | Changes to authority cause dependent permissions/protocols to be reconciled | Does an in-flight task using revoked permission stop or re-authorize? |
| R09 | C | Scientific scope, executive priority, planning, and execution remain distinct functions | Do reports avoid presenting next action as what the findings established? |
| R10 | I | Separate current state, history, evidence, and deliberation semantically | Can a new agent distinguish an approved result from a discussion excerpt? |
| R11 | I | The system survives context loss and interrupted execution | Can an independent fresh instance resume from only task ID and repository? |
| R12 | I | Human review effort is bounded and source-linked | Can a reviewer make the relevant decision without losing caveats? |
| R13 | I | Active-work discoverability and conflict handling | Can two agents work concurrently without silently overwriting each other? |
| R14 | I | Indexes and state views expose staleness and canonical sources | Can a source revision trigger a detectable review of affected summaries? |

## Proposed verification families (not performed)
1. **Startup/recovery:** fresh agent with finite context, absent prior chat, only repository + task ID.
2. **Concurrent work:** independent and overlapping agents, intentional disagreement, conflicting writes.
3. **Authority mutation:** change delegation mid-task, reconcile derived rules, test stale snapshots.
4. **Unknown responsibilities:** simulated role discovers unspecific but legitimate work and proposes revision.
5. **Cross-area signals:** blind routing, dropped messages, flooding, unassigned issue, delayed response.
6. **Structural evolution:** grow a synthetic repository, split/merge nested folders and skills, test retrieval and broken references.
7. **Human review:** short decision packet versus full source, test comprehensibility and limits.

For each test later record: scenario and setup, applicable authority, expected behavior, observation, failure, alternative explanations, cost, and proposed correction. No number or threshold is asserted as validated here.

## Failure taxonomy (opening hypotheses, not established)
- Context loss or insufficient startup orientation.
- Incorrect authority inherited through stale delegation.
- Summary or index promoted to evidence.
- Local optimization that harms cross-team work.
- Role drift, duplicated responsibility, responsibility gaps, over-delegation.
- Forgotten disagreement, unreviewed objection, peer consensus unsupported by independent evidence.
- Broken links and provenance after reorganization.
- Review overload for humans or LLMs.
- Governance overhead exceeding productive research.

## Acceptance evidence still missing
- Tested baseline implementations or reproducible mocks.
- Evidence that agent startup and recovery work within bounded context.
- Evidence that delegated authority and revisions are correctly routed.
- Evidence that cooperative work is recoverable and conflict-safe.
- Evidence that nested maintenance stays affordable as the repository grows.
- Design alternatives and recorded choices for each binding protocol.

Do **not** pass outset task 1 from this document alone.
