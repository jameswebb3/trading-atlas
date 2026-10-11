# crypto-database - Can a periodic quote snapshot support causal trading research?

**Decision question:** Can a periodic quote snapshot support causal trading research?

| Field | Review |
| --- | --- |
| Upstream | [ivopetiz/crypto-database](https://github.com/ivopetiz/crypto-database) |
| Primary area | Market Data & Ingestion |
| Source commit | [289742619baa9c6038d528e2daae28d3991e5825](https://github.com/ivopetiz/crypto-database/commit/289742619baa9c6038d528e2daae28d3991e5825) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The loop pulls 24-hour exchange summaries and stamps quote points with local time when they are written. The path does not preserve venue event time, sequence or missing-interval evidence, and several source venues are historical. |

## What this project does

An older multi-exchange quote collector writing points to InfluxDB.

## Mechanism inspected

The loop pulls 24-hour exchange summaries and stamps quote points with local time when they are written.

## Limitation that matters

The path does not preserve venue event time, sequence or missing-interval evidence, and several source venues are historical.

## Practical check for a trading system

Do not use local-write-time aggregate quotes as event-time order-book evidence.

## Why this score

1/5. It illustrates a common ingestion trap but offers little current trading-system reference value.

## Source trail

[README](https://github.com/ivopetiz/crypto-database/blob/289742619baa9c6038d528e2daae28d3991e5825/README.md#L1); [markets/main.go](https://github.com/ivopetiz/crypto-database/blob/289742619baa9c6038d528e2daae28d3991e5825/markets/main.go#L89); [Root license](https://github.com/ivopetiz/crypto-database/blob/289742619baa9c6038d528e2daae28d3991e5825/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
