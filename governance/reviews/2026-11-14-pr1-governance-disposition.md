# Governance audit disposition — Institutional prototype PR #1

**Audit status:** **REJECTED FOR ADOPTION / RETURN FOR REVISION** (auditor disposition; not a charter amendment or Research Director ratification)  
**Audited revision:** `prototype/institution` commit `4694e601a9d908cef4f61b9971a1f9973eeaf7b4`  
**Date:** 2026-11-14 (America/Los_Angeles)  
**Authority:** Director-designated independent audit of the proposed Article VIII outset task 1 institutional prototype. The Research Director retains final constitutional authority and determination of whether the outset mandate has been fulfilled.  
**Evidence basis:** Source and documentation inspection of [PR #1](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/pull/1), [decision](../../governance/decisions/README.md) on the PR branch, and [ratified charter](../../CHARTER.md). No independently observed execution tests were supplied at this revision.

## Issue presented

Does the exercise prototype adequately justify replacing an essentially Git/files-first shared institutional working system with a *local SQLite ledger* as canonical authority and live working state, while preserving human usability, portable agent recovery, traceability of design choice and review, and the constitutional chain of authority?

## Observed design, not inferred motive

The proposed Python CLI stores exercise `roles`, `grants`, `tasks`, `threads`, `resources`, `proposals` and append-only `events` in `.institution/state.sqlite3`, which is excluded from version control. Git retains the charter, READMEs, protocols and code. The CLI supports `boot`, `inbox`, `show`, `history`, `review`, `apply`, `audit` and one-way Markdown snapshot export. Workers are assumed to share one host and live ledger; actors are trusted self-asserted strings in the exercise.

This may be a legitimate *trusted-local exercise* architecture. It is **not** presently demonstrated to satisfy the intended full human+LLM self-booting institution.

## Decision provenance audit

The branch contains [governance/decisions/2026-11-14-institutional-prototype.md](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/blob/4694e601a9d908cef4f61b9971a1f9973eeaf7b4/governance/decisions/2026-11-14-institutional-prototype.md). It chooses “one local transactional ledger and keep source documents and procedures in Git” because related updates should remain transactionally consistent after interruption. It cites Git-only records and a network service as alternatives.

That is **recorded rationale**, but not sufficient evidence that the architectural decision was investigated and authorized. The decision, design, code, and README interface were introduced in the **same implementation commit**. This does not prove there was no prior private reasoning, but the repository lacks a prior comparative record, demonstrated human usage, a tested portability/recovery plan, and a clear approval of the architectural substitution. The Director authorized a committed prototype, **not SQLite specifically**.

Because the database changes the source of truth for authority, role state, ongoing work and discussion, the issue is **governance-significant**, not merely a software implementation detail.

## Blocking findings

1. **G-09: Inadequate architectural provenance.** Record the problem and human/agent operating requirements; compare file-first/Git, SQLite-backed, and hybrid approaches with tradeoffs in access, independence, integrity, complexity, source-of-truth, and maintenance; document actual design selection, dissent, and authority.
2. **G-10: Human interface unverified.** A CLI is a possible human interface, but no complete reviewer workflow is evidenced for discovering current state, examining evidence, challenging a rule, reviewing/applying an authorized amendment, and understanding the result without direct SQL or opaque internal state.
3. **G-11: Portable state/recovery incomplete.** The ignored database is canonical and `boot TASK` requires it. A fresh machine with just Git cannot reconstruct the institution; Markdown export is a derived browse view, not demonstrated lossless roundtrip state. Implement/verify restoration or narrow explicitly the claim and state assumptions and failure behavior.
4. **G-12: Cross-store governance integrity uncertain.** Governing files live in Git while authority/runtime state lives in the database, with no evidenced invariant or migration rule keeping normative amendments, issued grants, stale skills, and dependent instructions synchronized across stores.
5. **G-13: Trust boundaries not sufficient for general institutional use.** Claimed “independent” reviewer identity is a distinct actor string in a trusted local process, not enforcement across untrusted agents. Specify this as an exercise-only boundary and show the path to actual authenticated or isolated reviewers if wider assurance is claimed.

The eight previously submitted source-review findings (G-01–G-08) also remain open absent revision and observed verification. They include immovable single-domain threads, incomplete authority reconciliation, thread appeal/disposition, stale root context, and lack of integration-test records.

## Required next review packet

The building instance may continue exploratory implementation but should not merge or present a gate pass. Submit:

- A dated architecture decision and alternatives record that distinguishes documented facts from conjectures and makes the human/file-first design intent explicit.
- A traceable human walkthrough (starting from the root README) and an independent-agent cold-start/recovery walkthrough with actual observed outputs and cost.
- A stable description of canonical sources of truth, their writable/derived interfaces, synchronization, backup/recovery, authority propagation and responsibility owners.
- Reproducible adverse governance tests and resolutions to the outstanding review findings, with exact tested commit SHA and remaining deficiencies.

**No inference is authorized that SQLite is categorically inappropriate. The disposition rejects its adoption at the current evidentiary and governance standard, not its consideration.**

## Disposition and status propagation

- [PR #1](https://github.com/chrisoquinn2-arch/Abstraction-LLM-repo/pull/1) remains an open draft; audit objections were recorded in the PR review and a subsequent explicit blocking comment.
- GitHub did not allow the connected owner account to submit a native `REQUEST_CHANGES` review on its own PR (422 error). The explicit comment and this record therefore carry the auditor's rejection; this is **not** a GitHub-enforced branch-protection veto.
- Work must respond with corrections, rebuttal, or evidence. The Director retains final gate/charter determination. Source revision `4694e601` is **not approved** by the independent auditor.
