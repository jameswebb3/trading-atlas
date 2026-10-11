# Vela — Lower-timeframe bars are not ticks

**Decision question:** What information is exposed by replaying a coarse bar from finer bars?

| Field | Review |
| --- | --- |
| Upstream | [LuxAlgo/Vela](https://github.com/LuxAlgo/Vela) |
| Primary area | Backtesting & Simulation |
| Source commit | [766a0f134935ac714871c5e89ba63940a245965f](https://github.com/LuxAlgo/Vela/commit/766a0f134935ac714871c5e89ba63940a245965f) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/LuxAlgo/Vela/blob/766a0f134935ac714871c5e89ba63940a245965f/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | `lowerTimeframeTicks` fetches finer bars within the target span and `barsToTicks` emits one replay update per finer bar using its close, high, low and volume. The update knows the finer bar's full range at its close; it is not a trade tape and cannot infer queue priority or the order of high and low. |

## What this project does

Headless financial chart core with providers, indicators and visual replay. [README](https://github.com/LuxAlgo/Vela/blob/766a0f134935ac714871c5e89ba63940a245965f/README.md).

## Mechanism inspected

`lowerTimeframeTicks` fetches finer bars within the target span and `barsToTicks` emits one replay update per finer bar using its close, high, low and volume. [Implementation](https://github.com/LuxAlgo/Vela/blob/766a0f134935ac714871c5e89ba63940a245965f/src/core/replayTicks.ts#L8-L37).

## Limitation that matters

The update knows the finer bar's full range at its close; it is not a trade tape and cannot infer queue priority or the order of high and low. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Tag replay granularity explicitly and prohibit maker-fill conclusions from synthetic updates derived from OHLC bars.

## Why this score

`lowerTimeframeTicks` fetches finer bars within the target span and `barsToTicks` emits one replay update per finer bar using its close, high, low and volume. The update knows the finer bar's full range at its close; it is not a trade tape and cannot infer queue priority or the order of high and low.

## Source trail

[README](https://github.com/LuxAlgo/Vela/blob/766a0f134935ac714871c5e89ba63940a245965f/README.md) · [Implementation](https://github.com/LuxAlgo/Vela/blob/766a0f134935ac714871c5e89ba63940a245965f/src/core/replayTicks.ts#L8-L37) · [License](https://github.com/LuxAlgo/Vela/blob/766a0f134935ac714871c5e89ba63940a245965f/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
