# Tick Stock Panel - Does the configured fill occur after the signal is knowable?

**Decision question:** Does the configured fill occur after the signal is knowable?

| Field | Review |
| --- | --- |
| Upstream | [shy3130/tick-stock-panel](https://github.com/shy3130/tick-stock-panel) |
| Primary area | Backtesting & Simulation |
| Source commit | [469fd3157c65e9b5e7780e559081b2521a35160e](https://github.com/shy3130/tick-stock-panel/commit/469fd3157c65e9b5e7780e559081b2521a35160e) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The backtest builds a MatcherConfig with separate entry and exit fill modes, fees, taxes, slippage and position limits. The inspected configuration sets entry_fill to close_t. If an entry signal uses that same close, a causal delay must be enforced elsewhere; this path alone does not prove it. |

## What this project does

A self-hosted A-share research workbench with a strategy backtest service.

## Mechanism inspected

The backtest builds a MatcherConfig with separate entry and exit fill modes, fees, taxes, slippage and position limits.

## Limitation that matters

The inspected configuration sets entry_fill to close_t. If an entry signal uses that same close, a causal delay must be enforced elsewhere; this path alone does not prove it.

## Practical check for a trading system

Trace each signal timestamp into the matching engine and reject same-close fills when the close was an input.

## Why this score

3/5. The cost and fill controls are useful, but the decision clock needs independent verification.

## Source trail

[README](https://github.com/shy3130/tick-stock-panel/blob/469fd3157c65e9b5e7780e559081b2521a35160e/README.md#L1); [backend/app/backtest/strategy.py](https://github.com/shy3130/tick-stock-panel/blob/469fd3157c65e9b5e7780e559081b2521a35160e/backend/app/backtest/strategy.py#L1908); [backend/app/backtest/strategy.py](https://github.com/shy3130/tick-stock-panel/blob/469fd3157c65e9b5e7780e559081b2521a35160e/backend/app/backtest/strategy.py#L1910); [backend/app/backtest/strategy.py](https://github.com/shy3130/tick-stock-panel/blob/469fd3157c65e9b5e7780e559081b2521a35160e/backend/app/backtest/strategy.py#L1915).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
