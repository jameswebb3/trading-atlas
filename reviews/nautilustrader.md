# NautilusTrader: Do not infer depth or queue behavior from bars

**Decision question:** Which execution assumptions follow from the granularity of the replayed feed?

| Field | Review |
| --- | --- |
| Upstream | [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) |
| Primary area | Backtesting & Simulation |
| Source commit | [f95360d2d84e7fe47b07ba1ebd228fbd43382d25](https://github.com/nautechsystems/nautilus_trader/commit/f95360d2d84e7fe47b07ba1ebd228fbd43382d25) |
| Reviewed | 2026-09-25 |
| Declared license | [LGPL-3.0](https://github.com/nautechsystems/nautilus_trader/blob/f95360d2d84e7fe47b07ba1ebd228fbd43382d25/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Makes the simulated venue book type explicit and rejects unsupported time-in-force paths. Bars cannot reveal intrabar order, spread, depth, or queue position; a deterministic replay can still be unrealistic. |

## Mechanism worth inspecting

The backtesting guide orders L3, L2, quotes, trades, and bars by available execution detail and states that the venue book type selects which data updates matching state. The matching engine also rejects unsupported at-open/at-close time-in-force requests rather than silently treating them as another order type.

**Source trail:** [project overview](https://github.com/nautechsystems/nautilus_trader/blob/f95360d2d84e7fe47b07ba1ebd228fbd43382d25/README.md) · [documentation](https://github.com/nautechsystems/nautilus_trader/blob/f95360d2d84e7fe47b07ba1ebd228fbd43382d25/docs/concepts/backtesting/data-and-venues.md#L3-L47) · [implementation](https://github.com/nautechsystems/nautilus_trader/blob/f95360d2d84e7fe47b07ba1ebd228fbd43382d25/crates/execution/src/matching_engine/mod.rs#L3525-L3537) · [additional source](https://github.com/nautechsystems/nautilus_trader/blob/f95360d2d84e7fe47b07ba1ebd228fbd43382d25/docs/concepts/backtesting/fill-prices-and-matching.md#L1-L11).

## Important limit

The documentation itself says recorded depth cannot show the market impact of a simulated order. Matching rules are therefore assumptions, not evidence that a given live order would have filled.

## Questions to take into your own design

- Is every fill claim labeled with the data granularity that supports it?
- Do unsupported order semantics fail explicitly in simulation?

## Why this score for a trading system

Book-type and data-granularity rules directly bound fill claims in trading backtests; market impact remains unobservable in replay.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
