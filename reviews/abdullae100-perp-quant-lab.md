# Perp Quant Lab - Can a cross-sectional factor survive a simple held-out cost check?

**Decision question:** Can a cross-sectional factor survive a simple held-out cost check?

| Field | Review |
| --- | --- |
| Upstream | [AbdullaE100/perp-quant-lab](https://github.com/AbdullaE100/perp-quant-lab) |
| Primary area | Signals & Models |
| Source commit | [104dc669084b7f0d0a99748a0f4300950b49930d](https://github.com/AbdullaE100/perp-quant-lab/commit/104dc669084b7f0d0a99748a0f4300950b49930d) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Applies next-day returns and turnover fees to a dollar-neutral factor sweep. Sorting many configurations by the held-out score makes that same holdout part of model selection. |

## What this project does

A compact crypto-perp research script for rank-weighted momentum and short-term reversal sweeps.

## Mechanism inspected

It de-means cross-sectional ranks to dollar-neutral weights, applies next-day returns, subtracts a fixed taker cost proportional to turnover and reports separate first-70-percent versus last-30-percent statistics.

## Limitation that matters

The code sorts all candidate configurations by out-of-sample Sharpe, which turns that holdout into a selection set. A fixed fee omits funding, spread, impact and instrument constraints; no independent event clustering or preregistered winner rule is visible.

## Practical check for a trading system

Treat the script as a baseline cell, reserve a second untouched holdout after any configuration choice and make costs venue-specific.

## Why this score

2/5 because The causal shift and turnover charge are useful, but holdout reuse and incomplete perp costs prevent strong inference.

## Source trail

[README](https://github.com/AbdullaE100/perp-quant-lab/blob/104dc669084b7f0d0a99748a0f4300950b49930d/README.md#L1); [research/backtest.py](https://github.com/AbdullaE100/perp-quant-lab/blob/104dc669084b7f0d0a99748a0f4300950b49930d/research/backtest.py#L14); [research/backtest.py](https://github.com/AbdullaE100/perp-quant-lab/blob/104dc669084b7f0d0a99748a0f4300950b49930d/research/backtest.py#L22); [research/backtest.py](https://github.com/AbdullaE100/perp-quant-lab/blob/104dc669084b7f0d0a99748a0f4300950b49930d/research/backtest.py#L54); [License text](https://github.com/AbdullaE100/perp-quant-lab/blob/104dc669084b7f0d0a99748a0f4300950b49930d/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
