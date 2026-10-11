# Gekko BacktestTool — A top table is an in-sample ranking

**Decision question:** Does a parameter leaderboard prove that a strategy generalizes?

| Field | Review |
| --- | --- |
| Upstream | [xFFFFF/Gekko-BacktestTool](https://github.com/xFFFFF/Gekko-BacktestTool) |
| Primary area | Backtesting & Simulation |
| Source commit | [8c88d1c572b48a68d7b6353f08efae170d47b852](https://github.com/xFFFFF/Gekko-BacktestTool/commit/8c88d1c572b48a68d7b6353f08efae170d47b852) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/xFFFFF/Gekko-BacktestTool/blob/8c88d1c572b48a68d7b6353f08efae170d47b852/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The analysis groups runs by dataset and sorts top configurations by profit per day from the same tested history. Selecting the top row from the evaluated period spends degrees of freedom; the table is not holdout evidence or a multiple-testing correction. |

## What this project does

A CLI that sweeps Gekko strategies, markets, and parameters and prints ranked backtest tables. [Project README](https://github.com/xFFFFF/Gekko-BacktestTool/blob/8c88d1c572b48a68d7b6353f08efae170d47b852/README.md#L18).

## Mechanism inspected

The analysis groups runs by dataset and sorts top configurations by profit per day from the same tested history. [Implementation](https://github.com/xFFFFF/Gekko-BacktestTool/blob/8c88d1c572b48a68d7b6353f08efae170d47b852/backtest.pl#L211). [Related source 1](https://github.com/xFFFFF/Gekko-BacktestTool/blob/8c88d1c572b48a68d7b6353f08efae170d47b852/sample_output.csv#L1).

## Limitation that matters

Selecting the top row from the evaluated period spends degrees of freedom; the table is not holdout evidence or a multiple-testing correction. This is a source review, not a runtime or security test.

## Practical check for a trading system

Record the complete candidate count and reserve untouched data before discussing a ranked configuration.

## Why this score

A transparent selection-bias counterexample rather than a backtesting engine to reuse.

## Source trail

[README](https://github.com/xFFFFF/Gekko-BacktestTool/blob/8c88d1c572b48a68d7b6353f08efae170d47b852/README.md#L18); [Implementation](https://github.com/xFFFFF/Gekko-BacktestTool/blob/8c88d1c572b48a68d7b6353f08efae170d47b852/backtest.pl#L211); [Related source 1](https://github.com/xFFFFF/Gekko-BacktestTool/blob/8c88d1c572b48a68d7b6353f08efae170d47b852/sample_output.csv#L1) - [License](https://github.com/xFFFFF/Gekko-BacktestTool/blob/8c88d1c572b48a68d7b6353f08efae170d47b852/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
