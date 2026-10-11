# cmf_backtest - When may a historical maker order be counted as filled?

**Decision question:** When may a historical maker order be counted as filled?

| Field | Review |
| --- | --- |
| Upstream | [mrk-andreev/cmf_backtest](https://github.com/mrk-andreev/cmf_backtest) |
| Primary area | Backtesting & Simulation |
| Source commit | [152716cdea51e58854b71860eb7d8414077617d9](https://github.com/mrk-andreev/cmf_backtest/commit/152716cdea51e58854b71860eb7d8414077617d9) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Requires trade prints to clear estimated queue ahead before crediting a maker fill. Queue-ahead remains an estimate and the implementation can understate later same-level fills. |

## What this project does

A C++ market-replay engine that delays actions and tracks queue-ahead against book snapshots and trade prints.

## Mechanism inspected

A resting order with positive queue_ahead is not filled by a mere LOB cross. Trade prints first consume queue ahead and only their spillover can fill the simulated order; same-tick orders are excluded.

## Limitation that matters

The source explicitly notes a conservative simplification: later orders at the same price do not have their queue_ahead decremented when an earlier simulated order consumes a print. Historical cancellation position is still not observed.

## Practical check for a trading system

Distinguish book crossing, print consumption and queue estimate in fill logs, then vary cancellation assumptions as sensitivity scenarios.

## Why this score

3/5 because Print-gated fills are a useful direct mechanism, with an explicit queue accounting simplification.

## Source trail

[README](https://github.com/mrk-andreev/cmf_backtest/blob/152716cdea51e58854b71860eb7d8414077617d9/README.md#L129); [code/src/engine.hpp](https://github.com/mrk-andreev/cmf_backtest/blob/152716cdea51e58854b71860eb7d8414077617d9/code/src/engine.hpp#L95); [code/src/engine.hpp](https://github.com/mrk-andreev/cmf_backtest/blob/152716cdea51e58854b71860eb7d8414077617d9/code/src/engine.hpp#L103); [code/src/order_book.hpp](https://github.com/mrk-andreev/cmf_backtest/blob/152716cdea51e58854b71860eb7d8414077617d9/code/src/order_book.hpp#L369); [License text](https://github.com/mrk-andreev/cmf_backtest/blob/152716cdea51e58854b71860eb7d8414077617d9/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
