# airflow-provider-great-expectations — Running a validation definition does not itself enforce its result

**Decision question:** Does a pipeline stop when a data expectation fails?

| Field | Review |
| --- | --- |
| Upstream | [fivetran/airflow-provider-great-expectations](https://github.com/fivetran/airflow-provider-great-expectations) |
| Primary area | Data Quality & Lineage |
| Source commit | [706fec92274ad6ccd39fef7019d6e39ffafe68db](https://github.com/fivetran/airflow-provider-great-expectations/commit/706fec92274ad6ccd39fef7019d6e39ffafe68db) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/fivetran/airflow-provider-great-expectations/blob/706fec92274ad6ccd39fef7019d6e39ffafe68db/LICENSE.txt)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | run_validation_definition adds or updates a suite and batch definition, runs it with chosen result detail and returns the validation result. This helper returns the result but does not itself fail the task when success=false; the caller must impose the gate. |

## What this project does

Airflow provider that executes Great Expectations validation definitions. [README](https://github.com/fivetran/airflow-provider-great-expectations/blob/706fec92274ad6ccd39fef7019d6e39ffafe68db/README.md).

## Mechanism inspected

run_validation_definition adds or updates a suite and batch definition, runs it with chosen result detail and returns the validation result. [Implementation](https://github.com/fivetran/airflow-provider-great-expectations/blob/706fec92274ad6ccd39fef7019d6e39ffafe68db/great_expectations_provider/common/gx_context_actions.py#L19-L51).

## Limitation that matters

This helper returns the result but does not itself fail the task when success=false; the caller must impose the gate. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

For source-data contracts, assert the validation outcome and preserve failed-batch IDs before downstream features are materialized.

## Why this score

run_validation_definition adds or updates a suite and batch definition, runs it with chosen result detail and returns the validation result. This helper returns the result but does not itself fail the task when success=false; the caller must impose the gate.

## Source trail

[README](https://github.com/fivetran/airflow-provider-great-expectations/blob/706fec92274ad6ccd39fef7019d6e39ffafe68db/README.md) · [Implementation](https://github.com/fivetran/airflow-provider-great-expectations/blob/706fec92274ad6ccd39fef7019d6e39ffafe68db/great_expectations_provider/common/gx_context_actions.py#L19-L51) · [License](https://github.com/fivetran/airflow-provider-great-expectations/blob/706fec92274ad6ccd39fef7019d6e39ffafe68db/LICENSE.txt).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
