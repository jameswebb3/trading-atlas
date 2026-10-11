# Prediction Market Backtesting — When does synthetic liquidity become an unsupported fill assumption

**Decision question:** When does synthetic liquidity become an unsupported fill assumption?

| Field | Review |
| --- | --- |
| Upstream | [Prediction Market Backtesting](https://github.com/evan-kolberg/prediction-market-backtesting) |
| Primary area | Backtesting & Simulation |
| Source commit | [c76e77af00ef53472a9da8f66dae7fdd2d3e5928](https://github.com/evan-kolberg/prediction-market-backtesting/commit/c76e77af00ef53472a9da8f66dae7fdd2d3e5928) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT + LGPL-3.0-or-later (file-dependent)](https://github.com/evan-kolberg/prediction-market-backtesting/blob/c76e77af00ef53472a9da8f66dae7fdd2d3e5928/docs/license.md) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Separates recorded-book replay from a synthetic taker model and distinguishes entry from exit intent. Useful for auditing liquidity assumptions rather than transferring prediction-market strategies. |

## Project overview

NautilusTrader extensions and runners for prediction-market data loading, book replay and execution modeling. [Project documentation](https://github.com/evan-kolberg/prediction-market-backtesting/blob/c76e77af00ef53472a9da8f66dae7fdd2d3e5928/docs/execution-modeling.md#L3-L18).

## Mechanism worth inspecting

The non-book taker model builds an adverse-shifted synthetic order book with finite depth. Entry/exit intent comes from order tags or reduce-only before falling back to side. [Intent](https://github.com/evan-kolberg/prediction-market-backtesting/blob/c76e77af00ef53472a9da8f66dae7fdd2d3e5928/prediction_market_extensions/adapters/prediction_market/fill_model.py#L71-L94), [book construction](https://github.com/evan-kolberg/prediction-market-backtesting/blob/c76e77af00ef53472a9da8f66dae7fdd2d3e5928/prediction_market_extensions/adapters/prediction_market/fill_model.py#L173-L224).

## Important limit

If visible liquidity is absent, synthetic size can default to at least the order's quantity. This is an approximation, not recorded book depth; the documented public L2 runners use a separate passive-book path. [Fallback](https://github.com/evan-kolberg/prediction-market-backtesting/blob/c76e77af00ef53472a9da8f66dae7fdd2d3e5928/prediction_market_extensions/adapters/prediction_market/fill_model.py#L82-L94), [path distinction](https://github.com/evan-kolberg/prediction-market-backtesting/blob/c76e77af00ef53472a9da8f66dae7fdd2d3e5928/docs/execution-modeling.md#L69-L97).

## Questions to take into your own design

- When does synthetic liquidity become an unsupported fill assumption?
- Is absent book depth reported as unknown or replaced by order-sized synthetic liquidity?

## Why this score for a trading system

3/5: directly relevant execution-model distinctions, with binary-market price and settlement conventions that do not transfer unchanged.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
