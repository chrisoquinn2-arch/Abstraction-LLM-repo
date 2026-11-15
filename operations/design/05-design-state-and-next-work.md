# Operating architecture — live design state

**Status:** provisional status for architecture engineering; **not** approved program-wide operational state.  
**Last recorded:** 2026-11-14  
**Authority:** [ratified charter](../../CHARTER.md), outset item 1 only.

## What has been established
- The director ratified Charter v0.3.1, including reconciliation of derivative permissions when superior authority changes.
- The earlier [foundational protocol draft](../../protocols/01-foundational-research-governance.md) failed review. It remains an unapproved sketch, not operational law.
- The director authorized a design-first approach to outset task 1 and requires the five outset items to proceed separately in order.
- Design inputs: root-first agent startup; README/context/maintenance expectations for each folder; recursive directory and skill systems; persistent open-ended roles; role dispatch/construction/revision; cross-department communication; a feedback/revision route for *every* component, including challenges to higher-order law.

## New provisional design direction (2026-11-14)

The director identified a missing top-level **Executive / Coordination** responsibility accountable for routing information, context, cross-domain issues, role gaps, and dispatch. See the [four-domain responsibility record](../../governance/decisions/2026-11-14-four-domain-responsibility-model.md). Governance, executive/coordination, operations and research are distinct cooperating intellectual responsibilities; this design is **not yet an approved operating system**.

A concrete [four-domain prototype P0](06-four-domain-prototype-proposal.md) has been proposed for director review. It has not been implemented or tested. Its baseline comparison and context-loss/authority-change injections are intended to test whether the responsibility model actually improves robustness relative to a simpler arrangement.

## What has *not* been established
No architecture has been selected, no protocol has been validated or adopted, no role dispatcher has been implemented, and no scientific research knowledge has been admitted. Tabletop scenarios are not empirical evidence.

## Active design branches
1. **Agent and human startup/recovery:** minimum bounded root contract, task IDs, how to find authority and local context.
2. **Directory and skill maintenance:** recursive index contract, consolidation, stale summary checks, migration.
3. **Roles and cooperation:** role identity vs holder, dispatch, open-ended interpretation, delegation, multiple agents.
4. **Discussion and feedback:** cross-department notice routing; dissent against law; auditable escalation.
5. **Authority and verification:** dependent permissions, protocol promotion, independently reviewable evidence.

## Open decisions
- Is role-dispatch centralized, hierarchical, or federated?
- Are cross-department notices routed by subscriptions, dispatcher, periodic scan, or combination?
- What minimal persistent fields support recovery without excessive writing?
- What parts of README and maintenance can be shared versus local?
- Which validation can be automated, and what requires human judgment?
- How should governance protect authority while ensuring complaints against the rules themselves are heard?

## Suggested next work within outset item 1
1. Review this design set and identify missing operational cases; revise assumptions first.
2. Construct a *small, separate sandbox or mock repository*, not a full production hierarchy, for root-to-leaf navigation and single-agent restart.
3. Add concurrent agents and a deliberately underspecified maintenance role; observe cooperation and uncovered duties.
4. Introduce a changed delegation, a disputed cross-department notice, and a folder migration; test recovery and escalation.
5. Compare outcomes, failure rates, total context/tool cost, and human review burden against simpler alternatives.
6. Only then write and review bounded executable skills/protocols, consolidate the verification record, and request an outset item 1 gate decision.

The list is a proposal for design work, not authorization to start scientific research or subsequent outset items.

## Record maintenance
On a material design change, update this file *and* the appropriate primary design document. Keep this short enough for handoff, link to evidence, and preserve disagreements rather than silently resolving them. If it becomes long, move detailed branches into indexed subfolders and retain only navigation and current decisions.
