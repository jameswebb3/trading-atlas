# QuantReplay — A market-state fallback can hide a broken simulator input

**Decision question:** Can a simulator continue after its source of market state fails?

| Field | Review |
| --- | --- |
| Upstream | [Quod-Financial/quantreplay](https://github.com/Quod-Financial/quantreplay) |
| Primary area | Backtesting & Simulation |
| Source commit | [a58c7c6d5436601d447129a7a81e662ba102cd9c](https://github.com/Quod-Financial/quantreplay/commit/a58c7c6d5436601d447129a7a81e662ba102cd9c) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README, relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The inspected generator catches every market-state request exception and proceeds with a default reply; the converter also guards bid depth before reading offer depth. These are source-visible paths, not a demonstrated runtime incident. Their effect depends on the actual optional values and caller, so a failure-injection test would be needed. |

## What this project does

QuantReplay is a self-hosted venue simulator that can replay stored feeds or generate order flow and expose simulated market data and execution via FIX. [Project README](https://github.com/Quod-Financial/quantreplay/blob/a58c7c6d5436601d447129a7a81e662ba102cd9c/README.md#L1).

## Mechanism inspected

The generator requests instrument state inside a catch-all that does not propagate failure. It converts the default reply afterward. In that conversion, the offer-depth assignment tests current_bid_depth and then reads current_offer_depth; if the latter is absent, the optional access is not protected by its own condition. [Market-state provider](https://github.com/Quod-Financial/quantreplay/blob/a58c7c6d5436601d447129a7a81e662ba102cd9c/project/generator/src/context/order_market_data_provider.cpp#L9).

## Limitation that matters

The converter is marked noexcept, which increases the consequence of an exception from missing optional data. This code reading does not establish how often the condition occurs or how the full simulator behaves under it. This is a source review, not a runtime or security test.

## Practical check for a trading system

A replay harness should stop or mark an input unavailable when market-state fetch fails. Test bid-present/offer-absent and offer-present/bid-absent states independently before accepting generated order flow.

## Why this score

3/5 because the source exposes a concrete execution-simulator failure mode, but this review covers a narrow generator path and does not validate the full matching engine.

## Source trail

[README](https://github.com/Quod-Financial/quantreplay/blob/a58c7c6d5436601d447129a7a81e662ba102cd9c/README.md#L15); [Market-state provider](https://github.com/Quod-Financial/quantreplay/blob/a58c7c6d5436601d447129a7a81e662ba102cd9c/project/generator/src/context/order_market_data_provider.cpp#L9); [Order generator](https://github.com/Quod-Financial/quantreplay/blob/a58c7c6d5436601d447129a7a81e662ba102cd9c/project/generator/src/random/algorithm/order_generation_algorithm.cpp#L104); [License](https://github.com/Quod-Financial/quantreplay/blob/a58c7c6d5436601d447129a7a81e662ba102cd9c/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
