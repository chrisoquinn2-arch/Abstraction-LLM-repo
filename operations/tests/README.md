# Institution verification — executable checks and integration cases
**Parent:** [operations](../README.md) · **Status:** mixed: structural tests executable; live multi-actor exercises not yet certified.

## Run locally (optional)
`python3 tools/institution_audit.py check .`
`python3 -m unittest discover -s tests -v`

Or inspect the [GitHub Actions CI](../../.github/workflows/institution-verify.yml) on a PR. The verifier checks local Markdown links, README presence/index relationships, role/decision required fields, and issue template completeness. It is **not** evidence of human usability, lawful authority or scientific correctness.

## Adversarial exercises to record in PR/Issue evidence
1. Fresh human with GitHub browser: find department, open thread, edit a file, inspect decision history.
2. Fresh agent using only repo + task Issue: locate scope, read objections and leave an effective handoff.
3. Human submits wrong-domain Markdown post; executive identifies multiple affected roles and tracks acknowledgement.
4. Contest a closed discussion; prove new challenge remains visible rather than being discarded.
5. Two authors edit the same file; PR conflict, independent contributions and resolution preserve both grounds.
6. Revise a governance delegation mid-task; enumerate dependent files, roles and active work and block obsolete permission.
7. Move a nested folder; repair parent links and old references; verifier reports missing links before correction.
8. Research exercise: propose experiment, distinguish evidence from interpretation, retain rejected alternative.
9. Role holder disappears; new person/agent resumes solely through GitHub. Observe elapsed time and missed context.
10. Stress: many issues and limited agent context; assess triage backlog, human attention and costs.

Record exact Git revision, setup, actors, stimuli, evidence, outputs, defects and limitations. A successfully authored test document is not a successfully observed test. Human intervention and browser access must be recorded explicitly.

