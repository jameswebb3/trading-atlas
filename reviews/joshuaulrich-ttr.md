# TTR — Can the same EMA disagree after a different warm-up

**Decision question:** Can the same EMA disagree after a different warm-up?

| Field | Review |
| --- | --- |
| Upstream | [TTR](https://github.com/joshuaulrich/TTR) |
| Primary area | Signals & Models |
| Source commit | [76e5618e4a714f190519ee98da6de3234cf7d8b5](https://github.com/joshuaulrich/TTR/commit/76e5618e4a714f190519ee98da6de3234cf7d8b5) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-2.0-or-later](https://github.com/joshuaulrich/TTR/blob/76e5618e4a714f190519ee98da6de3234cf7d8b5/DESCRIPTION) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A useful indicator reference for exact warm-up and smoothing conventions. Its EMA uses a sample-mean seed and recursive state, so matching the period alone does not guarantee replay or cross-library parity. |

## Project overview

TTR provides technical-analysis functions for financial time series, including multiple moving-average conventions. [Project documentation](https://github.com/joshuaulrich/TTR/blob/76e5618e4a714f190519ee98da6de3234cf7d8b5/README.md#L1-L5).

## Mechanism worth inspecting

The EMA implementation finds the first usable value, leaves the warm-up region missing, seeds with an n-period mean, then recursively updates. The docs distinguish Wilder decay and warn about short-history instability. [Seed and recursion](https://github.com/joshuaulrich/TTR/blob/76e5618e4a714f190519ee98da6de3234cf7d8b5/src/moving_averages.c#L67-L89), [documented conventions](https://github.com/joshuaulrich/TTR/blob/76e5618e4a714f190519ee98da6de3234cf7d8b5/R/MovingAverages.R#L85-L111).

## Important limit

An n-period setting alone does not identify an EMA. Seed, smoothing ratio, input history and missing-data behavior affect its state; this is an indicator reference, not evidence of trading alpha.

## Questions to take into your own design

- Can the same EMA disagree after a different warm-up?
- Which seed, smoothing ratio and warm-up prefix define your indicator state?

## Why this score for a trading system

3/5: concrete signal-state behavior that affects reproducibility; familiar indicators offer no independent profitability evidence.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
