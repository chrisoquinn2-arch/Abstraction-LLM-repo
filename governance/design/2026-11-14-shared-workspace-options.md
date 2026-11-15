# ADR candidate 01 — Human-and-agent shared workspace

**Status:** PROPOSED — awaiting Research Director review; not ratified law and not authorization for implementation.  
**Scope:** Architecture choice under [Charter Article VIII, outset task 1](../../CHARTER.md).  
**Review thread:** [Issue #4](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/issues/4) · [Review sequence #3](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/issues/3).  
**Source provenance:** Director's 2026-11-14 discussions of direct human entry, editable departmental resources and discussions, shared message-board/Teams-like participation, hierarchical index contracts, persistent roles, and the explicit requirement to justify any platform pivot. Those statements are preserved in this issue/PR description as paraphrases; a verbatim transcript has not been filed or independently audited.

## Decision requested (not yet made)

Select **GitHub-native Markdown + Issues + pull requests** as the *first platform to test*, with the repository and native conversation surfaces forming the human/agent workplace. Do not select GitHub permanently, adopt an operational protocol, or approve a self-booting institution until the specified human/agent usability and recovery tests have been observed.

The decision is **about where participants do institutional work**, not only where software for an institution is developed.

## Non-negotiable evaluation criteria

1. Human can enter through the root and local folder indexes, locate an existing problem or role, read its provenance and context, contribute a comment or Markdown change through a browser, inspect a decision, and receive an actionable response without writing SQL or using a custom agent CLI.
2. Agent can enter through the same root and local indexes, locate source authority and current work with bounded context, contribute to the same canonical discussion, and recover after an interrupted session without former chat history.
3. Separate authority, evidence, proposed changes, active assignments, historical discussion, and derived summaries. A commit/Issue/PR is not by itself a valid constitutional amendment or accepted scientific result.
4. Executive responsibility owns routing, acknowledgment, unassigned issues and boundary disputes; scientific/operational/governance judgment remains with the relevant role.
5. File/folder hierarchy can be subdivided, migrated and audited while preserving access to source records. Human and model tool costs, concurrent work, backup and platform dependency must be examined.
6. Any platform later found inadequate can be replaced through a provenance-preserving migration decision, not a silent change of canonical source.

## Alternatives and capability audit (preliminary, not test evidence)

| Option | Can do | Does not yet establish / relevant costs |
| --- | --- | --- |
| **A. Git/Markdown alone** | Nested human-readable resource files; browser edits; versioned review; portable clones | Efficient back-and-forth forums, notifications, subscriptions, low-conflict concurrent discussion, and role-based issue queues without extra mechanisms |
| **B. GitHub Markdown + Issues/PRs** — proposed trial | Same hierarchy and browser editing; native threaded Issues, comments, author accounts, assigned work and PR discussion/review; connectors available for agent interactions | Robust automatic routing, complete archive export of Issues, durable notification processing, scalable volume, lawful approval beyond GitHub permissions, and verified usability; these must be constructed/tested |
| **C. Git + local SQLite canonical ledger** | Atomic transactional task state, queues, leases and change events; simple local code integration | Human drop-in without custom UI, cross-machine recovery from Git alone, synchronization with Git-based norms, and independently verified identities. A separate design and human-access contract would be necessary |
| **D. Different collaboration service (e.g. GitLab, Notion, Teams/SharePoint)** | Potentially better channels/wiki/collaborative editing and built-in notification surfaces | Actual connector accessibility, cost, provenance, formal authority review, migration fidelity, user learning and portability have not been tested; no demonstrated winner |

**Evaluation status:** This is a design comparison from documented capabilities and known failure modes, *not* a performed comparative experiment. The existence of native GitHub features does not guarantee reliable multiagent institutional behavior.

## Working representation, if trial approved

- **Canonical institutional documents:** Git-tracked Markdown and charter/decision histories. Exact authority states and amendment effects must be documented in these records.
- **Canonical active conversation and task status:** a specified GitHub Issue and its comments, linked bidirectionally to relevant departmental resources. Issues remain open to contradictory contributions; reassignment does not erase the original message.
- **Proposed document changes:** PR + linked decision evidence. Review is recorded, but binding effect depends on lawful authority and an explicit decision.
- **Roles:** persistent versioned responsibility cards, independent of holders. Holder assignment, escalation and handoff reference a canonical Issue. Empty/unowned is a permitted visible state.
- **Optional software:** indexes, checks, routing triggers and exports may help. They must be independently documented, replaceable, and not hide the sole authoritative institutional record in a local app.

## Main objections to the preferred trial

- GitHub Issues and Git files are distinct record systems and may drift. Need explicit linking/ownership rules and audits for mismatches.
- Native notifications are not guaranteed autonomous agent scheduling. A staffed Executive role or an actually verified automation must own pickup.
- GitHub account identity is not proof that a contributor is human or that a vote is an authorized decision.
- GitHub's external service may be unavailable or inaccessible to an agent; a portable backup including Issue history is a design obligation.
- A file-based interface may become cumbersome at scale; evaluate a real medium-size concurrent workload before declaring it adequate.
- No review should compel the Director to abandon the possibility of a different platform, including one with a database, if a capability comparison demonstrates superiority.

## Review questions and gate

**This PR requests only review of the platform hypothesis.** The Director should accept, reject or modify the *trial platform and decision constraints*, recording objections and rationale on Issue #4 / this PR. Then, and only then, a separate implementation PR may establish entry and navigation contracts.

Required later evidence: an unfamiliar human's browser-only contribution and authorized review; a separate agent's cold entry from root+Issue; a wrong-domain discussion safely routed; a role handoff; a link migration; and recovery with no earlier session memory. Record both success and failures, actual costs and source URLs. **No tests are claimed here.**

## Lineage and competing implementation

- [Charter v0.3.1](../../CHARTER.md) defines program authority and resource obligations; it does not select GitHub as permanent medium.
- [Four-domain responsibility design direction](../decisions/2026-11-14-four-domain-responsibility-model.md) gives Executive explicit responsibility for information/context transfer.
- [Audit disposition of SQLite-centered PR #1](../reviews/2026-11-14-pr1-governance-disposition.md) challenged adoption for missing human-interface, portability and design provenance; it did **not** prohibit SQLite categorically.
- Scratch implementations `architecture/human-native-institution` and `architecture/human-native-integration` are **unreviewed**. They may provide examples for separately scoped later PRs but have no authority or implementation acceptance from being committed.
