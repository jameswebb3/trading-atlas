# LOB Engine - How does a passive fill change when earlier queue volume consumes the trade?

**Decision question:** How does a passive fill change when earlier queue volume consumes the trade?

| Field | Review |
| --- | --- |
| Upstream | [bhedavivan/lob-engine](https://github.com/bhedavivan/lob-engine) |
| Primary area | Backtesting & Simulation |
| Source commit | [bab3fbd645e48cc814244f166ccb84abc8b6b8a0](https://github.com/bhedavivan/lob-engine/commit/bab3fbd645e48cc814244f166ccb84abc8b6b8a0) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The maker replay initializes queue-ahead size from displayed depth and fills only after observed trade quantity eats that queue. Cancellations ahead do not advance estimated position, making this conservative but not a reconstruction of actual order priority. |

## What this project does

A C++ LOB and Python market-making replay stack.

## Mechanism inspected

The maker replay initializes queue-ahead size from displayed depth and fills only after observed trade quantity eats that queue.

## Limitation that matters

Cancellations ahead do not advance estimated position, making this conservative but not a reconstruction of actual order priority.

## Practical check for a trading system

Show inventory P&L apart from captured spread and stress queue-ahead assumptions.

## Why this score

3/5. A useful explicit maker-fill assumption with its unobservability disclosed.

## Source trail

[README](https://github.com/bhedavivan/lob-engine/blob/bab3fbd645e48cc814244f166ccb84abc8b6b8a0/README.md#L1); [backtest/market_maker.py](https://github.com/bhedavivan/lob-engine/blob/bab3fbd645e48cc814244f166ccb84abc8b6b8a0/backtest/market_maker.py#L111); [Root license](https://github.com/bhedavivan/lob-engine/blob/bab3fbd645e48cc814244f166ccb84abc8b6b8a0/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
