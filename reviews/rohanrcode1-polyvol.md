# polyvol - Does short-horizon mean reversion survive executable prices and fees?

**Decision question:** Does short-horizon mean reversion survive executable prices and fees?

| Field | Review |
| --- | --- |
| Upstream | [rohanrcode1/polyvol](https://github.com/rohanrcode1/polyvol) |
| Primary area | Signals & Models |
| Source commit | [ef9c6d332c1f5f705d78b667f5f6bd60d63353a1](https://github.com/rohanrcode1/polyvol/commit/ef9c6d332c1f5f705d78b667f5f6bd60d63353a1) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Tests reversion at bid/ask with both fees and clusters statistical inference by market. Mid-price reversion is not trading edge until feed timing and taker economics survive. |

## What this project does

A Polymarket research package testing price-path reversion and spot lag with real bid/ask data.

## Mechanism inspected

The economics script enters at the ask, exits at a later bid and subtracts taker fees on both legs. The statistical script estimates per-market effects and clusters inference by market instead of treating every second as independent.

## Limitation that matters

The README's performance conclusions were not independently replicated, and predictions on short crypto binaries do not transfer directly to perpetuals. The analysis still depends on the captured BBO and spot timestamps being causally aligned.

## Practical check for a trading system

Pair any reversion statistic with a same-tape executable-price test, fees and market-clustered uncertainty.

## Why this score

4/5 because Both mechanism and falsification path are visible; source reading alone does not verify reported results or cross-feed timing.

## Source trail

[README](https://github.com/rohanrcode1/polyvol/blob/ef9c6d332c1f5f705d78b667f5f6bd60d63353a1/README.md#L87); [scripts/edge_economics.py](https://github.com/rohanrcode1/polyvol/blob/ef9c6d332c1f5f705d78b667f5f6bd60d63353a1/scripts/edge_economics.py#L105); [scripts/edge_economics.py](https://github.com/rohanrcode1/polyvol/blob/ef9c6d332c1f5f705d78b667f5f6bd60d63353a1/scripts/edge_economics.py#L135); [scripts/mean_reversion_test.py](https://github.com/rohanrcode1/polyvol/blob/ef9c6d332c1f5f705d78b667f5f6bd60d63353a1/scripts/mean_reversion_test.py#L14); [License text](https://github.com/rohanrcode1/polyvol/blob/ef9c6d332c1f5f705d78b667f5f6bd60d63353a1/LICENSE.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
