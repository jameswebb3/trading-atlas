# coinjure - Are backtest bids and asks observed or synthesized from a price series?

**Decision question:** Are backtest bids and asks observed or synthesized from a price series?

| Field | Review |
| --- | --- |
| Upstream | [ulab-uiuc/coinjure](https://github.com/ulab-uiuc/coinjure) |
| Primary area | Backtesting & Simulation |
| Source commit | [51bd34c0e3172973714181332bbdffac46716071](https://github.com/ulab-uiuc/coinjure/commit/51bd34c0e3172973714181332bbdffac46716071) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The backtester interleaves historical price points and constructs synthetic bid and ask events using fixed half-spread and book size. Those generated levels are assumptions, not observed executable depth, so simulated fills can overstate tradability. |

## What this project does

A prediction-market relation discovery and backtesting toolkit.

## Mechanism inspected

The backtester interleaves historical price points and constructs synthetic bid and ask events using fixed half-spread and book size.

## Limitation that matters

Those generated levels are assumptions, not observed executable depth, so simulated fills can overstate tradability.

## Practical check for a trading system

Carry an explicit synthetic-book flag and rerun candidates against recorded order books.

## Why this score

2/5. Its event structure is useful, while its liquidity evidence is unsuitable for execution claims.

## Source trail

[README](https://github.com/ulab-uiuc/coinjure/blob/51bd34c0e3172973714181332bbdffac46716071/README.md#L1); [docs/index.md](https://github.com/ulab-uiuc/coinjure/blob/51bd34c0e3172973714181332bbdffac46716071/docs/index.md#L1); [coinjure/engine/backtester.py](https://github.com/ulab-uiuc/coinjure/blob/51bd34c0e3172973714181332bbdffac46716071/coinjure/engine/backtester.py#L103); [Root license](https://github.com/ulab-uiuc/coinjure/blob/51bd34c0e3172973714181332bbdffac46716071/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
