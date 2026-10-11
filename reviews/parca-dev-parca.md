# Parca - Does a failed scrape leave a target looking healthy?

**Decision question:** Does a failed scrape leave a target looking healthy?

| Field | Review |
| --- | --- |
| Upstream | [parca-dev/parca](https://github.com/parca-dev/parca) |
| Primary area | Operations & Observability |
| Source commit | [dc0b442da64404254fc6dce3915857951e3af29d](https://github.com/parca-dev/parca/commit/dc0b442da64404254fc6dce3915857951e3af29d) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The scrape loop records failed processing as bad target health plus a last error and duration. This health marker concerns profiler collection; it does not establish market-data completeness. |

## What this project does

A continuous profiling system with scheduled target scrapes.

## Mechanism inspected

The scrape loop records failed processing as bad target health plus a last error and duration.

## Limitation that matters

This health marker concerns profiler collection; it does not establish market-data completeness.

## Practical check for a trading system

Surface failed collector cycles as unhealthy with last-error evidence before downstream use.

## Why this score

2/5. The failure-state pattern is useful for collectors but requires trading-specific coverage checks.

## Source trail

[README](https://github.com/parca-dev/parca/blob/dc0b442da64404254fc6dce3915857951e3af29d/README.md#L1); [pkg/scrape/scrape.go](https://github.com/parca-dev/parca/blob/dc0b442da64404254fc6dce3915857951e3af29d/pkg/scrape/scrape.go#L527); [pkg/scrape/scrape.go](https://github.com/parca-dev/parca/blob/dc0b442da64404254fc6dce3915857951e3af29d/pkg/scrape/scrape.go#L557).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
