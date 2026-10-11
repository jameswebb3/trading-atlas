# Argilla - What if a dataset write and its search-index update disagree?

**Decision question:** What if a dataset write and its search-index update disagree?

| Field | Review |
| --- | --- |
| Upstream | [argilla-io/argilla](https://github.com/argilla-io/argilla) |
| Primary area | Research & Reproducibility |
| Source commit | [eb689f8af0b02b52644d6b7a32b51513b1c784a9](https://github.com/argilla-io/argilla/commit/eb689f8af0b02b52644d6b7a32b51513b1c784a9) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The job fetches record IDs in a database session and updates search status after leaving that transaction, with bounded retries. A crash between stores can leave database state and search status divergent until reconciliation. |

## What this project does

A human-labeling and dataset platform with asynchronous indexing jobs.

## Mechanism inspected

The job fetches record IDs in a database session and updates search status after leaving that transaction, with bounded retries.

## Limitation that matters

A crash between stores can leave database state and search status divergent until reconciliation.

## Practical check for a trading system

Record an index-rebuild cursor and compare authoritative records with derived search state.

## Why this score

2/5. The cross-store handoff exposes a familiar reproducibility risk; retries alone do not close it.

## Source trail

[README](https://github.com/argilla-io/argilla/blob/eb689f8af0b02b52644d6b7a32b51513b1c784a9/README.md#L1); [argilla-server/src/argilla_server/jobs/dataset_jobs.py](https://github.com/argilla-io/argilla/blob/eb689f8af0b02b52644d6b7a32b51513b1c784a9/argilla-server/src/argilla_server/jobs/dataset_jobs.py#L32); [argilla-server/src/argilla_server/jobs/dataset_jobs.py](https://github.com/argilla-io/argilla/blob/eb689f8af0b02b52644d6b7a32b51513b1c784a9/argilla-server/src/argilla_server/jobs/dataset_jobs.py#L53).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
