# Skill: audit repository navigation and work
**Status:** prototype.
**Activate:** before PR review, after structural migration, when a fresh agent cannot orient, or on CI failure.
Inputs: branch SHA, root charter/README, relevant paths, GitHub Issues/PRs, actual verifier output.
1. Run `python3 tools/institution_audit.py check .` or consult the corresponding GitHub Actions run. Record branch SHA and output.
2. Walk root -> chosen domain -> child folder; verify each linked resource exists, status is accurate and maintenance obligations are visible.
3. Inspect active Issues, unowned notices and related decisions. Verify document authority with the charter, not a stale index.
4. Check a chosen end-to-end human workflow (browser navigation -> discussion -> receiving role -> explicit acknowledgment).
5. Record defects in an Issue with proof, severity, owner and response; avoid claiming the tool checks semantic authority.
Output: test report with files, failures, uncertainty and next responsible role.
Stop: no GitHub access, ambiguous source of truth, obsolete authority, or missing evidence for claimed automated behavior.

