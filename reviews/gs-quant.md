# A basket backtest can silently lose dates when its inputs disagree

**Decision question:** What happens when price, weight, and cost series cover different sessions?

| Field | Review |
| --- | --- |
| Upstream | [GS Quant](https://github.com/goldmansachs/gs-quant) |
| Primary area | Portfolio & Risk |
| Source commit | [f2a505a323692264c016f2623533cb5c47658d56](https://github.com/goldmansachs/gs-quant/commit/f2a505a323692264c016f2623533cb5c47658d56) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/goldmansachs/gs-quant/blob/f2a505a323692264c016f2623533cb5c47658d56/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Its basket backtest intersects the calendars of price, weight, and cost inputs before computing returns. That makes a complete-looking result possible even when sessions disappeared. The date policy is worth inspecting; the wider institutional stack is a poor fit for a self-hosted crypto trading system. |

## Mechanism worth inspecting

The [project overview](https://github.com/goldmansachs/gs-quant/blob/f2a505a323692264c016f2623533cb5c47658d56/README.md#L3-L7) identifies the institutional API context. The [basket backtest](https://github.com/goldmansachs/gs-quant/blob/f2a505a323692264c016f2623533cb5c47658d56/gs_quant/timeseries/backtesting.py#L56-L140) intersects the dates available for prices, weights, and costs before it applies rebalances and computes returns. A review can make those discarded dates explicit and demand an acceptance rule for missing observations.

## Important limit

The implementation is not a general trading simulator. Calendar intersection can erase missing-data evidence, while its return and cost calculations do not establish order execution, funding, or exchange-specific fills.

## Questions to take into your own design

- Which sessions are lost when input calendars are intersected?
- Is a missing session an acceptable exclusion or a data-quality failure?

## Why this score for a trading system

2/5: The calendar intersection is a precise, transferable backtest audit question. The surrounding client relies on institutional Marquee credentials, and this function does not model exchange fills or perpetual futures.

**Scope of this review:** We read the README and basket backtest implementation.
