# Institutional exercise runtime

Start with the [root index](../../README.md) and [governing contract](../../governance/protocols/README.md). Use Python 3.10 or later with built-in SQLite and Git. Work from the checkout root.

```sh
python3 -m operations.institution --help
python3 -m operations.institution init --exercise --director director --reviewer founding-reviewer
python3 -m operations.institution --actor director inbox governance
python3 -m operations.institution audit
```

These commands create and examine an isolated ledger at `.institution/state.sqlite3`. Use `--db /path/to/exercise.sqlite3` **before** a command to select another ledger. The explicit founding reviewer identity carries only the ability to review governance changes inside that ledger. The real institutional approval request lives in [Governance reviews](../../governance/reviews/2026-11-14-institutional-prototype-review-request.md).

From the repository and a task ID, run `boot TASK`. Read the root, domain index and role guides it identifies. Inspect individual resource and discussion IDs when relevant. The command surfaces a previous checkpoint, the lease status, stale inputs and recent event identifiers. It leaves any new lease to `claim`.

Shared workers on the same machine can use distinct registered actors and the same ledger. For a new local process, use `--actor ACTOR worker --seconds 900 ROLE -- EXECUTABLE ARG...`. The runner leases one eligible task and supplies a JSON packet on stdin. A worker uses the packet's actor, ledger path, task and lease to checkpoint and finish, block, or release via the CLI. An unfinished worker exit returns work to the queue when the current lease still belongs to that process. Hard interruption leaves a lease eligible for takeover at expiry. Credential and filesystem access are controlled by the local host. The runner's input format and test procedure are being verified on this branch.

Maintenance starts with `check-index` for Git links and `audit` for live record reconciliation. Record defects in the [forum](../../forum/README.md). Start authority changes from [Governance](../../governance/README.md). Code is under independent review on this branch.
