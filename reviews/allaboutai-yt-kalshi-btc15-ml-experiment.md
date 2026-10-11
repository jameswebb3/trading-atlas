# kalshi-btc15-ml-experiment - Can a model learn a correction to the market price?

**Decision question:** Can a model learn a correction to the market price?

| Field | Review |
| --- | --- |
| Upstream | [AllAboutAI-YT/kalshi-btc15-ml-experiment](https://github.com/AllAboutAI-YT/kalshi-btc15-ml-experiment) |
| Primary area | Signals & Models |
| Source commit | [19a152bd779a8ff26dc3af9ea14e09c3d869cbfa](https://github.com/AllAboutAI-YT/kalshi-btc15-ml-experiment/commit/19a152bd779a8ff26dc3af9ea14e09c3d869cbfa) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Offset logistic regression fixes market logit as an offset and learns regularized feature corrections. A statistical residual is not an executable edge until feature timing, fees, spread and out-of-sample calibration are checked. |

## What this project does

A Kalshi BTC 15-minute ML experiment with baseline and residual models.

## Mechanism inspected

Offset logistic regression fixes market logit as an offset and learns regularized feature corrections.

## Limitation that matters

A statistical residual is not an executable edge until feature timing, fees, spread and out-of-sample calibration are checked.

## Practical check for a trading system

Use market-implied probability as the baseline and preregister incremental decision value.

## Why this score

3/5. Transparent model structure, with profitability unestablished.

## Source trail

[README](https://github.com/AllAboutAI-YT/kalshi-btc15-ml-experiment/blob/19a152bd779a8ff26dc3af9ea14e09c3d869cbfa/README.md#L1); [train.py](https://github.com/AllAboutAI-YT/kalshi-btc15-ml-experiment/blob/19a152bd779a8ff26dc3af9ea14e09c3d869cbfa/train.py#L204); [Root license](https://github.com/AllAboutAI-YT/kalshi-btc15-ml-experiment/blob/19a152bd779a8ff26dc3af9ea14e09c3d869cbfa/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
