# Architecture alternatives — working comparison

**Status:** options under design, not selected protocols.  
**Rule:** do not present a preferred option as a demonstrated capability.

## 1. Startup and recursive navigation
**Candidate A: entire program summary upfront.** Easy single entry, but brittle and exceeds context with growth.
**Candidate B: root-first recursive README contracts.** Bounded local loading; risks missed cross-branch dependencies and stale summaries.
**Candidate C: B + explicit cross-links / search / active-work discovery.** Better cross-area coverage, adds index maintenance and consistency work.
**Working lean:** C, because the director requires root-first entry and every folder to have a README. No proof it scales yet.

In all candidates, a README is an *orientation contract*, not inherently scientific evidence or current authorization. It should name why the folder exists, what its children contain, why an agent enters, where to work, relevant authority and maintenance expectations. A stale README must be detectable and correctable.

## 2. Persistent roles versus agent instances
**Candidate A: only task prompts.** Cheap, but responsibility disappears with the session and dispatch remains manual.
**Candidate B: persistent role definitions with individual assignments.** Supports continuity and delegation; requires role state, owner/holder distinction, and revision controls.
**Candidate C: B + role discovery/dispatch/review.** Can surface uncovered responsibilities and rebalance work, but dispatch can become a bottleneck or create uncontrolled hierarchy.
**Working lean:** study B and C. The director's role concept is an *ongoing responsibility with an open-ended success condition*, not a fixed finite checklist. A role may be created, revised, specialized, merged, or retired. An agent instance may temporarily hold one or more roles only within a feasible context budget. Role interpretation is accountable and revisable; it does not allow changing the charter by self-interpretation.

Separate: (i) **identity/role** = continuing responsibility and interpretation; (ii) **holder** = executing human/agent instance; (iii) **assignment** = bounded work under authority; (iv) **role state** = progress, unresolved matters, dependencies; (v) **dispatch** = choosing holder and context.

## 3. Cross-department communication
**A: broadcast everything.** High discoverability, severe attention overload.
**B: per-folder discussions only.** Locally cheap, misses consequences elsewhere.
**C: interdepartment notices with routing, subscriptions, and triage.** Promising compromise, but routing can itself miss unknown dependencies.
**D: periodic role review/aggregation.** May catch neglected notices, with latency and cost.

A notice should distinguish *information*, *request*, *objection*, *proposed change*, and *urgent authorization conflict*. Its lifecycle needs discoverability, review/acknowledgment, and closure without requiring every agent to read every thread. Agents may post across areas without demanding consensus or pretending a discussion is an adopted finding.

## 4. Feedback on everything versus binding authority
**A: unrestricted edits to rules.** Fast, destroys authority integrity.
**B: only director can question rules.** Safe from casual edits, blocks discovery and scaling.
**C: universal right to flag, discuss, and propose changes; change of governing effect follows established authority and review.** Supports contradiction and improvement without informal repeal.
**Working lean:** C. Distinguish objection from amendment, amendment from ratification, and temporary safety pause from power to revoke law.

The charter already requires reconciliation of dependent authority when it changes. No repository status note or peer vote can bypass that.

## 5. Work/state persistence
**A: conversation memory.** Insufficient across instances and limited context.
**B: only event log.** Reconstructable but heavy to read.
**C: only current state file.** Fast, risks history loss.
**D: current snapshots + append-only significant events + links to underlying evidence.** Likely manageable, with stale-snapshot detection needed.

State includes separate semantic layers: authority, knowledge, active work, historical actions, and deliberations. They may share storage but should not silently inherit one another's evidentiary status.

## 6. Directory organization and maintenance
**A: rigid global taxonomy.** Easy early, poorly adapted to unknowns.
**B: unrestricted organic folders.** Flexible, increasingly unnavigable.
**C: recursive local indexes, local context/maintenance contracts, and periodic consolidation.** Preserves extensibility at recurring maintenance cost.

Maintenance decisions may include leave alone, link, split, merge, specialize, generalize, migrate, archive. They should account for authority, citations, in-flight work, and links—not only count files.

## Unresolved design tensions
1. How much skill/role maintenance overhead is acceptable relative to actual research?
2. Which role or mechanism can detect a missing role, when detection is itself an unknown-unknown problem?
3. How can a notice reach relevant departments whose relevance was not anticipated?
4. What is a safe and inexpensive way to discover stale indexes?
5. What must be immutable, and what should remain easily revised?
6. Does a single role-dispatch center scale, or should routing be hierarchical and eventually distributed?
7. What does a human need to review to authorize a high-impact change without reading all related files?
