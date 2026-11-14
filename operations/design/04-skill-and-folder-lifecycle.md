# Design study — folder, skill, and role lifecycles

**Status:** design hypotheses; no approved maintenance protocol.

## Folder contract (proposed)
Each folder has a README discoverable from its parent and usable within a bounded context. It answers:
1. **Why** does the folder exist, under what scope/authority, and what work belongs here?
2. **What** children exist, why, and how to select them without reading them all?
3. **How** may work, discussions, and proposed changes be placed here?
4. **Where** are canonical sources, local live state, and unresolved issues?
5. **Who/what** maintains it, and what change/maintenance obligations apply?
6. **When** should it be reviewed, split, merged, retired, or escalated?

Folder-specific maintenance requirements belong in the README by default, with shared rules in an indexed maintenance skill once validated. A separate local protocol is warranted only if the folder has genuinely different procedures; duplicating an entire manual in every README would overwhelm context and drift.

## Skill contract (proposed)
Skill discovery entry: name, purpose, activation cues, prerequisites, expected context budget, applicable authority, outputs, stop/escalate cases, and location. Skill body: bounded execution method, handoff contract, checks, and failure recovery. Relevant dependencies are **selected**, not blindly concatenated.

## Design diagnostics
| Symptom | Alternative responses to consider |
| --- | --- |
| Too abstract | add operational examples, a contract, or specialize a subskill; do not always add more rules |
| Too concrete | extract shared capability; keep domain-specific specialization |
| Too long | factor steps/dependencies, index children, improve selective loading |
| Too short | add missing prerequisites, evidence checks, failure handling |
| Needs split | different authority, inputs, outputs, contexts, or maintainers |
| Needs merge | inseparable repeated co-use, duplicate authority or instructions |
| Stale or contradictory | check source authority, reconcile dependencies, revise and test |
| Folder too deep or too broad | rebalance navigation, build cross-links, or consolidate |
| Role too broad | reduce simultaneous responsibilities, delegate, create supporting roles |
| Role gap | create an issue, compare reassignment/new role/temporary ownership |

These are qualitative triggers; arbitrary token or file-count thresholds are not yet defensible.

## Role lifecycle (proposed)
**Define or discover → assign/dispatch → orient → interpret scope → execute/cooperate → receive feedback → revise role or its interpretation → hand off/rotate → retire or specialize when appropriate.**

A role's success condition is open-ended but not unlimited. Its current interpretation, unresolved questions, authority, and performance evidence must be inspectable. Role owners and holders may change while responsibility continues. The original abstract description is preserved; operational specialization must not silently overwrite it.

**Potential core roles to test:** governance consistency, research-initiative maintenance, knowledge/provenance audit, cross-department review, infrastructure maintenance, operational dispatch. These are *illustrations*, not approved positions or a complete list.

## Maintenance lifecycle (proposed)
**Observe problem → register feedback → find affected resources/dependencies → explore alternatives → propose change → obtain proper authority → migrate carefully → check references/state/permissions → assess whether result helped.**

Feedback is permitted even against binding law, but the proposed change remains nonbinding until legally authorized. A human or another agent may open a challenge; the system must retain the objection rather than hide it.

## Critical failure cases
- Directory move breaks references and changes which rules an agent believes apply.
- Generated README summarizes away a counterexample or jurisdiction limit.
- Two skills silently duplicate normative responsibility.
- Agent holding a broad role forgets one responsibility due to context limits.
- Cross-department notice is silently assumed handled because it was posted.
- An agent treats peer votes as approval to supersede a governance rule.

## Work required before drafting a maintenance protocol
A small live prototype of the README/skill index pattern, a migration exercise, a finite-context agent test, and review of alternatives with observed costs.
