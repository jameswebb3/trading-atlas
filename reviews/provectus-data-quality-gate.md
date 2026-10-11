# Data Quality Gate — Publish the validation result, not just the report

**Decision question:** Can a pipeline look successful after a failed validation suite?

| Field | Review |
| --- | --- |
| Upstream | [provectus/data-quality-gate](https://github.com/provectus/data-quality-gate) |
| Primary area | Data Quality & Lineage |
| Source commit | [5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66](https://github.com/provectus/data-quality-gate/commit/5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/provectus/data-quality-gate/blob/5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The suite runner checks results.success, but the inspected path uses that flag to build documentation and does not propagate it as a failing job result. A generated report or validation identifier does not prove that expectations passed. |

## What this project does

An AWS/Terraform data-quality stack using Great Expectations, profiling, and reports. [Project README](https://github.com/provectus/data-quality-gate/blob/5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66/README.md#L3).

## Mechanism inspected

The suite runner checks results.success, but the inspected path uses that flag to build documentation and does not propagate it as a failing job result. [Implementation](https://github.com/provectus/data-quality-gate/blob/5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66/functions/data_test/data_test/data_test.py#L71). [Related source 1](https://github.com/provectus/data-quality-gate/blob/5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66/functions/data_test/README.md#L1). [Related source 2](https://github.com/provectus/data-quality-gate/blob/5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66/functions/data_test/data_test/suite_run.py#L22).

## Limitation that matters

A generated report or validation identifier does not prove that expectations passed. The serverless stack adds substantial maintenance for a small data gate. This is a source review, not a runtime or security test.

## Practical check for a trading system

Make the failed expectation count and final gate status mandatory outputs of every validation job.

## Why this score

The source shows a concrete false-green integration hazard, while the deployment stack offers little additional trading value.

## Source trail

[README](https://github.com/provectus/data-quality-gate/blob/5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66/README.md#L3); [Implementation](https://github.com/provectus/data-quality-gate/blob/5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66/functions/data_test/data_test/data_test.py#L71); [Related source 1](https://github.com/provectus/data-quality-gate/blob/5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66/functions/data_test/README.md#L1); [Related source 2](https://github.com/provectus/data-quality-gate/blob/5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66/functions/data_test/data_test/suite_run.py#L22) - [License](https://github.com/provectus/data-quality-gate/blob/5ca3ed0b90bbd9375182eab85d9ebb63cbf6be66/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
