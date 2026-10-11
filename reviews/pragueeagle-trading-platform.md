# Trading Platform - Does a completed-bar signal wait until the next executable bar?

**Decision question:** Does a completed-bar signal wait until the next executable bar?

| Field | Review |
| --- | --- |
| Upstream | [PragueEagle/Trading-Platform](https://github.com/PragueEagle/Trading-Platform) |
| Primary area | Backtesting & Simulation |
| Source commit | [e177050eb41b6e5f2b59c19e5a722588d571d45f](https://github.com/PragueEagle/Trading-Platform/commit/e177050eb41b6e5f2b59c19e5a722588d571d45f) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The step function executes signals saved from the previous close against the current bar open, with risk sizing and stop handling in the same step. Bar-open fills with configured slippage do not reproduce order-book depth, queue priority or venue response delays. |

## What this project does

A research-only crypto backtest and risk-engine core.

## Mechanism inspected

The step function executes signals saved from the previous close against the current bar open, with risk sizing and stop handling in the same step.

## Limitation that matters

Bar-open fills with configured slippage do not reproduce order-book depth, queue priority or venue response delays.

## Practical check for a trading system

Keep the one-bar causal boundary and test fills separately against executable book evidence.

## Why this score

3/5. The code makes the signal-to-fill delay explicit, while the fill model remains bar-based.

## Source trail

[README](https://github.com/PragueEagle/Trading-Platform/blob/e177050eb41b6e5f2b59c19e5a722588d571d45f/README.md#L1); [packages/backtest/src/backtest/engine.py](https://github.com/PragueEagle/Trading-Platform/blob/e177050eb41b6e5f2b59c19e5a722588d571d45f/packages/backtest/src/backtest/engine.py#L122); [Root license](https://github.com/PragueEagle/Trading-Platform/blob/e177050eb41b6e5f2b59c19e5a722588d571d45f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
