# polymarket-backtest - Is a future-bar fill enough to make a backtest causal?

**Decision question:** Is a future-bar fill enough to make a backtest causal?

| Field | Review |
| --- | --- |
| Upstream | [luuhongyii/polymarket-backtest](https://github.com/luuhongyii/polymarket-backtest) |
| Primary area | Backtesting & Simulation |
| Source commit | [16f3068689e9c5d1ec7cec73c8d32d207543cfab](https://github.com/luuhongyii/polymarket-backtest/commit/16f3068689e9c5d1ec7cec73c8d32d207543cfab) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Rejects duplicate or malformed price rows and fills only after decision time, while using price-panel rather than historical book execution. The latency setting is clamped when too few future observations remain; a strictly later bar still is not a quote-side fill. |

## What this project does

An offline prediction-market strategy harness with as-of context, panel audits, delayed fills and portfolio limits.

## Mechanism inspected

The auditor rejects duplicate token-time rows and missing timestamps or prices. FillModel selects observations strictly later than decision_ts and applies at least one future price step, with optional slippage, fee, cash and short-sale constraints.

## Limitation that matters

A later timestamp avoids same-bar execution, but the inspected fill route uses a price panel rather than historical bid/ask depth. It also clamps a requested latency exceeding the remaining future observations to the last one, so the configured delay is not always achieved.

## Practical check for a trading system

Treat a future-bar price as an execution assumption; reject orders when the required latency horizon is not present, and seek quote-side or book data for fill studies.

## Why this score

3/5 because Direct causal scheduling and basic panel checks are visible, but fill prices and tail-end latency behavior limit execution evidence.

## Source trail

[README research scope](https://github.com/luuhongyii/polymarket-backtest/blob/16f3068689e9c5d1ec7cec73c8d32d207543cfab/README.md#L16); [Panel audit](https://github.com/luuhongyii/polymarket-backtest/blob/16f3068689e9c5d1ec7cec73c8d32d207543cfab/src/polymarket_backtest/audit/lookahead.py#L16); [Future-bar selection](https://github.com/luuhongyii/polymarket-backtest/blob/16f3068689e9c5d1ec7cec73c8d32d207543cfab/src/polymarket_backtest/backtest/execution.py#L41); [As-of context](https://github.com/luuhongyii/polymarket-backtest/blob/16f3068689e9c5d1ec7cec73c8d32d207543cfab/src/polymarket_backtest/backtest/context.py#L31); [License](https://github.com/luuhongyii/polymarket-backtest/blob/16f3068689e9c5d1ec7cec73c8d32d207543cfab/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
