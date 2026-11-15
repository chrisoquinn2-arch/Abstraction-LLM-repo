# Prototype proposal P0 — Four-domain responsibility and handoff test

**Date:** 2026-11-14  
**Status:** Proposed for Research Director review; **not authorized for implementation or execution**.  
**Stage:** Charter Article VIII, outset task 1 only. Synthetic operating-system exercise; **not scientific research**.  
**Design basis:** [four-domain decision record](../../governance/decisions/2026-11-14-four-domain-responsibility-model.md), [scenario analyses](01-scenarios.md), [requirements](03-requirements-and-verification.md).

## Governing question

Can a finite-context agent/human system use recursive README-based navigation, persistent bounded roles, shared work state and explicit executive coordination to recognize, route, challenge and recover a cross-domain issue *without* silently changing authority, promoting unsupported evidence, or losing ownership?

This prototype should make weaknesses observable, not merely illustrate a preferred procedure.

## Smallest useful artifact set (to be built only after approval)

Use a synthetic, isolated working fixture (branch or directory, not the authoritative research knowledge base). Include:
- A root README / entry contract and a minimal index for four responsibility areas.
- One **role card** per domain: open-ended objective, scope/authority source, current interpretation, current holder, issues and handoff pointers.
- A shared **work/issue register**: ID, origin, type, owner or 'unassigned', status, impact, links, next action; an executive routing view.
- A compact **handoff/status file** for a task, with evidence links and unverified items.
- A **discussion/objection record** that can challenge a rule without changing it.
- An **event/decision trail** separating actor actions from approvals and source evidence.

No final schemas, persistent role dispatcher, agent runtime, or research database are presumed by this proposal.

## Synthetic scenario

A fictional research topic contains an evaluation claim, a source record that contradicts its summary, and an assignment to inspect the claim. Another simulated worker has an overlapping edit. In the middle of the exercise, the authority for approving this type of conclusion changes, and a nested README becomes stale. A researcher then raises a cross-domain objection to the evaluation rule.

All claims/sources are **fabricated test fixtures**. Nothing enters the real scientific knowledge base.

## Execution sequence to test

1. **Cold entry:** A fresh agent receives only the repository URL, task ID, and bounded role assignment. It starts at root, discovers the proper branch of work, applicable status and current authority, and does not read the entire repository.
2. **Research inspection:** It identifies the claim/source discrepancy, records evidence and uncertainty, and requests appropriate review rather than accepting a convenient summary.
3. **Operations response:** An operations role identifies the broken index and edit collision, proposes an implementation remedy and records the cost/impact.
4. **Executive routing:** The executive role discovers the cross-domain notice, names a responsible recipient for each issue, tracks acknowledgment and escalates the unowned or conflicted case. Routing does not constitute scientific acceptance or rule change.
5. **Governance review:** A governance role receives the objection and changed authority, distinguishes a proposed amendment from operative law, and identifies dependent permissions requiring reconciliation. Only an appropriate authorized reviewer could ratify any binding change.
6. **Context-loss injection:** Stop a role holder without a handoff conversation. A different agent restarts from root using only the task ID and persistent artifacts; test whether it reconstructs current state, remaining issues, authority and provenance.
7. **Closure review:** Produce a bounded human decision packet listing what happened, what is supported, what remains open, what changed, what needs approval, and linked primary records.

These steps are a test *script*, not adopted work instructions.

## Candidate baselines and alternatives

- **Baseline B0:** Single README + shared task ledger + human dispatcher, without separate persistent role state; tests whether four domains add benefit relative to minimal shared coordination.
- **Candidate P0:** Four persistent role cards + executive-owned issue routing + hierarchical READMEs.
- **Alternative P1:** Same four roles but peer-to-peer notices, without a central dispatcher; compare unnoticed issues, context burden and handoff complexity.

All should use the same synthetic problem and failure injections. Do not presume P0 is superior.

## Provisional acceptance observations

Collect actual evidence rather than claiming a pass from document existence:
- Can a fresh agent identify current authority, task owner, applicable local materials and outstanding issues without access to prior conversations?
- Does every cross-domain issue receive a named owner or explicitly visible unassigned status?
- Is an objection to a rule recorded and routed while the original rule remains in force until lawfully changed?
- Are an obsolete summary, stale index and conflicting edit discovered and corrected or explicitly reported?
- Can a second, context-reset instance reconstruct uncertainty, provenance, authority changes and next steps?
- Can a human reviewer understand the proposed decision and inspect underlying records without exhaustive reading?
- Record missed messages, unauthorized acts, mistaken truth claims, tool calls, context length and human review burden.

Missing results, discovered defects and unresolved objections are outputs, not reasons to silently declare success. Verify whether any benefit justifies the extra overhead over B0.

## Risks and stopping rules

- Do not write actual research findings or grant real approval powers in the synthetic fixture.
- If authority/status cannot be recovered, pause the simulated dependent action and log the failure.
- If a test agent invents a state or permission, record the defect; do not repair it silently to preserve apparent success.
- If the exercise requires context or coordination beyond the intended budget, treat the overload as a failure to study.
- Any subsequent changes to production folders, binding governance, or actual program protocols require separately appropriate authorization.

## Work requested from Research Director

Approve, revise, or reject **the test design only**. After approval, prepare the minimal isolated fixture and run a first comparison (B0 vs P0), then report observations and design implications. A deeper peer-to-peer comparison (P1) can follow if warranted.

**Open choices:** whether to run multiple fresh model instances or simulate handoffs manually for the first pass; what context/tool budgets to impose; and whether routing is centralized only in the first prototype or also compared with a peer-based method immediately.
