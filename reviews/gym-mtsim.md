# Missing timestamps need an explicit boundary rule before price lookup

**Decision question:** What price is selected when simulation time is outside the data range?

| Field | Review |
| --- | --- |
| Upstream | [gym-mtsim](https://github.com/AminHP/gym-mtsim) |
| Primary area | Backtesting & Simulation |
| Source commit | [1131a4becaf8a9459dfaa728d5547f81a724b070](https://github.com/AminHP/gym-mtsim/commit/1131a4becaf8a9459dfaa728d5547f81a724b070) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/AminHP/gym-mtsim/blob/1131a4becaf8a9459dfaa728d5547f81a724b070/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The simulator uses a pandas index lookup to find an earlier timestamp, then directly indexes the returned position without a missing-position guard. That before-first-data boundary deserves an explicit regression. Its fee parameter represents an assumed spread, not a complete perpetual-futures cost model. |

## Mechanism worth inspecting

The [README](https://github.com/AminHP/gym-mtsim/blob/1131a4becaf8a9459dfaa728d5547f81a724b070/README.md#L3-L7) describes a MetaTrader-style simulator, and its [fee documentation](https://github.com/AminHP/gym-mtsim/blob/1131a4becaf8a9459dfaa728d5547f81a724b070/README.md#L57-L59) explains the spread proxy. The [price lookup](https://github.com/AminHP/gym-mtsim/blob/1131a4becaf8a9459dfaa728d5547f81a724b070/gym_mtsim/simulator/mt_simulator.py#L96-L109) uses get_indexer with forward-fill and directly selects df.index[i], then retrieves the row.

## Important limit

We did not run the lookup or reproduce a boundary failure. The source lacks an explicit missing-position guard in this helper. Bar-close prices, spread proxies, stop-out assumptions, and MetaTrader leverage are not proof of Hyperliquid margin or funding behavior.

## Questions to take into your own design

- Does a query before the first observation fail instead of selecting a row?
- Can a stale earlier bar be accepted indefinitely during a gap?

## Why this score for a trading system

2/5: Timestamp-boundary auditing is a useful direct simulation caution, while the market and cost assumptions require substantial adaptation.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
