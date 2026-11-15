# Parallel work, review, and reopening — candidate coordination contract

**Status:** PROPOSED FOR REVIEW (not ratified, not operational instruction).  
**Scope:** Article VIII outset task 1; GitHub working-interface conventions, not constitutional amendment.  
**Decision discussion:** [Issue #6](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/issues/6)  
**Source/provenance:** [Director's objection to serial gates in Issue #3](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/issues/3#issuecomment-6887191630); [subsequent no-further-objection](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/issues/3#issuecomment-6887390043); [trial platform choice in PR #5](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/pull/5). This is the architect's proposed interpretation; it has not been approved as a governance protocol.

## Why this exists / what would change

**Current state:** GitHub hosts the charter, file scaffolding, issue discussions and an accepted-for-trial platform ADR, but there is **no approved convention** for tracking parallel dependent reviews, distinguishing review from adoption/verification, or reopening an issue after later evidence. [Roadmap Issue #3](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/issues/3) contains an initial sequential plan that the Director expressly challenged.

**Desired effect:** A reader starting from the repository and any linked Issue should be able to determine: which responsibilities are active, who is accountable for each decision and follow-up, what work can proceed in parallel, what specifically blocks acceptance, what was reviewed and by whom, and what evidence would reopen a settled question. This must work through GitHub's ordinary web interface as well as supported agent tools.

**Proposed delta:** Adopt a *parallel review network*: Issues are persistent work/discussion threads; PRs contain independently reviewable file changes; cross-links express dependencies; explicit status, provenance and revision-specific dispositions make review possible without a master queue or hidden runtime. A single area may be revisited whenever its assumptions fail. No PR can self-promote a higher-authority decision.

## Mechanism candidate

### Issue and PR relationships

- Create an Issue for an identifiable design, decision, failure, review, role gap or work responsibility. The opening message contains purpose, requested change, governing source, owner or **unassigned**, relevant material, affected domains, alternatives, expected result, outstanding questions and next action.
- Add a PR for a cohesive proposed change, linking its originating Issue(s), exact diff scope, why and how, alternatives, provenance of discussions, state of dependencies, test evidence and *decision requested*. Do not combine unrelated approvals merely because the code or files are in one branch.
- Multiple PRs may be **prepared and reviewed in parallel**. An affected PR links to the others; it need not stop development, but cannot claim an implemented/delegated/effective change when its authority dependency remains unresolved.
- Distinguish **consulted domains** from **accountable coordinator** and from **substantive authority**. Executive tracks missing recipients; Governance approves binding standards where authorized; Operations tests execution; Research judges intellectual evidence.
- The original Issue/PR discussion is the canonical record of why the change was considered. An ADR may summarize, but cannot substitute for missing discussion by retroactive assertion.

### Status table and tagging

| Visible status | Meaning | Not interchangeable with |
| --- | --- | --- |
| **Proposed** | New claim/change under discussion; no approval | Ready to merge |
| **In review** | Relevant reviewers asked to evaluate exact version | Accepted |
| **Blocked** | Specific dependency, absent authority or evidence prevents the next action; owner and unblock condition identified | Rejected |
| **Accepted for trial** | Reviewer permits bounded experiment with known limits | Ratified law or verified success |
| **Implemented** | Files/tools/process changed; reference the commit/PR | Correct or validated behavior |
| **Verified** | Named tests or observations passed under stated assumptions, with links | Universal correctness or authority |
| **Rejected** | Competent decision authority declined the proposal; reasons preserved | Closed as irrelevant |

These tags are *descriptive*. In GitHub use bracketed title prefixes such as `[design]`, `[coordination]`, `[challenge]` and `[blocked]` until the label vocabulary and permissions are established. Labels, a closed Issue, green CI or a merged PR alone do not confer authority. A reviewer must record the kind of acceptance and exact revision when the difference matters. A human and LLM may share a connected GitHub login, so LLM-authored comments must begin `[LLM]` and human provenance must not be inferred from account alone.

**Table / discovery contract:** The associated coordination Issue should expose a short, maintained table of linked work items: `Issue/PR | intent | responsibility | holder or vacancy | status | prerequisites | next review/action`. Link rather than copy the entire content. This is an interface proposal, **not** a demand that every issue or folder maintain a second status database. A GitHub Projects board is an optional later alternative after actual permissions/cost validation.

### Closing, re-opening, and revision changes

1. Record a reasoned final disposition in the Issue/PR before closure, including deciding authority, reviewed revision, outstanding dissent and affected work. Closing a discussion is not ratification of its scientific or governance conclusions.
2. Reopen when new evidence contradicts an assumption, a higher authority changes, unaddressed stakeholder input arrives, verification fails, a dependency breaks, or the previous disposition was exceeded.
3. For an **Issue**, reopen that Issue with a reason, link to the old review, and update its outstanding action. For a **closed unmerged PR**, reopening can be requested if the branch and review are still meaningful; if the source changes, renewed review is needed. A **merged PR cannot be reopened as an active change**; use a new linked corrective PR and preserve the original merge history. Avoid rewriting prior justifications to conceal the change.
4. When scope or authority is uncertain, explicitly mark blocked and seek proper review. Any participant may lodge an objection; ability to raise an Issue is distinct from power to approve a change.
5. Following structural moves or authority revisions, owning roles inspect linked Issues/PRs and dependent documents; missing reconciliation remains a visible open task.

## Alternatives and weaknesses

- **Serial universal PR gates:** easy to order but prevents concurrent refinement of coupled responsibilities, and the Director explicitly objected.
- **Omnibus PR:** simplifies initial construction but hides independently reviewable decisions, dilutes provenance and makes rollback hard.
- **Parallel Issues/PRs with explicit dependencies (candidate):** allows coupled work with localized approvals; costs include cross-link maintenance and tracking overdue reviews.
- **Centralized automated dashboard:** might improve high-volume discoverability but risks duplicated status, broken sync and extra platform cost; evaluate after a small live workload.

This candidate does not claim that GitHub issue tagging is sufficient by itself. Native notifications are not a verified autonomous agent scheduler. Human and agent cold-entry, changed-reviewer cases, dependency links, and reopening need observed exercises.

## Acceptance test / failure triggers

A controlled scenario opens three related Issues (Governance authority, Executive routing, Operations procedure), with separate PRs developed simultaneously. Introduce a changed source authority and a conflicting test result. Ask a fresh human and a fresh agent to locate the responsible owner, verify the applicable review state and evidence, identify which PR can be independently reviewed, reopen an invalidated decision, and leave an auditable next action. Record links, review time, missing context, misrouted notices and unresolved objections.

Failures to discover ownership, repeated stale tables, overloaded notification traffic or ambiguity about review vs binding approval trigger an explicit redesign of this contract. **No such test is claimed completed.**

## Decision being requested

Does this candidate solve the Director's objection to linear PR gates **well enough to implement and test**, subject to revision? A favorable comment or merge of this document would record a design direction, not by itself authorize arbitrary edits, delegation, charter modification, or a complete operating system.
