# algo-trader — Can replayed and live data drive the same strategy pipeline

**Decision question:** Can replayed and live data drive the same strategy pipeline?

| Field | Review |
| --- | --- |
| Upstream | [algo-trader](https://github.com/idanya/algo-trader) |
| Primary area | Backtesting & Simulation |
| Source commit | [742589a488f02bbffd6bc576c08357622084b7f9](https://github.com/idanya/algo-trader/commit/742589a488f02bbffd6bc576c08357622084b7f9) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/idanya/algo-trader/blob/742589a488f02bbffd6bc576c08357622084b7f9/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Builds configurable candle-processing pipelines for strategy research. A small architecture reference, with live integration and replay equivalence still requiring evidence. |

## Project overview

Python strategy pipeline and backtester with serializable components and unfinished live-provider integration. [Project documentation](https://github.com/idanya/algo-trader/blob/742589a488f02bbffd6bc576c08357622084b7f9/README.md#L9-L38).

## Mechanism worth inspecting

Documentation separates candle sources, processors, events and terminators. The backtest builder wires a database source through technical calculations into strategy and signal execution, using fixed research intervals. [Pipeline](https://github.com/idanya/algo-trader/blob/742589a488f02bbffd6bc576c08357622084b7f9/README.md#L54-L106), [builder](https://github.com/idanya/algo-trader/blob/742589a488f02bbffd6bc576c08357622084b7f9/src/algotrader/pipeline/builders/backtest.py#L19-L35).

## Important limit

The README explicitly says real-time providers are incomplete. Shared pipeline wiring is an architectural intention, not a demonstrated equivalence of live and historical event timing. [Status](https://github.com/idanya/algo-trader/blob/742589a488f02bbffd6bc576c08357622084b7f9/README.md#L12-L16).

## Questions to take into your own design

- Can replayed and live data drive the same strategy pipeline?
- Which event-order fixtures establish equivalence between live and historical providers?

## Why this score for a trading system

2/5: trading-specific structure, but the inspected builder adds little beyond mature source/processor designs already available.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
