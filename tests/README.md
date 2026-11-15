# Test suite — code for structural checks
**Parent:** [root](../README.md) · **Status:** prototype.
- [test_institution_audit.py](test_institution_audit.py) verifies local index and link discovery, decision status, issue templates and basic intake field validation.

Run `python3 -m unittest discover -s tests -v`. These are **tool unit tests**, not evidence that agent/human governance interactions pass. The [Operations test index](../operations/tests/README.md) tracks cross-domain scenarios that require real GitHub Issues, PRs and humans/agents.

Maintenance: add regression tests for every validator defect and record unresolved integration limits in the PR.

