# Data Drift — No sample is a distinct monitoring state

**Decision question:** Can an empty metric history be mistaken for a quiet system?

| Field | Review |
| --- | --- |
| Upstream | [data-drift/data-drift](https://github.com/data-drift/data-drift) |
| Primary area | Data Quality & Lineage |
| Source commit | [a582ff6d1e7b132d337e28df0de7e69ce1ad0d87](https://github.com/data-drift/data-drift/commit/a582ff6d1e7b132d337e28df0de7e69ce1ad0d87) |
| Reviewed | 2026-10-10 |
| Declared license | GPL-3.0 ([source](https://github.com/data-drift/data-drift/blob/a582ff6d1e7b132d337e28df0de7e69ce1ad0d87/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its history reducer sorts metric samples by commit and turns nonzero changes into events. A period without samples can return an empty result shape rather than an explicit missing-data status. |

## What this project does

A metrics-by-commit platform with history, alerts, and visual diagnostics. [Project README](https://github.com/data-drift/data-drift/blob/a582ff6d1e7b132d337e28df0de7e69ce1ad0d87/README.md#L49).

## Mechanism inspected

Its history reducer sorts metric samples by commit and turns nonzero changes into events. [Implementation](https://github.com/data-drift/data-drift/blob/a582ff6d1e7b132d337e28df0de7e69ce1ad0d87/backend/reducers/metric_history.go#L40). [Related source 1](https://github.com/data-drift/data-drift/blob/a582ff6d1e7b132d337e28df0de7e69ce1ad0d87/backend/README.md#L1). [Related source 2](https://github.com/data-drift/data-drift/blob/a582ff6d1e7b132d337e28df0de7e69ce1ad0d87/backend/reducers/sort_filter_events.go#L17).

## Limitation that matters

A period without samples can return an empty result shape rather than an explicit missing-data status. That makes absence easy to confuse with stability. This is a source review, not a runtime or security test.

## Practical check for a trading system

Track expected cadence and emit Missing or Unknown before interpreting an empty metric history as no drift.

## Why this score

A specific missing-sample lesson, while the Redis/UI platform is too broad for a trading data gate.

## Source trail

[README](https://github.com/data-drift/data-drift/blob/a582ff6d1e7b132d337e28df0de7e69ce1ad0d87/README.md#L49); [Implementation](https://github.com/data-drift/data-drift/blob/a582ff6d1e7b132d337e28df0de7e69ce1ad0d87/backend/reducers/metric_history.go#L40); [Related source 1](https://github.com/data-drift/data-drift/blob/a582ff6d1e7b132d337e28df0de7e69ce1ad0d87/backend/README.md#L1); [Related source 2](https://github.com/data-drift/data-drift/blob/a582ff6d1e7b132d337e28df0de7e69ce1ad0d87/backend/reducers/sort_filter_events.go#L17) - [License](https://github.com/data-drift/data-drift/blob/a582ff6d1e7b132d337e28df0de7e69ce1ad0d87/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
