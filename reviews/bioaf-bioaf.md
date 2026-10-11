# bioAF - Revoke queued work when an input fails integrity

**Decision question:** What happens to a queued computation when its input checksum later fails?

| Field | Review |
| --- | --- |
| Upstream | [bioAF/bioAF](https://github.com/bioAF/bioAF) |
| Primary area | Data Quality & Lineage |
| Source commit | [ff1c81a2e1568bf3c4749c4ebccf9d7b5636da58](https://github.com/bioAF/bioAF/commit/ff1c81a2e1568bf3c4749c4ebccf9d7b5636da58) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/bioAF/bioAF/blob/ff1c81a2e1568bf3c4749c4ebccf9d7b5636da58/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | An automatic run is queued only after a sample-completeness check. A later checksum mismatch cancels waiting runs; the launch loop also disables automatic runs and cancels pending work after the configured spending threshold is reached. The inspected idempotency check is a read before insert and does not itself prove race-free uniqueness across workers. Biomedical sample completeness and spend are not market-data availability or trading risk limits. |

## What this project does

bioAF manages biomedical samples, pipelines and automatic analysis runs. [README](https://github.com/bioAF/bioAF/blob/ff1c81a2e1568bf3c4749c4ebccf9d7b5636da58/README.md).

## Mechanism inspected

An automatic run is queued only after a sample-completeness check. A later checksum mismatch cancels waiting runs; the launch loop also disables automatic runs and cancels pending work after the configured spending threshold is reached. [Implementation](https://github.com/bioAF/bioAF/blob/ff1c81a2e1568bf3c4749c4ebccf9d7b5636da58/backend/app/services/auto_run_service.py#L163-L243). [Related path](https://github.com/bioAF/bioAF/blob/ff1c81a2e1568bf3c4749c4ebccf9d7b5636da58/backend/app/services/auto_run_service.py#L246-L324).

## Limitation that matters

The inspected idempotency check is a read before insert and does not itself prove race-free uniqueness across workers. Biomedical sample completeness and spend are not market-data availability or trading risk limits. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

For delayed market-data partitions, record a validation state before queuing research and revoke queued work if the source is later rejected or backfill changes its integrity verdict.

## Why this score

The explicit reversal path is useful when data quality changes after scheduling, but the domain and concurrency assumptions need adaptation.

## Source trail

[README](https://github.com/bioAF/bioAF/blob/ff1c81a2e1568bf3c4749c4ebccf9d7b5636da58/README.md) - [Implementation](https://github.com/bioAF/bioAF/blob/ff1c81a2e1568bf3c4749c4ebccf9d7b5636da58/backend/app/services/auto_run_service.py#L163-L243) - [Related path](https://github.com/bioAF/bioAF/blob/ff1c81a2e1568bf3c4749c4ebccf9d7b5636da58/backend/app/services/auto_run_service.py#L246-L324) - [License](https://github.com/bioAF/bioAF/blob/ff1c81a2e1568bf3c4749c4ebccf9d7b5636da58/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
