# Decision record: four-domain responsibility model

**Record ID:** DR-2026-11-14-01  
**Date:** 2026-11-14  
**Status:** Director-endorsed *design direction*; **not** an adopted operating protocol, delegated role assignment, or charter amendment.  
**Authority/provenance:** Research Director's November 14 discussion of a missing top-level executive/coordination function, following the three-domain model debate.  
**Scope:** Architecture engineering under Article VIII outset task 1 only.  
**Related context:** [design alternatives](../../operations/design/02-architecture-alternatives.md), [requirements](../../operations/design/03-requirements-and-verification.md), [prototype proposal](../../operations/design/06-four-domain-prototype-proposal.md).

## Question and rationale

The three domains (governance, operations, research) account for distinct modes of judgment, but do not by themselves assign responsibility for moving information and context between them, triaging unowned work, and ensuring conflicts do not disappear in a boundary. Assuming every role will handle coordination is not an adequate ownership model. The Research Director therefore proposed **Executive / Coordination** as a fourth top-level responsibility.

This record preserves a design direction and competing concerns; it does not assert that implementation details or effectiveness are established.

## Proposed responsibility domains

| Domain | Primary intellectual responsibility | Owns what in the system |
| --- | --- | --- |
| **Governance** | What ought to govern the program, why, and how principles, authorities, and the system itself may be questioned and revised | Governing-law design, justification, validity and amendment paths, institutional definitions, normative review |
| **Executive / Coordination** | What information, context, assignments and decisions must move across the program, and who must handle an unresolved issue | Cross-domain routing, role construction/dispatch and gap detection, shared situational awareness, priority arbitration within delegated authority, escalation and follow-up |
| **Operations** | What is operationally true, what can be executed, what it costs, how infrastructure functions, and what progress is being made | Agent/human workflow implementation, persistent state and context recovery, maintenance, cost/feasibility evidence, operational auditing and delivery |
| **Research** | What is intellectually supported, what is unknown, what investigations could establish, and how research interpretations progress | Scientific questions, hypotheses, studies, novelty/capability evidence, interpretation, findings, suggested research directions |

These are **responsibilities**, not mutually exclusive subject matters, mandatory folder names, or autonomous rights to change the charter. Each domain may require its own skills, protocols, tests, discussions, local state and maintenance. Cross-domain dependencies are expected.

## Ownership rather than merely universal duties

- Every consequential issue should have a discoverable accountable role or disposition; an item with no clear owner is a responsibility of Executive/Coordination **for triage and assignment**, not automatically for solving its substance.
- Every domain keeps its own authoritative work records. Executive coordinates *transfer and discovery* of context, rather than becoming the sole canonical store of scientific truth, governance law, or implementation state.
- Every actor may question any component, including higher law. Executive is answerable for routing, acknowledgment and tracking of cross-domain objections; the relevant authority decides whether a proposed binding change is adopted.
- Role definitions describe persistent **open-ended responsibilities**. Assignment of human/LLM holders is a distinct, bounded action. Missing roles, conflicting roles and role reinterpretation must themselves have an escalation path.
- Governance controls legal authority and principles; operations evaluates implementation practicality and cost; research controls epistemic examination; executive coordinates priority conflicts and interfaces without being entitled to declare scientific facts or alter constitutional rules.
- Authority changes must trigger reconciliation of downstream delegations and affected working state under Charter Article VII.

## Edge cases that remain design obligations

1. **Research finds a direction outside priorities:** research preserves the scientific argument; executive evaluates cross-project priority and routing; no suppressing dissent.
2. **Operations cannot implement a governance standard:** operations documents failure and options, executive ensures delivery to governance, governance decides normative response.
3. **Two roles assume the other is tracking a contradiction:** executive must have a detectable unowned-work mechanism, not an assumption that posting was sufficient.
4. **A rule is challenged by a subordinate agent:** record and forward objection without pretending it has already amended the rule.
5. **An executive center becomes a bottleneck:** test delegated or hierarchical routing and local autonomy; a responsibility owner need not manually execute every message.

## Alternatives and unresolved questions

- **Three domains with coordination as a universal duty:** smaller top-level taxonomy but no single accountable owner for boundary failures.
- **Four domains with a central executive dispatcher:** explicit ownership, possible overload and single-point-of-failure.
- **Four domains with distributed executive roles:** potentially scalable but requires aggregation, discoverability and responsibility-gap handling.

The four-domain **responsibility split** is the proposed baseline; centralized vs hierarchical vs distributed dispatch remains **unresolved**. Boundaries between executive prioritization and operations planning are provisional and should be tested rather than hidden.

## Decision status and next action

Design direction supported by the Research Director; not proof of robustness and not a binding delegation. Preserve these distinctions in indexes and future implementation. Next authorized work is proposing a small prototype, **not executing it without review**. See [prototype proposal](../../operations/design/06-four-domain-prototype-proposal.md).
