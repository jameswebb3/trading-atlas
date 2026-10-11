# Batch Data Pipeline - Can a pipeline publish Silver data after a quality failure?

**Decision question:** Can a pipeline publish Silver data after a quality failure?

| Field | Review |
| --- | --- |
| Upstream | [abeltavares/batch-data-pipeline](https://github.com/abeltavares/batch-data-pipeline) |
| Primary area | Data Quality & Lineage |
| Source commit | [05016db2f6844278e4aa55222194886a003a9168](https://github.com/abeltavares/batch-data-pipeline/commit/05016db2f6844278e4aa55222194886a003a9168) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its quality checker can run configured checks against Silver data, but fail_on_error defaults to false. An enabled check is not a publication gate unless the failure policy stops downstream writes; configuration can also disable checks. |

## What this project does

A batch ETL example using Airflow, DuckDB, Delta Lake and Soda checks.

## Mechanism inspected

Its quality checker can run configured checks against Silver data, but fail_on_error defaults to false.

## Limitation that matters

An enabled check is not a publication gate unless the failure policy stops downstream writes; configuration can also disable checks.

## Practical check for a trading system

Make critical data contracts fail closed and record the exact checks used for each batch.

## Why this score

2/5. The configurable failure boundary is a concrete caution for a research-data pipeline.

## Source trail

[README](https://github.com/abeltavares/batch-data-pipeline/blob/05016db2f6844278e4aa55222194886a003a9168/README.md#L1); [src/processors/quality_checker.py](https://github.com/abeltavares/batch-data-pipeline/blob/05016db2f6844278e4aa55222194886a003a9168/src/processors/quality_checker.py#L23); [src/processors/quality_checker.py](https://github.com/abeltavares/batch-data-pipeline/blob/05016db2f6844278e4aa55222194886a003a9168/src/processors/quality_checker.py#L25); [src/processors/quality_checker.py](https://github.com/abeltavares/batch-data-pipeline/blob/05016db2f6844278e4aa55222194886a003a9168/src/processors/quality_checker.py#L132).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
