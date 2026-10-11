# mimir - Continuously write and read a known series

**Decision question:** Can a data service be green while its read path loses recent writes?

| Field | Review |
| --- | --- |
| Upstream | [grafana/mimir](https://github.com/grafana/mimir) |
| Primary area | Operations & Observability |
| Source commit | [86811cf62aeb074e7ab1d8d8e4517dc76b657da2](https://github.com/grafana/mimir/commit/86811cf62aeb074e7ab1d8d8e4517dc76b657da2) |
| Reviewed | 2026-10-10 |
| Declared license | AGPL ([source](https://github.com/grafana/mimir/blob/86811cf62aeb074e7ab1d8d8e4517dc76b657da2/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The test recovers a recent written range after restart, writes known generated samples, then checks range and instant queries through normal and fan-out read paths. A synthetic series probes infrastructure health, not the correctness or completeness of real market feeds; it needs a separate source-data gate. |

## What this project does

A metrics store runs continuous synthetic tests against its own write and query APIs. [README](https://github.com/grafana/mimir/blob/86811cf62aeb074e7ab1d8d8e4517dc76b657da2/README.md).

## Mechanism inspected

The test recovers a recent written range after restart, writes known generated samples, then checks range and instant queries through normal and fan-out read paths. [Implementation](https://github.com/grafana/mimir/blob/86811cf62aeb074e7ab1d8d8e4517dc76b657da2/pkg/continuoustest/write_read_series.go#L116-L205).

## Limitation that matters

A synthetic series probes infrastructure health, not the correctness or completeness of real market feeds; it needs a separate source-data gate. This conclusion is limited to the inspected path at the pinned commit.

## Practical check for a trading system

Use a small sentinel market-data partition with known values and verify write, query, restart recovery and gap detection end to end.

## Why this score

The test recovers a recent written range after restart, writes known generated samples, then checks range and instant queries through normal and fan-out read paths. A synthetic series probes infrastructure health, not the correctness or completeness of real market feeds; it needs a separate source-data gate.

## Source trail

[README](https://github.com/grafana/mimir/blob/86811cf62aeb074e7ab1d8d8e4517dc76b657da2/README.md) - [Implementation](https://github.com/grafana/mimir/blob/86811cf62aeb074e7ab1d8d8e4517dc76b657da2/pkg/continuoustest/write_read_series.go#L116-L205) - [License](https://github.com/grafana/mimir/blob/86811cf62aeb074e7ab1d8d8e4517dc76b657da2/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
