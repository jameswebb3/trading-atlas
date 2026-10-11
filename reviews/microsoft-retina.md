# Retina - Can a capture pipeline expose how many observations it dropped?

**Decision question:** Can a capture pipeline expose how many observations it dropped?

| Field | Review |
| --- | --- |
| Upstream | [microsoft/retina](https://github.com/microsoft/retina) |
| Primary area | Operations & Observability |
| Source commit | [0ab3742b058d1d2c9a28ccf4248e862c6c44ff52](https://github.com/microsoft/retina/commit/0ab3742b058d1d2c9a28ccf4248e862c6c44ff52) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its metric definitions include a lost-events counter keyed by event type and reason. This file declares the metric but does not prove that every eBPF loss path increments it or that market-data gaps are covered. |

## What this project does

A network telemetry platform with control-plane and packet metrics.

## Mechanism inspected

Its metric definitions include a lost-events counter keyed by event type and reason.

## Limitation that matters

This file declares the metric but does not prove that every eBPF loss path increments it or that market-data gaps are covered.

## Practical check for a trading system

Expose drop counts at each collector boundary and verify increments on every overflow path.

## Why this score

2/5. The metric shape is useful; the inspected source is not a coverage proof.

## Source trail

[README](https://github.com/microsoft/retina/blob/0ab3742b058d1d2c9a28ccf4248e862c6c44ff52/README.md#L1); [pkg/metrics/metrics.go](https://github.com/microsoft/retina/blob/0ab3742b058d1d2c9a28ccf4248e862c6c44ff52/pkg/metrics/metrics.go#L126); [pkg/metrics/metrics.go](https://github.com/microsoft/retina/blob/0ab3742b058d1d2c9a28ccf4248e862c6c44ff52/pkg/metrics/metrics.go#L136); [Root license](https://github.com/microsoft/retina/blob/0ab3742b058d1d2c9a28ccf4248e862c6c44ff52/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
