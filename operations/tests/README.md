# Institutional verification
[Operations](../README.md) · [Integration scenarios](integration-scenarios.md) · [Forum tests](../../forum/tests/README.md)

**Status:** design scenarios and static checker; **no independent human walkthrough, live multi-agent run, or Gate 1 success is claimed**. Reproducible test evidence must link to exact commit/PR and observable effects.

## Available executable structural verification
Run `python3 tools/check_repository.py` from repository root (Python 3.10+ standard library). The validator checks existence of local Markdown links and every directory's README and parent index. It checks **structure**, not whether law was legitimately amended or a researcher acted intelligently.

## Required integrated exercises
Use [integration-scenarios.md](integration-scenarios.md) to exercise human entry, wrong-domain messages, role reassignment, context loss, authority change, evidence disagreement and index migration with actual GitHub Issues and PRs. Record action links, timings/tool calls, reviewer burden, failed behaviors and alternative explanations. If using a simulation, label it as a simulation.

## Test evidence index
- [Static checker script](../../tools/check_repository.py): source exists; results pending CI or local execution verification.
- [Exercise logs](evidence/README.md): no substantive test result yet.
- [Existing scenarios](../design/01-scenarios.md): design hypotheses, not proof.

**Gate rule:** file scaffolding, descriptions and simulated tests are insufficient to certify an autonomous institution. The Research Director controls the ultimate outset mandate determination.

