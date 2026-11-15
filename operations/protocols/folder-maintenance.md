# Recursive directory and file maintenance
**Status:** prototype process; subject to independent review.

Each folder README is the bounded orientation contract: **purpose and authority, children and why each matters, canonical resources, current state/limits, maintenance and feedback path**. The parent README must link every child folder; an optional machine checker verifies presence and local link resolution.

## Operations
1. Add a file: select the correct local folder, set status/authority/provenance, update its README if meaningful; preserve its relation to work Issues.
2. Add a folder: add its README *in the same PR*, link it in parent, name accountable maintenance and context. No empty unindexed folders.
3. Move/split/merge: propose purpose and alternative layouts, search inbound links and running tasks, record a migration map from old path to new, retain old navigational redirects where feasible, update indexes and linked Issues; run verifier.
4. Retire: preserve provenance, version history, replacement and dissent; do not silently delete an objection.
5. Revise README: compare to actual files and active PRs, not merely spelling or link syntax. Detect institutional contradictions (e.g., “no executive folder” after creation) during human review.
6. If a local skill becomes too broad or too short, assess activation cues, authority, failure/stop behavior and actual reader burden before split/merge.

## Escalation
A folder's classification and this protocol are themselves open to challenge. Changes of binding effect require governance review. An ignored validator warning or stale context must become a visible Issue, not a silent exception.

