# honest-backtest - Did the displayed ask survive until the taker order arrived?

**Decision question:** Did the displayed ask survive until the taker order arrived?

| Field | Review |
| --- | --- |
| Upstream | [JohanAlvarado/honest-backtest](https://github.com/JohanAlvarado/honest-backtest) |
| Primary area | Backtesting & Simulation |
| Source commit | [fefcd0eae4ba02105a2e0965ec1355fe2306491a](https://github.com/JohanAlvarado/honest-backtest/commit/fefcd0eae4ba02105a2e0965ec1355fe2306491a) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Regrades paper buys against the ask seen after order latency and, when available, a corroborating execution tape. Book persistence and tape prints strengthen a fill claim but cannot establish your own queue or exact size. |

## What this project does

A prediction-market research harness that grades paper signals against delayed book persistence and an optional real trade tape.

## Mechanism inspected

The taker grader rechecks the ask after a latency interval and marks an intended buy missed if the ask moved above its limit. A stricter tape corroboration lens searches for a taker buy at or below that limit; results retain whether the book check or tape was actually available.

## Limitation that matters

A later surviving ask does not prove that this specific order would have filled at the recorded size. The maker route is explicitly optimistic about FIFO, and tape corroboration needs complete correctly matched trade data. The source code is an audit lens, not independent replication of the README result.

## Practical check for a trading system

Report paper, arrival-book and tape-backed outcomes separately, including unknown cases; use the gap to test whether edge survives actual transactable conditions.

## Why this score

4/5 because The source directly exposes adverse-selection and phantom-fill mechanisms with separate evidence levels, although neither lens certifies a personal order fill.

## Source trail

[README grading lenses](https://github.com/JohanAlvarado/honest-backtest/blob/fefcd0eae4ba02105a2e0965ec1355fe2306491a/README.md#L14); [Arrival-book and tape checks](https://github.com/JohanAlvarado/honest-backtest/blob/fefcd0eae4ba02105a2e0965ec1355fe2306491a/honest_backtest/fills.py#L29); [Maker assumption](https://github.com/JohanAlvarado/honest-backtest/blob/fefcd0eae4ba02105a2e0965ec1355fe2306491a/honest_backtest/fills.py#L82); [Evaluation harness](https://github.com/JohanAlvarado/honest-backtest/blob/fefcd0eae4ba02105a2e0965ec1355fe2306491a/honest_backtest/harness.py#L13); [License](https://github.com/JohanAlvarado/honest-backtest/blob/fefcd0eae4ba02105a2e0965ec1355fe2306491a/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
