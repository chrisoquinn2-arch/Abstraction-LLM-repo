# Optional institution maintenance tools
**Parent:** [root](../README.md) · **Status:** prototype assistive tooling, never canonical authority.

- [institution_audit.py](institution_audit.py): standard-library-only verifier. `python3 tools/institution_audit.py check .` validates local Markdown links, recursive folder READMEs and parent indexes, proposal record status, issue template presence and dropbox post schema. No network or database is needed.
- [Unit tests](../tests/README.md) and [CI](../.github/workflows/institution-verify.yml).

**Human operation does not require these tools.** GitHub's browser UI permits reading/editing files, commenting in Issues and reviewing PRs. Automation may report defects but does not enact law, assign scientific truth, or dismiss objections.

Maintenance: include failure modes and versions, preserve Git history, and compare actual runtime behavior with assumptions. Scripts must not silently create an alternate state store; request review before introducing dependencies.

