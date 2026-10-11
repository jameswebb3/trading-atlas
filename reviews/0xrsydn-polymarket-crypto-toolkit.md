# Polymarket Crypto Toolkit - Does a crypto prediction-market backtest use actual contract prices?

**Decision question:** Does a crypto prediction-market backtest use actual contract prices?

| Field | Review |
| --- | --- |
| Upstream | [0xrsydn/polymarket-crypto-toolkit](https://github.com/0xrsydn/polymarket-crypto-toolkit) |
| Primary area | Backtesting & Simulation |
| Source commit | [63d805b879c0e13eaac223e1a1806149ed900f69](https://github.com/0xrsydn/polymarket-crypto-toolkit/commit/63d805b879c0e13eaac223e1a1806149ed900f69) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 3/3: README, relevant implementation and test source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Turns next-candle direction into a fixed-price binary payoff backtest. Fixed contract prices and a missing last outcome prevent an executable PnL claim. |

## What this project does

A modular Polymarket toolkit with data feeds, an execution layer and a candle-based backtest.

## Mechanism inspected

The backtest turns next-candle direction into a binary outcome, applies fixed buy price and payout, and sorts parameter sweeps by the resulting win rate and PnL.

## Limitation that matters

The code does not use as-of Polymarket order prices, fees, depth or resolution rules. The last next_close is missing but its boolean comparison yields a non-null false outcome, so a terminal signal can be scored as a loss. The parameter sweep ranks on the same sample. No root license was verified.

## Practical check for a trading system

Keep the outcome clock, contract quote, fees and final-row exclusion explicit before treating a candle classifier as trading evidence.

## Why this score

1/5. The public code provides a precise example of optimistic market-price abstraction and terminal-row mis-scoring.

## Source trail

[README](https://github.com/0xrsydn/polymarket-crypto-toolkit/blob/63d805b879c0e13eaac223e1a1806149ed900f69/README.md#L15); [packages/backtest/src/polymarket_algo/backtest/engine.py](https://github.com/0xrsydn/polymarket-crypto-toolkit/blob/63d805b879c0e13eaac223e1a1806149ed900f69/packages/backtest/src/polymarket_algo/backtest/engine.py#L44); [packages/backtest/src/polymarket_algo/backtest/engine.py](https://github.com/0xrsydn/polymarket-crypto-toolkit/blob/63d805b879c0e13eaac223e1a1806149ed900f69/packages/backtest/src/polymarket_algo/backtest/engine.py#L61); [packages/backtest/src/polymarket_algo/backtest/engine.py](https://github.com/0xrsydn/polymarket-crypto-toolkit/blob/63d805b879c0e13eaac223e1a1806149ed900f69/packages/backtest/src/polymarket_algo/backtest/engine.py#L108).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
