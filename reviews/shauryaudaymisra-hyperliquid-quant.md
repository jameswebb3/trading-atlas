# hyperliquid_quant - Are risk and feature inputs clipped to the current Hyperliquid bar?

**Decision question:** Are risk and feature inputs clipped to the current Hyperliquid bar?

| Field | Review |
| --- | --- |
| Upstream | [ShauryaUdayMisra/hyperliquid_quant](https://github.com/ShauryaUdayMisra/hyperliquid_quant) |
| Primary area | Backtesting & Simulation |
| Source commit | [e591551c74367c1daabb50687b715e51b39783ef](https://github.com/ShauryaUdayMisra/hyperliquid_quant/commit/e591551c74367c1daabb50687b715e51b39783ef) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Clips history and liquidity sizing to elapsed bars while retaining unavailable historical book fields as missing. Index-aligned features still need an independent available-at contract. |

## What this project does

A Hyperliquid-oriented research engine with a point-in-time MarketView and separate data verification commands.

## Mechanism inspected

History access slices through the current bar; liquidity sizing uses a recent median from that slice so tomorrow's volume cannot license today's size. The engine orders funding, liquidation and strategy actions within each bar.

## Limitation that matters

The feature accessor returns row i from a supplied feature frame; the inspected code does not itself prove that each row's source was available at bar i. The README says historical order-book fields are absent rather than imputed, so book-sensitive strategies need separate recorded data.

## Practical check for a trading system

Test timestamp alignment of every feature frame before using the MarketView and retain nulls where historical book information does not exist.

## Why this score

3/5 because The bar cursor and liquidity guard are direct, but feature-frame provenance and bar-level fills remain external conditions.

## Source trail

[README](https://github.com/ShauryaUdayMisra/hyperliquid_quant/blob/e591551c74367c1daabb50687b715e51b39783ef/README.md#L1); [backtest/engine.py](https://github.com/ShauryaUdayMisra/hyperliquid_quant/blob/e591551c74367c1daabb50687b715e51b39783ef/backtest/engine.py#L86); [backtest/engine.py](https://github.com/ShauryaUdayMisra/hyperliquid_quant/blob/e591551c74367c1daabb50687b715e51b39783ef/backtest/engine.py#L93); [backtest/engine.py](https://github.com/ShauryaUdayMisra/hyperliquid_quant/blob/e591551c74367c1daabb50687b715e51b39783ef/backtest/engine.py#L110); [README limitation](https://github.com/ShauryaUdayMisra/hyperliquid_quant/blob/e591551c74367c1daabb50687b715e51b39783ef/README.md#L217).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
