# AutoTrader: a virtual broker can assume infinite top-of-book liquidity

**Decision question:** What fill assumption sits behind a virtual broker's backtest?

| Field | Review |
| --- | --- |
| Upstream | [AutoTrader](https://github.com/kieran-mackle/AutoTrader) |
| Primary area | Backtesting & Simulation |
| Source commit | [e686e48cf98a532ea1e1606ff66dea1f511e8e96](https://github.com/kieran-mackle/AutoTrader/commit/e686e48cf98a532ea1e1606ff66dea1f511e8e96) |
| Reviewed | 2026-09-25 |
| Declared license | [GPL-3.0](https://github.com/kieran-mackle/AutoTrader/blob/e686e48cf98a532ea1e1606ff66dea1f511e8e96/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Tracks pending, open, filled, and cancelled orders, but its documented backtest book has infinite top-level liquidity and bid/ask prices derived from OHLC plus a spread model. Order-state vocabulary alone does not make those fills venue-realistic. |

## Mechanism worth inspecting

The [README](https://github.com/kieran-mackle/AutoTrader/blob/e686e48cf98a532ea1e1606ff66dea1f511e8e96/README.md#L50-L54) presents a backtest and paper-trading simulator. The [virtual-broker guide](https://github.com/kieran-mackle/AutoTrader/blob/e686e48cf98a532ea1e1606ff66dea1f511e8e96/docs/source/broker/virtual-broker.md#L25-L36) defines order states, then [states the fill model](https://github.com/kieran-mackle/AutoTrader/blob/e686e48cf98a532ea1e1606ff66dea1f511e8e96/docs/source/broker/virtual-broker.md#L50-L68): backtests simulate infinite liquidity at the top of a book from OHLC and a configured spread, whereas live paper mode may query a real order book. The [implementation](https://github.com/kieran-mackle/AutoTrader/blob/e686e48cf98a532ea1e1606ff66dea1f511e8e96/autotrader/brokers/virtual.py#L100-L137) keeps separate open, filled, and fill records.

## Important limit

A real book snapshot in paper mode still does not prove queue priority or executed fill prices. The inspected backtest path is unsuitable for estimating capacity-sensitive limit-order returns on a thin venue.

## Questions to take into your own design

- Are fill assumptions visible beside every reported backtest?
- Can depth, latency, and partial fills be compared with actual venue traces?

## Why this score for a trading system

Its explicit virtual-broker assumption is useful for reviewing fill claims, but infinite liquidity sharply limits direct execution realism.

**Scope of this review:** We read the pinned README, virtual-broker guide, and selected state code. We did not run the simulator.
