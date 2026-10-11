# Hyperliquid Rust Bot — OHLC fills need explicit bounds

**Decision question:** How does a candle backtest decide whether a resting order could fill?

| Field | Review |
| --- | --- |
| Upstream | [0xNoSystem/hyperliquid_rust_bot](https://github.com/0xNoSystem/hyperliquid_rust_bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [4a71bcb0f666132f741d8b9df650a6b4e0d77096](https://github.com/0xNoSystem/hyperliquid_rust_bot/commit/4a71bcb0f666132f741d8b9df650a6b4e0d77096) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/0xNoSystem/hyperliquid_rust_bot/blob/4a71bcb0f666132f741d8b9df650a6b4e0d77096/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The backtester excludes orders created on the current candle from resting-order fills, which removes one obvious same-bar hindsight path. OHLC data still cannot reconstruct queue position or intrabar event order; market orders priced at a candle close can remain optimistic. |

## What this project does

A local Hyperliquid perpetual terminal with scripts and an OHLC-based backtest. [Project README](https://github.com/0xNoSystem/hyperliquid_rust_bot/blob/4a71bcb0f666132f741d8b9df650a6b4e0d77096/README.md#L1).

## Mechanism inspected

The backtester excludes orders created on the current candle from resting-order fills, which removes one obvious same-bar hindsight path. [Implementation](https://github.com/0xNoSystem/hyperliquid_rust_bot/blob/4a71bcb0f666132f741d8b9df650a6b4e0d77096/src/backtest/backtester.rs#L698). [Related source 1](https://github.com/0xNoSystem/hyperliquid_rust_bot/blob/4a71bcb0f666132f741d8b9df650a6b4e0d77096/README.md#L25).

## Limitation that matters

OHLC data still cannot reconstruct queue position or intrabar event order; market orders priced at a candle close can remain optimistic. This is a source review, not a runtime or security test.

## Practical check for a trading system

State which orders can fill on each bar and mark unresolved intrabar cases as model assumptions.

## Why this score

Its same-bar guard is concrete, but its candle fill model is too coarse for execution-quality claims.

## Source trail

[README](https://github.com/0xNoSystem/hyperliquid_rust_bot/blob/4a71bcb0f666132f741d8b9df650a6b4e0d77096/README.md#L1); [Implementation](https://github.com/0xNoSystem/hyperliquid_rust_bot/blob/4a71bcb0f666132f741d8b9df650a6b4e0d77096/src/backtest/backtester.rs#L698); [Related source 1](https://github.com/0xNoSystem/hyperliquid_rust_bot/blob/4a71bcb0f666132f741d8b9df650a6b4e0d77096/README.md#L25) - [License](https://github.com/0xNoSystem/hyperliquid_rust_bot/blob/4a71bcb0f666132f741d8b9df650a6b4e0d77096/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
