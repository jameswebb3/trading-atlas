# KalshiMarketMaker - Can a maker worker stop while resting orders remain live?

**Decision question:** Can a maker worker stop while resting orders remain live?

| Field | Review |
| --- | --- |
| Upstream | [rodlaf/KalshiMarketMaker](https://github.com/rodlaf/KalshiMarketMaker) |
| Primary area | Execution & Exchange Integration |
| Source commit | [af660af885d20c089c37901e1110c38dc4c12e01](https://github.com/rodlaf/KalshiMarketMaker/commit/af660af885d20c089c37901e1110c38dc4c12e01) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Shutdown first waits for the worker to stop, then repeatedly reads and cancels resting orders and checks for a remaining order set. If the worker cannot stop by timeout, cleanup is deferred and live orders can remain; the return value must be acted upon. |

## What this project does

A Kalshi market maker with quote logic and explicit worker shutdown cleanup.

## Mechanism inspected

Shutdown first waits for the worker to stop, then repeatedly reads and cancels resting orders and checks for a remaining order set.

## Limitation that matters

If the worker cannot stop by timeout, cleanup is deferred and live orders can remain; the return value must be acted upon.

## Practical check for a trading system

Treat timeout or incomplete cancellation as a visible unresolved exposure, with independent account reconciliation.

## Why this score

3/5. The lifecycle ordering is useful; the unresolved-order state cannot be interpreted as flat.

## Source trail

[README](https://github.com/rodlaf/KalshiMarketMaker/blob/af660af885d20c089c37901e1110c38dc4c12e01/README.md#L1); [kalshi_market_maker/runtime/cleanup.py](https://github.com/rodlaf/KalshiMarketMaker/blob/af660af885d20c089c37901e1110c38dc4c12e01/kalshi_market_maker/runtime/cleanup.py#L59); [Root license](https://github.com/rodlaf/KalshiMarketMaker/blob/af660af885d20c089c37901e1110c38dc4c12e01/LICENSE.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
