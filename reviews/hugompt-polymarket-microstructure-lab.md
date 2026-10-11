# polymarket-microstructure-lab - What happens to one signal as order latency increases?

**Decision question:** What happens to one signal as order latency increases?

| Field | Review |
| --- | --- |
| Upstream | [hugompt/polymarket-microstructure-lab](https://github.com/hugompt/polymarket-microstructure-lab) |
| Primary area | Backtesting & Simulation |
| Source commit | [d0ac7013b667ee4a6127d55c9a65de5f9d127438](https://github.com/hugompt/polymarket-microstructure-lab/commit/d0ac7013b667ee4a6127d55c9a65de5f9d127438) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Replays the same forward paper decision across a latency grid and computes fee-aware break-even thresholds. The latency curve describes the paper fill model; it is not a measurement of actual order fills or proof of the reported returns. |

## What this project does

A read-only Polymarket research lab that reconstructs wallet PnL and runs the same forward paper decision across several latency accounts.

## Mechanism inspected

The paper engine generates one decision and creates orders for a configured latency grid; separate fill and settlement ticks update each account. It reports realized PnL differences relative to the zero-latency account. The fee module computes break-even win rates from entry price and a market fee schedule instead of a fixed hit-rate target.

## Limitation that matters

The headline performance claims in the README were not independently reproduced. Forward paper orders are simulated against captured books and do not establish that a real order would have received the same queue position, size or settlement treatment.

## Practical check for a trading system

Hold the decision fixed while varying only arrival delay, and report both gross and fee-adjusted outcomes; keep paper-fill assumptions visible beside any claimed edge.

## Why this score

4/5 because A direct latency-sensitivity design with common decisions and fee-aware break-even calculations is visible, but reported PnL remains unreplicated paper evidence.

## Source trail

[README paper-study scope](https://github.com/hugompt/polymarket-microstructure-lab/blob/d0ac7013b667ee4a6127d55c9a65de5f9d127438/README.md#L128); [Shared decision and latency accounts](https://github.com/hugompt/polymarket-microstructure-lab/blob/d0ac7013b667ee4a6127d55c9a65de5f9d127438/backend/app/paper/engine.py#L145); [Settlement and latency verdict](https://github.com/hugompt/polymarket-microstructure-lab/blob/d0ac7013b667ee4a6127d55c9a65de5f9d127438/backend/app/paper/engine.py#L193); [Fee-aware break-even](https://github.com/hugompt/polymarket-microstructure-lab/blob/d0ac7013b667ee4a6127d55c9a65de5f9d127438/backend/app/analysis/fees.py#L1); [License](https://github.com/hugompt/polymarket-microstructure-lab/blob/d0ac7013b667ee4a6127d55c9a65de5f9d127438/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
