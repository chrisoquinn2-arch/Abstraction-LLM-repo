# Workflows — automation with no independent authority
**Parent:** [GitHub configuration](../README.md) · **Status:** prototype.
- [institution-verify.yml](institution-verify.yml) checks indexes, links and file templates and runs standard-library unit tests on changes.
- [forum-intake.yml](forum-intake.yml) accepts newly added Markdown posts under `forum/dropbox/` on `main` and opens a linked GitHub Issue. The original commit remains the author's provenance. Later conversation lives in the Issue.

**Limits:** Actions need a working GitHub runner and permissions; the author cannot rely on this until the run succeeds. A failed Action must leave a visible submission for Executive to triage. Workflows do not review law, promote evidence, or coordinate AI automatically.

Maintenance: inspect Action logs and least-privilege permissions; treat code changes as reviewable PRs. Record explicit outage/recovery if notifications are delayed.

