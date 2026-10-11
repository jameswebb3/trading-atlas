# Hyperliquid Backtester - Does the published Hyperliquid backtester implement the advertised funding mechanics?

**Decision question:** Does the published Hyperliquid backtester implement the advertised funding mechanics?

| Field | Review |
| --- | --- |
| Upstream | [xsa-dev/hyperliquid-backtest](https://github.com/xsa-dev/hyperliquid-backtest) |
| Primary area | Backtesting & Simulation |
| Source commit | [5014f56d9eaac917ca51429f994a3383651cf965](https://github.com/xsa-dev/hyperliquid-backtest/commit/5014f56d9eaac917ca51429f994a3383651cf965) |
| Reviewed | 2026-10-11 |
| Declared license | MIT (Cargo.toml) |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Advertises a broad Hyperliquid backtester, while its inspected backtest module is only a funding-payment record. A funding struct is not a funding settlement engine or a validated historical replay. |

## What this project does

A Rust crate whose README advertises live data integration, funding and a broad strategy suite.

## Mechanism inspected

The inspected library exports small Position, RiskManager and FundingPayment building blocks. Its backtest module defines a funding-payment record with timestamp, size, rate, amount and mark.

## Limitation that matters

The inspected backtest.rs contains only that data structure; it does not settle funding or implement a replay engine. Example names and README feature claims are not evidence that those paths work through this library API. The package manifest declares MIT; a standalone root license text was not verified.

## Practical check for a trading system

Inspect the actual exported engine and runnable tests at a pinned commit before treating a feature list as an implementation reference.

## Why this score

1/5 because A relevant caution about README-to-code mismatch, with little usable backtest mechanism at the reviewed commit.

## Source trail

[README](https://github.com/xsa-dev/hyperliquid-backtest/blob/5014f56d9eaac917ca51429f994a3383651cf965/README.md#L1); [src/lib.rs](https://github.com/xsa-dev/hyperliquid-backtest/blob/5014f56d9eaac917ca51429f994a3383651cf965/src/lib.rs#L1); [src/backtest.rs](https://github.com/xsa-dev/hyperliquid-backtest/blob/5014f56d9eaac917ca51429f994a3383651cf965/src/backtest.rs#L3).

[Cargo.toml](https://github.com/xsa-dev/hyperliquid-backtest/blob/5014f56d9eaac917ca51429f994a3383651cf965/Cargo.toml#L13).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
