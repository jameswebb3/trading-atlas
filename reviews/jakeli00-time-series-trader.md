# Time Series Trader - When should a WebSocket market view fall back to a fresh REST book?

**Decision question:** When should a WebSocket market view fall back to a fresh REST book?

| Field | Review |
| --- | --- |
| Upstream | [jakeli00/time-series-trader](https://github.com/jakeli00/time-series-trader) |
| Primary area | Market Data & Ingestion |
| Source commit | [41d4c1be19ff41734f93c9900b29476d2f4d9d41](https://github.com/jakeli00/time-series-trader/commit/41d4c1be19ff41734f93c9900b29476d2f4d9d41) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The hybrid loop forces a REST book refresh on stale WS state, invalid book, a sequence-gap reason or near contract close, and records the fallback reason. REST refresh can itself be rate-limited or fail; the shown loop records that condition but cannot make the missing interval tradable. |

## What this project does

A Kalshi time-series trading experiment with hybrid market data.

## Mechanism inspected

The hybrid loop forces a REST book refresh on stale WS state, invalid book, a sequence-gap reason or near contract close, and records the fallback reason.

## Limitation that matters

REST refresh can itself be rate-limited or fail; the shown loop records that condition but cannot make the missing interval tradable.

## Practical check for a trading system

Keep fallback reason and feed invalidity visible until a complete snapshot is accepted.

## Why this score

3/5. The explicit stale/gap fallback is a useful exchange-data recovery reference.

## Source trail

[README](https://github.com/jakeli00/time-series-trader/blob/41d4c1be19ff41734f93c9900b29476d2f4d9d41/README.md#L1); [kalshi_live_execution.py](https://github.com/jakeli00/time-series-trader/blob/41d4c1be19ff41734f93c9900b29476d2f4d9d41/kalshi_live_execution.py#L563); [kalshi_live_execution.py](https://github.com/jakeli00/time-series-trader/blob/41d4c1be19ff41734f93c9900b29476d2f4d9d41/kalshi_live_execution.py#L605).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
