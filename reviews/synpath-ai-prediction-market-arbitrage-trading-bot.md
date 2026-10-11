# Prediction Market Arbitrage Bot - Can two backtested venue quotes be bought as one hedge?

**Decision question:** Can two backtested venue quotes be bought as one hedge?

| Field | Review |
| --- | --- |
| Upstream | [Synpath-ai/prediction-market-arbitrage-trading-bot](https://github.com/Synpath-ai/prediction-market-arbitrage-trading-bot) |
| Primary area | Backtesting & Simulation |
| Source commit | [f59eca89aa3c0d845e776ff6531dbbdace4f00d7](https://github.com/Synpath-ai/prediction-market-arbitrage-trading-bot/commit/f59eca89aa3c0d845e776ff6531dbbdace4f00d7) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Prices two cross-venue binary hedges after taker fees; its bar replay assumes unavailable size and full paired fills. The historical price bars do not prove either leg was available at the same time or size. |

## What this project does

A paper trading and bar-backtest example for paired YES and NO positions across Kalshi and Polymarket.

## Mechanism inspected

The pricer computes both cross-venue YES/NO pairings, prices taker fees at the configured contract size, and bounds known top-of-book sizes by the smaller leg. The backtest reuses the live pricing and strategy objects on synchronized price bars.

## Limitation that matters

The historical Polymarket side is sampled price or trade-bar data, not a replayed order book. Size is absent from the candles and the backtest assumes full configured-size fills at the quoted prices; it cannot model one-leg exposure when the hedge misses.

## Practical check for a trading system

Keep pair pricing separate from execution claims. Use dual venue books and explicit leg-fill/hedge-failure states before valuing cross-venue arbitrage.

## Why this score

3/5 because A directly relevant fee-aware pairing mechanism is visible, but the historical execution assumptions are too optimistic to support returns.

## Source trail

[README paper scope](https://github.com/Synpath-ai/prediction-market-arbitrage-trading-bot/blob/f59eca89aa3c0d845e776ff6531dbbdace4f00d7/README.md#L168); [Two-leg pricing](https://github.com/Synpath-ai/prediction-market-arbitrage-trading-bot/blob/f59eca89aa3c0d845e776ff6531dbbdace4f00d7/src/arbitrage.py#L104); [Bar simulation](https://github.com/Synpath-ai/prediction-market-arbitrage-trading-bot/blob/f59eca89aa3c0d845e776ff6531dbbdace4f00d7/backtest/backtest.py#L40); [Historical size caveat](https://github.com/Synpath-ai/prediction-market-arbitrage-trading-bot/blob/f59eca89aa3c0d845e776ff6531dbbdace4f00d7/backtest/data.py#L1); [License](https://github.com/Synpath-ai/prediction-market-arbitrage-trading-bot/blob/f59eca89aa3c0d845e776ff6531dbbdace4f00d7/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
