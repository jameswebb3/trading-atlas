# AlgoBulls Strategy Pool — What does an indicator recipe actually establish about a strategy

**Decision question:** What does an indicator recipe actually establish about a strategy?

| Field | Review |
| --- | --- |
| Upstream | [AlgoBulls Strategy Pool](https://github.com/algobulls/pyalgostrategypool) |
| Primary area | Signals & Models |
| Source commit | [ee6a6fc1d36f2f3d838c89450a723edb092955bb](https://github.com/algobulls/pyalgostrategypool/commit/ee6a6fc1d36f2f3d838c89450a723edb092955bb) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/algobulls/pyalgostrategypool/blob/ee6a6fc1d36f2f3d838c89450a723edb092955bb/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Readable indicator and order callbacks for the AlgoBulls platform. Useful as recipes to inspect, with research validity and execution semantics left to the surrounding system. |

## Project overview

Collection of trading-strategy implementations built for the AlgoBulls platform. [Project documentation](https://github.com/algobulls/pyalgostrategypool/blob/ee6a6fc1d36f2f3d838c89450a723edb092955bb/README.md#L1-L12).

## Mechanism worth inspecting

The Bollinger example separates instrument selection, order submission and exit selection. It compares previous-candle values against the latest computed band and requires a completed broker order before selecting an exit. [Strategy](https://github.com/algobulls/pyalgostrategypool/blob/ee6a6fc1d36f2f3d838c89450a723edb092955bb/pyalgostrategypool/strategy_bollinger_bands_intraday/_strategy.py#L30-L87), [API documentation index](https://github.com/algobulls/pyalgostrategypool/blob/ee6a6fc1d36f2f3d838c89450a723edb092955bb/docs/source/pyalgostrategypool.rst#L7-L21).

## Important limit

Execution and data-window semantics come from an external platform/base class. The inspected recipe does not establish point-in-time availability, costs or out-of-sample profitability. [Imports and callbacks](https://github.com/algobulls/pyalgostrategypool/blob/ee6a6fc1d36f2f3d838c89450a723edb092955bb/pyalgostrategypool/strategy_bollinger_bands_intraday/_strategy.py#L11-L38).

## Questions to take into your own design

- What does an indicator recipe actually establish about a strategy?
- Which completed candle and band timestamps does the base class actually expose?

## Why this score for a trading system

2/5: directly trading-related examples, but the inspected mechanism supplies little new evidence about reliable research or execution.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
