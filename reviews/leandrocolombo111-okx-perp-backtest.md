# OKX Perp Backtest - What should a backtest do when historical funding is unavailable?

**Decision question:** What should a backtest do when historical funding is unavailable?

| Field | Review |
| --- | --- |
| Upstream | [LeandroColombo111/okx-perp-backtest](https://github.com/LeandroColombo111/okx-perp-backtest) |
| Primary area | Backtesting & Simulation |
| Source commit | [fabe026791397a8e18f4a56182c490edaf9ba033](https://github.com/LeandroColombo111/okx-perp-backtest/commit/fabe026791397a8e18f4a56182c490edaf9ba033) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation, and relevant test source inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Raises on unavailable funding and preserves indicator warmup outside each scored walk-forward window. Funding zero is an explicit scenario, not a silent substitute for missing history. |

## What this project does

An OKX perpetuals backtester that separates funding, liquidation, fees and slippage, with walk-forward research tests.

## Mechanism inspected

The data loader raises when requested funding predates the provider's retention instead of filling historical gaps with zero. The execution step settles funding before liquidation and strategy actions. A regression test covers slow-indicator warmup without moving the scored test window.

## Limitation that matters

The venue is OKX, not Hyperliquid, and its bar-level liquidation and slippage assumptions still need venue-specific validation. This review did not replicate reported strategy results.

## Practical check for a trading system

Fail closed on missing funding or explicitly label a zero-funding scenario; warm indicators from pretest history without leaking scored outcomes.

## Why this score

4/5 because Several consequential cost and timing safeguards are visible in implementation and tests, with clear venue and bar-fidelity boundaries.

## Source trail

[README](https://github.com/LeandroColombo111/okx-perp-backtest/blob/fabe026791397a8e18f4a56182c490edaf9ba033/README.md#L1); [src/okx_perp_backtest/okx_data.py](https://github.com/LeandroColombo111/okx-perp-backtest/blob/fabe026791397a8e18f4a56182c490edaf9ba033/src/okx_perp_backtest/okx_data.py#L11); [src/okx_perp_backtest/execution.py](https://github.com/LeandroColombo111/okx-perp-backtest/blob/fabe026791397a8e18f4a56182c490edaf9ba033/src/okx_perp_backtest/execution.py#L50); [tests/test_walkforward.py](https://github.com/LeandroColombo111/okx-perp-backtest/blob/fabe026791397a8e18f4a56182c490edaf9ba033/tests/test_walkforward.py#L31); [License text](https://github.com/LeandroColombo111/okx-perp-backtest/blob/fabe026791397a8e18f4a56182c490edaf9ba033/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
