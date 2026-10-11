# Squant — An equities clock is not a perpetual clock

**Decision question:** Does the backtest clock advance through hours when the market would still trade?

| Field | Review |
| --- | --- |
| Upstream | [eryk/squant](https://github.com/eryk/squant) |
| Primary area | Portfolio & Risk |
| Source commit | [ff69d0accd23a6f7d0d59ae049e899a625f6fd78](https://github.com/eryk/squant/commit/ff69d0accd23a6f7d0d59ae049e899a625f6fd78) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | Its BACKTEST clock jumps from after 15:00 to the next day at 09:30, while a live clock uses wall time. That calendar skips overnight perpetual trading and makes replay/live time semantics diverge. |

## What this project does

A Scala framework for equity and FX data and backtesting. [Project README](https://github.com/eryk/squant/blob/ff69d0accd23a6f7d0d59ae049e899a625f6fd78/README.md#L1).

## Mechanism inspected

Its BACKTEST clock jumps from after 15:00 to the next day at 09:30, while a live clock uses wall time. [Implementation](https://github.com/eryk/squant/blob/ff69d0accd23a6f7d0d59ae049e899a625f6fd78/src/main/scala/com/squant/cheetah/engine/Clock.scala#L17). [Related source 1](https://github.com/eryk/squant/blob/ff69d0accd23a6f7d0d59ae049e899a625f6fd78/src/main/scala/com/squant/cheetah/Feeds.scala#L14).

## Limitation that matters

That calendar skips overnight perpetual trading and makes replay/live time semantics diverge. Some inspected feed methods are unfinished. This is a source review, not a runtime or security test.

## Practical check for a trading system

Prove event-time parity and 24/7 funding boundaries before transferring any session-based backtest pattern.

## Why this score

A clear calendar-mismatch caution, with limited direct value for perpetuals.

## Source trail

[README](https://github.com/eryk/squant/blob/ff69d0accd23a6f7d0d59ae049e899a625f6fd78/README.md#L1); [Implementation](https://github.com/eryk/squant/blob/ff69d0accd23a6f7d0d59ae049e899a625f6fd78/src/main/scala/com/squant/cheetah/engine/Clock.scala#L17); [Related source 1](https://github.com/eryk/squant/blob/ff69d0accd23a6f7d0d59ae049e899a625f6fd78/src/main/scala/com/squant/cheetah/Feeds.scala#L14).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
