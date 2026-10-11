# Kalshi Orderbook - Does a conflicting snapshot or missing delta invalidate the whole subscription?

**Decision question:** Does a conflicting snapshot or missing delta invalidate the whole subscription?

| Field | Review |
| --- | --- |
| Upstream | [Chenaters/kalshi-orderbook](https://github.com/Chenaters/kalshi-orderbook) |
| Primary area | Market Data & Ingestion |
| Source commit | [c67b69e4eb23cf77e0f5503e8334b3caec7314ed](https://github.com/Chenaters/kalshi-orderbook/commit/c67b69e4eb23cf77e0f5503e8334b3caec7314ed) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The book state rejects conflicting duplicate snapshots, invalid deltas, negative sizes and sequence gaps, invalidating the affected state. A valid aggregate book still does not establish personal queue position or executable maker fills. |

## What this project does

A Kalshi order-book scanner with per-subscription state.

## Mechanism inspected

The book state rejects conflicting duplicate snapshots, invalid deltas, negative sizes and sequence gaps, invalidating the affected state.

## Limitation that matters

A valid aggregate book still does not establish personal queue position or executable maker fills.

## Practical check for a trading system

Treat snapshot and sequence integrity as prerequisites, then model fill uncertainty separately.

## Why this score

3/5. The strict invalidation path is a strong data-state reference with a clear fillability limit.

## Source trail

[README](https://github.com/Chenaters/kalshi-orderbook/blob/c67b69e4eb23cf77e0f5503e8334b3caec7314ed/README.md#L1); [src/kalshi_orderbook/api/websocket.py](https://github.com/Chenaters/kalshi-orderbook/blob/c67b69e4eb23cf77e0f5503e8334b3caec7314ed/src/kalshi_orderbook/api/websocket.py#L240); [src/kalshi_orderbook/api/websocket.py](https://github.com/Chenaters/kalshi-orderbook/blob/c67b69e4eb23cf77e0f5503e8334b3caec7314ed/src/kalshi_orderbook/api/websocket.py#L308).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
