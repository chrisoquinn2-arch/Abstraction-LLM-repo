# Independent audit brief — Integrated research-institution prototype

**Date:** 2026-11-14  
**Status:** Advisory review brief; not an approved protocol, implementation, audit result, or gate decision.  
**Author:** Independent auditing instance, at Research Director's request.  
**Audience:** Work-mode implementation instance and future governance reviewers.  
**Applicable scope:** [Ratified Charter v0.3.1](../../CHARTER.md), Article VIII **outset task 1**.  
**Evidence boundary:** Retrospective of the Director's requirements, prior design discussions and the [documented four-domain model](../decisions/2026-11-14-four-domain-responsibility-model.md). This brief **does not claim to have inspected or tested** Work-mode outputs. Recheck the current repository and decisions before acting.

## Executive assessment

The Director requested a **committed, integrated, self-bootstrapping prototype of the research institution**, **not** an MVP, a skeleton of directories, or a toy four-agent role-play. The earlier prototype proposal ([P0](../../operations/design/06-four-domain-prototype-proposal.md)) is **insufficient as the overall deliverable**: it can serve as a component test but not as the institutional prototype or a complete gate.

The purpose of the prototype is to force interactions among the system's functions into the open. Build executable mechanisms across the institution and test cross-domain workflows. A failure that reveals a previously unidentified constraint is useful evidence, but an absent subsystem is not an implemented capability.

A previous protocol draft failed Director review for being charter commentary disguised as operational procedure: no serious design alternatives, no meaningful runbook or skill decomposition, no verified execution, inadequate agent/human limitation model, insufficient living state and self-maintenance, and an inappropriate assumption of unlimited LLM context.

## Responsibility model — maintain separate ownership

| Domain | Primary intellectual responsibility | Distinction |
| --- | --- | --- |
| **Governance** | What ought to govern the program; reasons, ideals, authority, institutional design, review, amendment and self-revision | Establishes legitimate standards; does not itself implement every workflow or declare scientific truth |
| **Executive / Coordination** | Transfer of information and context; role dispatch and construction; ownership of cross-domain issues; accountable triage, follow-up and priority interfaces | Responsible for ensuring an issue reaches an owner, not automatically for deciding the issue's scientific or constitutional merits |
| **Operations** | Operational reality and feasible action; infrastructure, persistent state, execution, cost, monitoring, maintenance and progress | Does not acquire the power to amend governing law because an implementation is convenient |
| **Research** | Intellectual reality; problems, unknowns, theories, investigation, candidate methods, evidence and scientific interpretation | Retains initiative to propose directions beyond current executive priorities; hypotheses are not accepted findings |

This is an **intellectual responsibility / ownership architecture**, not four sequential stages or a license for one department to become supreme. Departments must communicate in both directions. Explicitly distinguish domain responsibility, persistent role, current holder, bounded task, authority source, live state and review obligations.

Governance protocols and operations protocols are not one monolithic category. Local skills, tests, discussions, review, protocols, context and maintenance may be repeated **by domain** where meaningfully different. Shared mechanisms need explicit interfaces, not an implicit global manual.

## Hard requirements for the builder's design and implementation

1. **Root-first and recursively navigable.** Every new agent session begins at root. Every folder has a useful, bounded README identifying purpose, contents, status, applicable authority, navigation links, where work belongs, maintenance responsibilities and when to reconsider the organization. Indexes are maintained on create/move/split/merge/archive. Agents load the relevant path selectively, not the entire repository. Indexes point to canonical evidence and must not become unquestioned sources of truth.

2. **Open-ended roles with persistent responsibility.** Roles survive individual LLM/human holders and are not mere finite task prompts. Support definition, interpretation, assignment, discovery of missing duties, specialization, revision, handoff, merger and retirement. Show how inadequate, overlapping and unclaimed roles are detected and surfaced. Do not demand that each agent perform every institutional responsibility.

3. **Executive accountability for cross-domain work.** Shared forums or notices are not enough: provide addressing, discovery, acknowledgment, an unresolved/ownerless state, escalation, and disposition. Avoid both a universal inbox every agent must read and a single dispatcher with unbounded cognitive load. Compare central, hierarchical, federated or mixed routing as warranted.

4. **Real multi-agent cooperation.** Handle overlapping edits, independent competing hypotheses, delegated work, stale information and concurrent readers/writers. Keep operational coordination distinguishable from scientific consensus. A version-control conflict is not the same as a semantic disagreement.

5. **Finite context and human capacity.** Implement cold startup, relevant skill selection, bounded loading, checkpoints, interruption recovery, fresh-instance handoff and concise human decision packets linked to underlying grounds. Do not use unbounded summaries, tacit chat memory, or continuous human attention as prerequisites.

6. **Distinct state semantics.** Separate the *meaning* of authority, epistemic claims, active operational state, deliberation, logs and provenance even if stored in related files. A proposal, comment, status page, peer vote, commit, or agent confidence statement must not silently become ratified law or verified science. Live state should identify current actors/tasks and link to evidence/history; recovery must detect staleness.

7. **Derived authority and propagation.** Article VII of the charter requires that changes in source authority trigger reconciliation of dependent permissions, protocols, role assignments and in-flight work. Test how revoked/narrowed authority affects current tasks. Reasonable interpretation of explicit or codified delegations is allowed; silent self-enlargement is not.

8. **Universal feedback and contradiction.** Every part of the institution, including the charter and this note, must be challengeable. Any agent/human may record objections and proposals contradicting prevailing law. *Right to challenge* is distinct from *power to enact*. Challenges need an accountable review path, persistence of disagreement, and a means of revisiting rejected proposals.

9. **Actual organizational self-maintenance.** Folders, skills, roles, indexes and protocols need procedures for growth, revision, subdivision, consolidation, migration, archiving and dependency checks. Assess when a skill is too abstract, concrete, long, short, separable, duplicative or obsolete; do not substitute arbitrary file/token thresholds for judgment about cohesion, navigability and context costs.

10. **Research cycle exercised without contaminating accepted science.** Implement question/hypothesis/evidence/interpretation/alternatives/disagreement/revision/proposed experiment workflows in the prototype. Use **clearly synthetic** research fixtures while task 1 is open; do not prematurely populate the real accepted knowledge base or proceed through outset tasks 2–5.

11. **Cost and efficiency explicitly measured.** Log token/context exposure, tool calls, human review burden, routing delay, coordination overhead and rework. Compare meaningful alternative designs. The goal is reliable institutional operation, not perfect-looking bureaucracy or the smallest possible toy.

## Verification evidence to demand

A credible prototype audit should inspect the *actual artifacts* and *observed behavior*. Suggested cross-component tests:

- **Cold-entry:** a fresh instance has only the repository and an assignment ID; it identifies applicable authority, active work, relevant local context and required skills.
- **Concurrency:** two agents work on linked documents; detect both accidental write conflict and legitimate competing interpretations without overwriting either.
- **Abrupt context loss:** replace a holder without transferring its chat; recover task, unfinished claims, evidence, objections, responsible roles, permissions and next action.
- **Authority mutation:** change a delegation mid-task; detect the dependent role, skill, approval and in-flight consequences, and reconcile lawfully.
- **Cross-department escalation:** a research issue implicates governance and operations; executive routes to named owners, tracks acknowledgment and notices an unclaimed responsibility.
- **Institutional dissent:** an agent challenges the governing rule itself; the objection persists but does not self-ratify.
- **Structural migration:** split or merge a populated folder and a skill/role; verify indexes, canonical links, provenance, permissions and recoverability.
- **Human review:** give a bounded, source-linked decision packet to a reviewer who has not read the full repository.
- **Epistemic contamination:** verify synthetic, tentative or externally reported claims cannot quietly become approved scientific results.
- **Recovery from maintenance failure:** stale README, broken dependency or unacknowledged notice is detected and handled or explicitly escalated.

For each executed test, capture setup, version/commit, agent inputs, actions, observed outcomes, defects, alternatives, cost, and what remains unproved. **A tabletop example, file existence, or an assistant's claim of successful operation is not execution evidence.**

## Review of the development process itself

- Maintain distinct artifacts for **requirements; competing architectures; reasons for decisions; actual implementation; operational runbooks/skills; test execution evidence; unresolved issues; gate decision**.
- Treat procedure writing as engineering: identify use cases and failures, examine alternatives, specify inputs/outputs/authority/state, test, then revise. Make return to prior stages normal when testing exposes a flawed premise.
- Each major decision should be logged and indexed with an explicit authority and status. The [existing responsibility decision](../decisions/2026-11-14-four-domain-responsibility-model.md) is a *design direction*, not a fully ratified protocol.
- Do not silently replace the original [failed protocol draft](../../protocols/01-foundational-research-governance.md) or promote it to binding status.
- The five chartered outset tasks proceed **separately and in order**. Work currently concerns task 1. Historical ideas may be preserved as **unverified research context**, not incorporated as accepted knowledge by inference from chat memory.
- Directory scaffolding is useful, but only a precursor. Do not present the scaffold as a self-booting operating system.
- Ensure the prototype's **own governance and maintenance** can revise its assumptions when real behavior contradicts them.

## Specific auditor questions to put to Work

1. Where is the authority and current-state entry point used by a totally new instance? Show an actual fresh-entry run.
2. What exactly owns an unassigned interdepartment issue, and how is forgotten work detected?
3. How does a persistent role evolve independently of its holder? Show the recorded before/after state of a role revision.
4. What makes an approval binding as opposed to a note, a vote, or a Git commit?
5. How do authority amendments reach dependent jobs already in progress?
6. How are directory/skill migrations verified, including old inbound links and source provenance?
7. Can an agent preserve a minority objection against constitutional rules without accidentally overriding them?
8. What evidence distinguishes a genuine executed multi-agent test from a narrated simulation?
9. Does the system become more reliable than simpler coordination structures at an acceptable context/human cost?
10. What remains broken, unimplemented, or unverifiable — with links — before the Director is asked to approve Gate 1?

## Auditor posture and coordination boundary

This is an independent audit lane. Do not treat it as an instruction from a co-implementer or as permission to bypass the Research Director's approval and other law. The auditing instance should inspect and report implementation defects, rationale gaps and adverse findings, not silently edit Work's files or certify success from a plausible design. Work may rebut or correct this note; the critique should remain traceable.

**No gate approval is conferred by this document.**
