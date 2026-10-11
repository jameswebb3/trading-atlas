# vibe-investing - Missing settlement data is a result state, not a loss

**Decision question:** What happens to a prediction when its evaluation price is unavailable?

| Field | Review |
| --- | --- |
| Upstream | [gameworkerkim/vibe-investing](https://github.com/gameworkerkim/vibe-investing) |
| Primary area | Backtesting & Simulation |
| Source commit | [a90e98a3b20666bd0df130ed81e60c60e6b62f69](https://github.com/gameworkerkim/vibe-investing/commit/a90e98a3b20666bd0df130ed81e60c60e6b62f69) |
| Reviewed | 2026-10-10 |
| Declared license | MIT badge in README; no root license file found at the reviewed commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Separates settled wins and losses from missing-price and stale-prediction states in a ticker-prediction ledger. Settlement relies on a later yfinance close and a weekday-only calendar; it does not establish point-in-time price validity or tradability. |

## What this project does

A broad investing research repository with a ticker-prediction component. This review covers only the settlement service and its persistent prediction states.

## Mechanism inspected

The service fetches a target-date close, changes pending predictions to settled win or loss when a close exists, and records no_data with a cause when it does not. A separate expiry path turns stale pending predictions into no_data rather than letting them remain pending indefinitely.

## Limitation that matters

The inspected service uses yfinance closing prices and a Korea-time schedule, while its next-trading-day helper only skips weekends. This does not validate corporate actions, US holidays, corrections or point-in-time price availability. The missing-price state is valuable, but these result labels are not evidence of a tradable signal. This is a source review, not a runtime or security test.

## Practical check for a trading system

For research or pre-registration ledgers, report unresolved and missing-observation outcomes separately from wins and losses. Bind each settlement to a pinned price source and availability clock before using it to change weights.

## Why this score

2/5 because the explicit no-data outcome is directly relevant to honest strategy evaluation, but the surrounding equity-style settlement path is not a trading-grade causal test.

## Source trail

[README](https://github.com/gameworkerkim/vibe-investing/blob/a90e98a3b20666bd0df130ed81e60c60e6b62f69/README.md#L1); [Settlement and expiry](https://github.com/gameworkerkim/vibe-investing/blob/a90e98a3b20666bd0df130ed81e60c60e6b62f69/AIInvestor/services/prediction_settler.py#L74); [Missing close](https://github.com/gameworkerkim/vibe-investing/blob/a90e98a3b20666bd0df130ed81e60c60e6b62f69/AIInvestor/services/prediction_settler.py#L86); [Weekday helper](https://github.com/gameworkerkim/vibe-investing/blob/a90e98a3b20666bd0df130ed81e60c60e6b62f69/AIInvestor/services/prediction_settler.py#L31); [Prediction states](https://github.com/gameworkerkim/vibe-investing/blob/a90e98a3b20666bd0df130ed81e60c60e6b62f69/AIInvestor/services/prediction_repo.py#L5).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
