# Crypto_MM - Does a maker quote wait for an arriving print after its latency?

**Decision question:** Does a maker quote wait for an arriving print after its latency?

| Field | Review |
| --- | --- |
| Upstream | [Starkl7/Crypto_MM](https://github.com/Starkl7/Crypto_MM) |
| Primary area | Backtesting & Simulation |
| Source commit | [f87033fae0fcee55ce8a3bd7197bd1fd55e35a9b](https://github.com/Starkl7/Crypto_MM/commit/f87033fae0fcee55ce8a3bd7197bd1fd55e35a9b) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation, and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Carries calibration and inventory through walk-forward windows and fills only on later trade-through prints. Trade-through is stronger than touch but still does not prove queue priority or maker economics. |

## What this project does

A C++ walk-forward Avellaneda-Stoikov market-making study for crypto perpetuals.

## Mechanism inspected

The replay carries inventory between test windows, applies calibration to later windows and delays new or canceled quotes. A bid is credited only when a real tape print trades strictly through the live bid; the model's intensity estimate sets spread rather than generating fills.

## Limitation that matters

The README acknowledges no queue-position or maker-fee model. A trade-through print can still over-credit an order without size ahead, and reported returns were not reproduced.

## Practical check for a trading system

Treat trade-through results as a fill upper bound, vary fees and queue-ahead, and retain the recalibration delay during out-of-sample replay.

## Why this score

3/5 because Walk-forward sequencing and print-gated fills are direct, but absent queue and fee economics keep PnL provisional.

## Source trail

[README](https://github.com/Starkl7/Crypto_MM/blob/f87033fae0fcee55ce8a3bd7197bd1fd55e35a9b/README.md#L59); [README](https://github.com/Starkl7/Crypto_MM/blob/f87033fae0fcee55ce8a3bd7197bd1fd55e35a9b/README.md#L202); [src/walk_forward.cpp](https://github.com/Starkl7/Crypto_MM/blob/f87033fae0fcee55ce8a3bd7197bd1fd55e35a9b/src/walk_forward.cpp#L92); [src/fill_engine.cpp](https://github.com/Starkl7/Crypto_MM/blob/f87033fae0fcee55ce8a3bd7197bd1fd55e35a9b/src/fill_engine.cpp#L122); [tests/test_main.cpp](https://github.com/Starkl7/Crypto_MM/blob/f87033fae0fcee55ce8a3bd7197bd1fd55e35a9b/tests/test_main.cpp#L116); [License text](https://github.com/Starkl7/Crypto_MM/blob/f87033fae0fcee55ce8a3bd7197bd1fd55e35a9b/LICENSE#L1); [README limitation](https://github.com/Starkl7/Crypto_MM/blob/f87033fae0fcee55ce8a3bd7197bd1fd55e35a9b/README.md#L206).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
