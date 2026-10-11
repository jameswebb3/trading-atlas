# Abu — A backtest order is a calculated object

**Decision question:** Where does simulated order size come from?

| Field | Review |
| --- | --- |
| Upstream | [Abu](https://github.com/bbfamily/abu) |
| Primary area | Backtesting & Simulation |
| Source commit | [d602d847677e4c2b77b0a122df30816ea68b5710](https://github.com/bbfamily/abu/commit/d602d847677e4c2b77b0a122df30816ea68b5710) |
| Reviewed | 2026-10-06 |
| Declared license | [GPL-3.0](https://github.com/bbfamily/abu/blob/d602d847677e4c2b77b0a122df30816ea68b5710/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The buy-order path derives quantity from position capital and the chosen market rules before recording an order. Its market branches and rounding assumptions are tied to stocks and Chinese futures, not Hyperliquid perpetual contract constraints. |

## What this project does

A broad Chinese quantitative research and trading framework with separate market, factor, trade and metrics modules. [README](https://github.com/bbfamily/abu/blob/d602d847677e4c2b77b0a122df30816ea68b5710/readme.md).

## Mechanism inspected

The buy-order path derives quantity from position capital and the chosen market rules before recording an order. [Implementation](https://github.com/bbfamily/abu/blob/d602d847677e4c2b77b0a122df30816ea68b5710/abupy/TradeBu/ABuOrder.py#L53-L112).

## Limitation that matters

Its market branches and rounding assumptions are tied to stocks and Chinese futures, not Hyperliquid perpetual contract constraints. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Inspect position sizing and reject an order when the exchange minimum, precision or available collateral disagrees with the model.

## Why this score

Direct trading-system relevance: The buy-order path derives quantity from position capital and the chosen market rules before recording an order. Its market branches and rounding assumptions are tied to stocks and Chinese futures, not Hyperliquid perpetual contract constraints.

## Source trail

[README](https://github.com/bbfamily/abu/blob/d602d847677e4c2b77b0a122df30816ea68b5710/readme.md) · [Implementation](https://github.com/bbfamily/abu/blob/d602d847677e4c2b77b0a122df30816ea68b5710/abupy/TradeBu/ABuOrder.py#L53-L112).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
