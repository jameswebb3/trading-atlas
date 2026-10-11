# Uptrace - What should an anomaly detector do with missing samples?

**Decision question:** What should an anomaly detector do with missing samples?

| Field | Review |
| --- | --- |
| Upstream | [uptrace/uptrace](https://github.com/uptrace/uptrace) |
| Primary area | Operations & Observability |
| Source commit | [1e622fff165391a26bbebc135e4c4f8a843ef1bd](https://github.com/uptrace/uptrace/commit/1e622fff165391a26bbebc135e4c4f8a843ef1bd) |
| Reviewed | 2026-10-11 |
| Declared license | AGPL-3.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The alarm requires a minimum sample count, counts holes and requires every latest-window point to be anomalous. It converts NaN values to zero in place, which may bias the baseline or the anomaly decision. |

## What this project does

An observability system with MAD-based alarm evaluation.

## Mechanism inspected

The alarm requires a minimum sample count, counts holes and requires every latest-window point to be anomalous.

## Limitation that matters

It converts NaN values to zero in place, which may bias the baseline or the anomaly decision.

## Practical check for a trading system

Keep missingness as a first-class state and validate sample sufficiency before evaluating alerts.

## Why this score

2/5. The explicit sample gate is valuable; zero-filling makes the detector unsafe as a direct market-data template.

## Source trail

[README](https://github.com/uptrace/uptrace/blob/1e622fff165391a26bbebc135e4c4f8a843ef1bd/README.md#L1); [pkg/madalarm/alarm.go](https://github.com/uptrace/uptrace/blob/1e622fff165391a26bbebc135e4c4f8a843ef1bd/pkg/madalarm/alarm.go#L59); [pkg/madalarm/alarm.go](https://github.com/uptrace/uptrace/blob/1e622fff165391a26bbebc135e4c4f8a843ef1bd/pkg/madalarm/alarm.go#L97).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
