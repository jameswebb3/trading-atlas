# Zipline — original Quantopian project — Which slippage model actually limits historical fill volume

**Decision question:** Which slippage model actually limits historical fill volume?

| Field | Review |
| --- | --- |
| Upstream | [Zipline — original Quantopian project](https://github.com/quantopian/zipline) |
| Primary area | Backtesting & Simulation |
| Source commit | [014f1fc339dc8b7671d29be2d85ce57d3daec343](https://github.com/quantopian/zipline/commit/014f1fc339dc8b7671d29be2d85ce57d3daec343) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/quantopian/zipline/blob/014f1fc339dc8b7671d29be2d85ce57d3daec343/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Contrasts volume-limited impact with unconstrained fixed-spread fills. A historical execution-model reference whose original packaging is dated. |

## Project overview

Original event-driven Python backtesting library with data bundles and pluggable execution models. [Project documentation](https://github.com/quantopian/zipline/blob/014f1fc339dc8b7671d29be2d85ce57d3daec343/README.rst#L16-L21).

## Mechanism worth inspecting

VolumeShareSlippage caps total fill volume per bar, deducts already consumed volume and moves price with squared volume share. FixedSlippage instead applies a fixed spread and does not impose size limits. [Volume model](https://github.com/quantopian/zipline/blob/014f1fc339dc8b7671d29be2d85ce57d3daec343/zipline/finance/slippage.py#L291-L338), [fixed model](https://github.com/quantopian/zipline/blob/014f1fc339dc8b7671d29be2d85ce57d3daec343/zipline/finance/slippage.py#L341-L374), [bundles](https://github.com/quantopian/zipline/blob/014f1fc339dc8b7671d29be2d85ce57d3daec343/docs/source/bundles.rst#L58-L65).

## Important limit

A model choice can remove liquidity constraints entirely. The inspected original README targets obsolete Python versions; treat this repository as historical source rather than assuming its old deployment claims describe today's maintained tooling. [Version scope](https://github.com/quantopian/zipline/blob/014f1fc339dc8b7671d29be2d85ce57d3daec343/README.rst#L42-L48).

## Questions to take into your own design

- Which slippage model actually limits historical fill volume?
- Can two orders consume more liquidity than the shared per-bar volume allowance?

## Why this score for a trading system

3/5: direct and inspectable liquidity-accounting examples, with old runtime assumptions and no venue-specific validation here.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
