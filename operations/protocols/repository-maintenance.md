# Repository and skill lifecycle — executable prototype procedure
**Status:** draft; source authority is the charter and any valid scope-specific delegation. **Maintainer:** Operations role, with Executive coordination if other domains affected.

## Create
1. Enter from root and choose the owner domain. Search existing directories, roles, skills and Issues for overlap.
2. State a new resource's reason, scope, expected users, status (draft/approved/archived/unknown) and source authority.
3. Create the file and, for every new directory, a README with parent link, children, owner, participation route, current state, maintenance and reopening condition.
4. Update the immediate parent's index, cross-domain links, relevant role skill indexes and tracked dependent work. Never assume an index is canonical evidence.
5. Open a PR linked to the need/issue. Run repository checker, inspect semantic authority and review required by effect.

## Revise / split / merge
1. Record what changed in meaning, behavior, authority, and discovery route (not only lines). List inbound references and active issues.
2. Propose options: local edit, reorganization, subdivision, generalization, consolidation, archive. Compare context load, retrieval, maintainability and review cost; no arbitrary universal file-size threshold substitutes for cohesion.
3. Preserve a discoverable old path (redirect or archival pointer) when feasible. Keep source provenance, dissent, revisions, and current work links.
4. Update child/parent indexes and local skill selectors. Test root-to-target navigation, broken-link checks and cold recovery from an old URL.
5. If a rule changes, submit to Governance for approval and reconcile derived authority before changing active work. A moved folder does not gain new authority.

## Skill lifecycle
A skill has: name, purpose/trigger, required context, scoped authority, inputs, steps, outputs, failure paths, dependencies, review owner, and version/status. An agent selects **one relevant skill at a time** via local index; do not load all procedure files. Collect usage failures and split/merge when evidence warrants.

## Retirement
Link successor, preserved history, open work handoff, reason, who authorized, and external links that cannot be repaired. An empty directory's disappearance must not remove its domain from root navigation without review.

## Recovery and failure
If link checks fail, raise an Issue with exact path and reproduction. If authority or epistemic status is ambiguous, block the consequential action and request review. Keep human-readable primary files usable even if optional validation scripts are missing.

