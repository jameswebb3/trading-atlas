# howtrader - Can outstanding close orders freeze more position than remains?

**Decision question:** Can outstanding close orders freeze more position than remains?

| Field | Review |
| --- | --- |
| Upstream | [51bitquant/howtrader](https://github.com/51bitquant/howtrader) |
| Primary area | Execution & Exchange Integration |
| Source commit | [fcad8e2d86825506b9d33441ab78be853c2c3bdd](https://github.com/51bitquant/howtrader/commit/fcad8e2d86825506b9d33441ab78be853c2c3bdd) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | PositionHolding tracks active orders, trade updates and frozen long/short inventory before converting close/open requests. Exchange-specific close-today semantics do not directly transfer to Hyperliquid perps, and this code is not a restart ledger. |

## What this project does

An event-driven trading framework with position and order conversion for several futures venues.

## Mechanism inspected

PositionHolding tracks active orders, trade updates and frozen long/short inventory before converting close/open requests.

## Limitation that matters

Exchange-specific close-today semantics do not directly transfer to Hyperliquid perps, and this code is not a restart ledger.

## Practical check for a trading system

Separate available, frozen and filled quantities when issuing concurrent reductions, then reconcile venue state after restart.

## Why this score

3/5. The inventory accounting pattern is useful, while the venue rules are different.

## Source trail

[README](https://github.com/51bitquant/howtrader/blob/fcad8e2d86825506b9d33441ab78be853c2c3bdd/README.md#L1); [howtrader/trader/converter.py](https://github.com/51bitquant/howtrader/blob/fcad8e2d86825506b9d33441ab78be853c2c3bdd/howtrader/trader/converter.py#L146); [Root license](https://github.com/51bitquant/howtrader/blob/fcad8e2d86825506b9d33441ab78be853c2c3bdd/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
