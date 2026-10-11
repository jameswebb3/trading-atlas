# Boz Weather Trader - Does a prediction-market backtest count missing decision snapshots and fees?

**Decision question:** Does a prediction-market backtest count missing decision snapshots and fees?

| Field | Review |
| --- | --- |
| Upstream | [aclarkson2013/boz-weather-trader](https://github.com/aclarkson2013/boz-weather-trader) |
| Primary area | Backtesting & Simulation |
| Source commit | [136cc13219df7bc3fd5fa614025b16d0ed76e2d0](https://github.com/aclarkson2013/boz-weather-trader/commit/136cc13219df7bc3fd5fa614025b16d0ed76e2d0) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 3/3: README, relevant implementation and test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Reports missing snapshots and simulates fee-aware bounded taker fills. A decision-time quote is not proof that its full size was executable. |

## What this project does

A Kalshi weather trading bot with archived decision-time snapshots and a day-by-day backtest.

## Mechanism inspected

The backtest excludes missing markets and non-tiling brackets, scores market probabilities separately, and fills only orders whose quote plus Kalshi-style fee fits the remaining budget.

## Limitation that matters

Its fill function grants the entire affordable count at the snapshot quote plus configurable slippage. It does not model displayed depth, order-arrival delay or cancellations. No root license text was verified.

## Practical check for a trading system

Keep exclusion counts and fee-budget mechanics, but add order-arrival book and fill uncertainty before promoting a strategy.

## Why this score

3/5. The data-exclusion and fee-budget paths are directly relevant, with a clear fill-model ceiling.

## Source trail

[README](https://github.com/aclarkson2013/boz-weather-trader/blob/136cc13219df7bc3fd5fa614025b16d0ed76e2d0/README.md#L5); [backend/backtesting/real_engine.py](https://github.com/aclarkson2013/boz-weather-trader/blob/136cc13219df7bc3fd5fa614025b16d0ed76e2d0/backend/backtesting/real_engine.py#L70); [backend/backtesting/real_engine.py](https://github.com/aclarkson2013/boz-weather-trader/blob/136cc13219df7bc3fd5fa614025b16d0ed76e2d0/backend/backtesting/real_engine.py#L99); [backend/strategy/fills.py](https://github.com/aclarkson2013/boz-weather-trader/blob/136cc13219df7bc3fd5fa614025b16d0ed76e2d0/backend/strategy/fills.py#L45).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
