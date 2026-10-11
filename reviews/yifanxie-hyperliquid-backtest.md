# Hyperliquid Backtest Toolkit - Does a Hyperliquid-style candle backtest admit what it cannot fill?

**Decision question:** Does a Hyperliquid-style candle backtest admit what it cannot fill?

| Field | Review |
| --- | --- |
| Upstream | [yifanxie/hyperliquid-backtest](https://github.com/yifanxie/hyperliquid-backtest) |
| Primary area | Backtesting & Simulation |
| Source commit | [d6922113c2f164eec6d7eb958c4622bf4b05e323](https://github.com/yifanxie/hyperliquid-backtest/commit/d6922113c2f164eec6d7eb958c4622bf4b05e323) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Models a USDC-margined perpetual ledger and defaults to next-bar fills, while explicitly leaving partial fills and L2 impact outside the simulation. A candle touching a limit does not prove queue access; the optional same-bar-close path needs a causal signal timestamp. |

## What this project does

A local bar-by-bar simulation of a USDC-margined perpetual account with orders, fees, margin, hourly funding and a ledger.

## Mechanism inspected

The order model distinguishes submitted, accepted, rejected, partially filled and terminal states; the engine defaults signals to next-bar-open execution and routes pending orders through a candle matcher. The README explicitly declares a full-fill candle model rather than claiming order-book execution.

## Limitation that matters

The status vocabulary is broader than the implemented fill physics: partial fills are reserved in configuration but not simulated, and there is no L2 depth or queue impact. Switching to same-bar-close can also make the signal depend on the close used for execution.

## Practical check for a trading system

Treat its ledger and next-bar scheduling as a reference for bar-level studies, but require a separate L2 or live-fill check before inferring capacity or maker execution.

## Why this score

4/5 because Direct Hyperliquid perpetual accounting and explicit timing limits are visible in code; missing depth and partial fills rule out a 5/5 execution reference.

## Source trail

[README execution limits](https://github.com/yifanxie/hyperliquid-backtest/blob/d6922113c2f164eec6d7eb958c4622bf4b05e323/README.md#L342); [Order timing default](https://github.com/yifanxie/hyperliquid-backtest/blob/d6922113c2f164eec6d7eb958c4622bf4b05e323/src/hyperliquid_backtest/domain/orders.py#L183); [Candle matching](https://github.com/yifanxie/hyperliquid-backtest/blob/d6922113c2f164eec6d7eb958c4622bf4b05e323/src/hyperliquid_backtest/engine/backtest.py#L381); [Order state transitions](https://github.com/yifanxie/hyperliquid-backtest/blob/d6922113c2f164eec6d7eb958c4622bf4b05e323/src/hyperliquid_backtest/domain/orders.py#L200); [License](https://github.com/yifanxie/hyperliquid-backtest/blob/d6922113c2f164eec6d7eb958c4622bf4b05e323/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
