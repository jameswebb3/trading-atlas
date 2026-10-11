# Quant Trading — Indicator examples are not execution evidence

**Decision question:** What is missing when a signal backtest assumes frictionless fills?

| Field | Review |
| --- | --- |
| Upstream | [je-suis-tm/quant-trading](https://github.com/je-suis-tm/quant-trading) |
| Primary area | Signals & Models |
| Source commit | [611b73f2c3f577ac5b28aaa19ac8c43d3236c7a5](https://github.com/je-suis-tm/quant-trading/commit/611b73f2c3f577ac5b28aaa19ac8c43d3236c7a5) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/je-suis-tm/quant-trading/blob/611b73f2c3f577ac5b28aaa19ac8c43d3236c7a5/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The oscillator example derives position changes from daily close-based moving averages and computes signals inside one historical-data script. The README explicitly assumes no slippage, fees, or illiquidity. |

## What this project does

A collection of educational technical-indicator and quantitative-trading scripts. [Project README](https://github.com/je-suis-tm/quant-trading/blob/611b73f2c3f577ac5b28aaa19ac8c43d3236c7a5/README.md#L19).

## Mechanism inspected

The oscillator example derives position changes from daily close-based moving averages and computes signals inside one historical-data script. [Implementation](https://github.com/je-suis-tm/quant-trading/blob/611b73f2c3f577ac5b28aaa19ac8c43d3236c7a5/Awesome%20Oscillator%20backtest.py#L34). [Related source 1](https://github.com/je-suis-tm/quant-trading/blob/611b73f2c3f577ac5b28aaa19ac8c43d3236c7a5/README.md#L31).

## Limitation that matters

The README explicitly assumes no slippage, fees, or illiquidity. That leaves the main execution questions unresolved for perpetual futures. This is a source review, not a runtime or security test.

## Practical check for a trading system

Use the scripts only to study indicator definitions; require next-available price, fees, and fill rules before comparing any return.

## Why this score

Educational signal code is readable, but its frictionless assumptions make it a poor reference for production trading.

## Source trail

[README](https://github.com/je-suis-tm/quant-trading/blob/611b73f2c3f577ac5b28aaa19ac8c43d3236c7a5/README.md#L19); [Implementation](https://github.com/je-suis-tm/quant-trading/blob/611b73f2c3f577ac5b28aaa19ac8c43d3236c7a5/Awesome%20Oscillator%20backtest.py#L34); [Related source 1](https://github.com/je-suis-tm/quant-trading/blob/611b73f2c3f577ac5b28aaa19ac8c43d3236c7a5/README.md#L31) - [License](https://github.com/je-suis-tm/quant-trading/blob/611b73f2c3f577ac5b28aaa19ac8c43d3236c7a5/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
