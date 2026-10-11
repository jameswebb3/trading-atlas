# Quantdom: examine signal timing and partial-close accounting separately

**Decision question:** Can a next-bar strategy example still use incomplete position accounting?

| Field | Review |
| --- | --- |
| Upstream | [Quantdom](https://github.com/constverum/Quantdom) |
| Primary area | Backtesting & Simulation |
| Source commit | [e05304006d3805f941d5f1033135730287b447e6](https://github.com/constverum/Quantdom/commit/e05304006d3805f941d5f1033135730287b447e6) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/constverum/Quantdom/blob/e05304006d3805f941d5f1033135730287b447e6/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Offers a small visual backtesting framework with a readable next-bar example. Its position code also exposes explicit limitations around partial closes and margin, useful reminders that causal signal timing alone does not make a simulation faithful. |

## Project overview

An early-alpha Python framework provides strategy backtests, portfolio analysis, and charts. [Project documentation](https://github.com/constverum/Quantdom/blob/e05304006d3805f941d5f1033135730287b447e6/README.rst#L15-L28).

## Mechanism worth inspecting

The [example strategy](https://github.com/constverum/Quantdom/blob/e05304006d3805f941d5f1033135730287b447e6/examples/simple_strategies.py#L15-L44) executes the previous signal at the current open before updating signal state from the current bar. The [position close](https://github.com/constverum/Quantdom/blob/e05304006d3805f941d5f1033135730287b447e6/quantdom/lib/portfolio.py#L271-L282) updates realized profit and closes the position.

## Important limit

The [close wrapper](https://github.com/constverum/Quantdom/blob/e05304006d3805f941d5f1033135730287b447e6/quantdom/lib/portfolio.py#L398-L402) documents that a partial close changes the whole status to CLOSED. [Order opening](https://github.com/constverum/Quantdom/blob/e05304006d3805f941d5f1033135730287b447e6/quantdom/lib/portfolio.py#L382-L390) has an unfinished margin check, and the [profit formulas](https://github.com/constverum/Quantdom/blob/e05304006d3805f941d5f1033135730287b447e6/quantdom/lib/portfolio.py#L284-L349) are gross calculations rather than a complete cost model.

## Questions to take into your own design

- Do partial closes preserve remaining quantity and its unrealized PnL?
- Are entry timing, costs, and margin validated independently?

## Why this score for a trading system

2/5: educational next-bar and accounting source, limited by explicit partial-close and margin gaps.

**Scope of this review:** README, documented strategy example, position and order accounting source.
