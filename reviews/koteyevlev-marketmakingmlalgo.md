# MarketMakingMLAlgo - Does an order-log market-making replay initialize without future prices?

**Decision question:** Does an order-log market-making replay initialize without future prices?

| Field | Review |
| --- | --- |
| Upstream | [koteyevlev/MarketMakingMLAlgo](https://github.com/koteyevlev/MarketMakingMLAlgo) |
| Primary area | Backtesting & Simulation |
| Source commit | [8225dde96a8efb0f6a9cf0fefa116aee308e96d0](https://github.com/koteyevlev/MarketMakingMLAlgo/commit/8225dde96a8efb0f6a9cf0fefa116aee308e96d0) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and test source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Replays historical orders through a delayed strategy order path. Early replay uses future record prices and may hide data-error exclusions. |

## What this project does

A market-making research project built around historical full order logs and a local matching simulation.

## Mechanism inspected

Its daily loop processes order-log records, waits a configured latency before handing strategy orders to the simulated book, and accounts for simulated fills.

## Limitation that matters

Before the loop it seeds the strategy price from records 1000 to 1002, which are future relative to early records. Broad exception handlers also continue after replay errors or skip days, so the resulting sample can be selected by data failures.

## Practical check for a trading system

Initialize only from elapsed records and publish rejected-event and skipped-day counts beside any PnL.

## Why this score

2/5. The order-log replay is relevant, but future initialization and swallowed errors undercut result credibility.

## Source trail

[README](https://github.com/koteyevlev/MarketMakingMLAlgo/blob/8225dde96a8efb0f6a9cf0fefa116aee308e96d0/README.md#L1); [backtest_py/backtest_period.py](https://github.com/koteyevlev/MarketMakingMLAlgo/blob/8225dde96a8efb0f6a9cf0fefa116aee308e96d0/backtest_py/backtest_period.py#L10); [backtest_py/backtest_period.py](https://github.com/koteyevlev/MarketMakingMLAlgo/blob/8225dde96a8efb0f6a9cf0fefa116aee308e96d0/backtest_py/backtest_period.py#L22); [backtest_py/backtest_period.py](https://github.com/koteyevlev/MarketMakingMLAlgo/blob/8225dde96a8efb0f6a9cf0fefa116aee308e96d0/backtest_py/backtest_period.py#L53); [License text](https://github.com/koteyevlev/MarketMakingMLAlgo/blob/8225dde96a8efb0f6a9cf0fefa116aee308e96d0/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
