# Operating scenarios and failure discovery

**Status:** tabletop scenarios, not software verification or accepted procedures.
**Scope:** outfitting the program for large, dynamic, multi-agent work under finite human and model attention.

## Scenario A — a new agent joins an ongoing study
**Setup:** Hundreds of files; a task references a subtopic; a finding was revised; another agent works nearby; a protocol has changed.
**Walkthrough:** agent starts at repository root → identifies current scope/authority → descends through READMEs → selects skills → locates task and its evidence → checks active work → performs limited work → records state and leaves handoff.
**Failure injections:** stale local README; search locates obsolete conclusion; stale grant of approval; context window exhausted midway.
**Required outcomes:** locates source-of-truth or reports inability; distinguishes evidence from index; checks current authority; records unverified partial work; can resume without conversational memory.
**Evidence not yet obtained:** independent agent run with constrained context and a fresh task identifier.

## Scenario B — multiple agents discover a previously missing responsibility
**Setup:** A role owner is tasked with maintaining cross-topic consistency. Its duty is abstract; there is no complete checklist. A second agent notices a contradiction affecting three branches.
**Walkthrough:** topic agent files a cross-area notice → recipients or dispatcher discover it → role owner assesses whether the issue is within its mandate → independent reviewers offer interpretations → the appropriate authority approves any binding changes → affected indexes/skills are reconciled.
**Failure injections:** notice has no owner; reviewers share a blind spot; responsibility belongs to no defined role; two roles assume the other is handling it; change contradicts an approved rule.
**Required outcomes:** unresolved notices remain visible and routable; role boundaries may be questioned and revised; disagreement can persist safely; changes do not gain authority through agreement alone; a closure path is identifiable.
**Evidence not yet obtained:** comparison of broadcast, subscription, and coordinator routing under load.

## Scenario C — role revision and authority change while work is active
**Setup:** One agent maintains a living index; another maintains the governance protocol from which that editing permission derives. Permission is narrowed during an active assignment.
**Walkthrough:** amendment recorded → dependency search → outstanding work evaluated for changed authority → impacted role holders notified → in-flight work pauses, adjusts, or seeks fresh authorization → audit record updated.
**Failure injections:** one role holder misses notice; a snapshot appears to confer revoked authority; a folder move breaks dependency references.
**Required outcomes:** dependent authority reconciled, affected task not silently continued, prior lawful actions not retroactively erased.
**Evidence not yet obtained:** deliberate migration rehearsal with conflicting authority versions.

## Scenario D — a human enters without time to read the entire project
**Setup:** Director receives a proposed protocol change and an unresolved objection while several branches have ongoing work.
**Walkthrough:** read bounded decision packet → inspect evidence and alternatives by link → accept, reject, or request more work → decision and consequences propagated.
**Failure injections:** opinion framed as fact; excessive review text; approving proposed document unintentionally approves unrelated changes.
**Required outcomes:** clear decision scope, traceable sources, efficient review, no implied blanket delegation.
**Evidence not yet obtained:** actual human review of realistic packets.

## Scenario E — the system's own organization stops fitting
**Setup:** A folder/skill index grows; an abstract role becomes over-specific; two topics turn out to be overlapping but not equivalent.
**Walkthrough:** maintenance role flags symptoms → alternatives (split, merge, rename, cross-link, retain) assessed → impact on permissions, links, live state, and history mapped → approved migration performed → validation/recovery.
**Failure injections:** references point at old locations; summary loses an unresolved objection; reorganization changes effective authority by accident.
**Required outcomes:** recoverability, provenance, dependency integrity, improved navigation at acceptable maintenance cost.
**Evidence not yet obtained:** navigation and migration tests on synthetic large repositories.

## Scenario F — two-candidate role behavior as a *research hypothesis*, not infrastructure law
A role may propose two competing interpretations or next actions. Other roles may assess them, but peer agreement is not identical to correctness or authority. A designated reviewer may preserve both for later study rather than commit to one. Training/learning on this pattern belongs to later research authorization, **not** to task 1.

## Cross-cutting questions
- What minimum startup data must an agent receive, and what must always be rechecked?
- How are work claims, independent parallel investigations, and emergency pauses distinguished?
- How can feedback on any resource be captured without promoting a suggestion to law?
- What kind of role representation supports unknown responsibilities yet remains accountable?
- At what point is it cheaper for a human to intervene than to add another agent?

Scenarios are design probes. Each must eventually have a reproducible test setup, pass/fail expectations, observed run, and documented revisions.
