# Bitquant — A bar loop is not a fill model

**Decision question:** Can a backtest report trades when its broker leaves matching unfinished?

| Field | Review |
| --- | --- |
| Upstream | [51bitquant/bitquant](https://github.com/51bitquant/bitquant) |
| Primary area | Signals & Models |
| Source commit | [a19e703238a7d4c06240a0aa3d31699ad8a7e68f](https://github.com/51bitquant/bitquant/commit/a19e703238a7d4c06240a0aa3d31699ad8a7e68f) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/51bitquant/bitquant/blob/a19e703238a7d4c06240a0aa3d31699ad8a7e68f/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The broker loops over bars and calls its order checker before giving the new bar to the strategy. The matching and trade-accounting methods inspected are unfinished, so ordering in the loop cannot establish execution realism or reliable PnL. |

## What this project does

A collection of teaching code and examples for crypto trading. [Project README](https://github.com/51bitquant/bitquant/blob/a19e703238a7d4c06240a0aa3d31699ad8a7e68f/README.md#L1).

## Mechanism inspected

The broker loops over bars and calls its order checker before giving the new bar to the strategy. [Implementation](https://github.com/51bitquant/bitquant/blob/a19e703238a7d4c06240a0aa3d31699ad8a7e68f/backtest/backtester/broker.py#L130). [Backtest documentation](https://github.com/51bitquant/bitquant/blob/a19e703238a7d4c06240a0aa3d31699ad8a7e68f/backtest/%E5%9B%9E%E6%B5%8B%E6%A1%86%E6%9E%B6%E8%AF%B4%E6%98%8E.md#L2).

## Limitation that matters

The matching and trade-accounting methods inspected are unfinished, so ordering in the loop cannot establish execution realism or reliable PnL. This is a source review, not a runtime or security test.

## Practical check for a trading system

Audit matching, partial fills, fees, and trade accounting before trusting a backtest result.

## Why this score

Useful as a negative test case: the visible bar loop has no complete execution mechanism to reuse.

## Source trail

[README](https://github.com/51bitquant/bitquant/blob/a19e703238a7d4c06240a0aa3d31699ad8a7e68f/README.md#L1); [Implementation](https://github.com/51bitquant/bitquant/blob/a19e703238a7d4c06240a0aa3d31699ad8a7e68f/backtest/backtester/broker.py#L130); [Backtest documentation](https://github.com/51bitquant/bitquant/blob/a19e703238a7d4c06240a0aa3d31699ad8a7e68f/backtest/%E5%9B%9E%E6%B5%8B%E6%A1%86%E6%9E%B6%E8%AF%B4%E6%98%8E.md#L2) - [License](https://github.com/51bitquant/bitquant/blob/a19e703238a7d4c06240a0aa3d31699ad8a7e68f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
