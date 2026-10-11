# kalshi-data-collector - Can a checkpoint hide a temporarily empty event?

**Decision question:** Can a checkpoint hide a temporarily empty event?

| Field | Review |
| --- | --- |
| Upstream | [harrodyuan/kalshi-data-collector](https://github.com/harrodyuan/kalshi-data-collector) |
| Primary area | Market Data & Ingestion |
| Source commit | [e6b52c4bef9461d536bb7eded5b27a222140c1f2](https://github.com/harrodyuan/kalshi-data-collector/commit/e6b52c4bef9461d536bb7eded5b27a222140c1f2) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It pages events with nested markets and saves processed event IDs locally. An event with no markets in the current sweep is marked processed, so later data can be skipped; checkpoint writes are direct. |

## What this project does

A Kalshi open-market collector with paginated event sweeps and per-event JSON files.

## Mechanism inspected

It pages events with nested markets and saves processed event IDs locally.

## Limitation that matters

An event with no markets in the current sweep is marked processed, so later data can be skipped; checkpoint writes are direct.

## Practical check for a trading system

Record verified completeness separately from an empty response and retry uncertain events.

## Why this score

2/5. Pagination is practical, but checkpoint semantics can create silent gaps.

## Source trail

[README](https://github.com/harrodyuan/kalshi-data-collector/blob/e6b52c4bef9461d536bb7eded5b27a222140c1f2/README.md#L1); [open_market_collector.py](https://github.com/harrodyuan/kalshi-data-collector/blob/e6b52c4bef9461d536bb7eded5b27a222140c1f2/open_market_collector.py#L97); [open_market_collector.py](https://github.com/harrodyuan/kalshi-data-collector/blob/e6b52c4bef9461d536bb7eded5b27a222140c1f2/open_market_collector.py#L96).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
