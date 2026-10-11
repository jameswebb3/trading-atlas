# Strategems.jl — A prior-bar signal still needs an execution model

**Decision question:** Where does this Julia backtest place a trade after a signal?

| Field | Review |
| --- | --- |
| Upstream | [JTAmos/Strategems.jl](https://github.com/JTAmos/Strategems.jl) |
| Primary area | Backtesting & Simulation |
| Source commit | [d7126264c7639a611162f98fcf33f69e464dcb8c](https://github.com/JTAmos/Strategems.jl/commit/d7126264c7639a611162f98fcf33f69e464dcb8c) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/JTAmos/Strategems.jl/blob/d7126264c7639a611162f98fcf33f69e464dcb8c/LICENSE.md)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The loop reads `trades[t-1]`, changes position at bar `t`, and computes PnL from selected trade and close prices. The inspected path shows no fee, slippage, latency or partial-fill mechanism; next-bar indexing alone does not make a faithful live replay. |

## What this project does

Julia strategy and backtesting package with universe, indicators, signals and rules. [README](https://github.com/JTAmos/Strategems.jl/blob/d7126264c7639a611162f98fcf33f69e464dcb8c/README.md).

## Mechanism inspected

The loop reads `trades[t-1]`, changes position at bar `t`, and computes PnL from selected trade and close prices. [Implementation](https://github.com/JTAmos/Strategems.jl/blob/d7126264c7639a611162f98fcf33f69e464dcb8c/src/compute/backtest.jl#L35-L60).

## Limitation that matters

The inspected path shows no fee, slippage, latency or partial-fill mechanism; next-bar indexing alone does not make a faithful live replay. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Pair signal-lag tests with venue-specific fill and cost tests before comparing results with live trading.

## Why this score

The loop reads `trades[t-1]`, changes position at bar `t`, and computes PnL from selected trade and close prices. The inspected path shows no fee, slippage, latency or partial-fill mechanism; next-bar indexing alone does not make a faithful live replay.

## Source trail

[README](https://github.com/JTAmos/Strategems.jl/blob/d7126264c7639a611162f98fcf33f69e464dcb8c/README.md) · [Implementation](https://github.com/JTAmos/Strategems.jl/blob/d7126264c7639a611162f98fcf33f69e464dcb8c/src/compute/backtest.jl#L35-L60) · [License](https://github.com/JTAmos/Strategems.jl/blob/d7126264c7639a611162f98fcf33f69e464dcb8c/LICENSE.md).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
