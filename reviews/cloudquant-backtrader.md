# Backtrader — cloudQuant fork — What queue assumption supports a simulated maker fill

**Decision question:** What queue assumption supports a simulated maker fill?

| Field | Review |
| --- | --- |
| Upstream | [Backtrader — cloudQuant fork](https://github.com/cloudQuant/backtrader) |
| Primary area | Backtesting & Simulation |
| Source commit | [7196567284af97b536a7f8d8b817fce70554b330](https://github.com/cloudQuant/backtrader/commit/7196567284af97b536a7f8d8b817fce70554b330) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-3.0](https://github.com/cloudQuant/backtrader/blob/7196567284af97b536a7f8d8b817fce70554b330/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Exposes alternative maker-fill assumptions inside a Backtrader fork. Inspect queue initialization and missing-level behavior before using simulated fills as execution evidence. |

## Project overview

Performance-oriented Backtrader fork with event-driven and vectorized paths plus broker and HFT simulation components. [Project documentation](https://github.com/cloudQuant/backtrader/blob/7196567284af97b536a7f8d8b817fce70554b330/docs/ARCHITECTURE.md#L6-L31).

## Mechanism worth inspecting

The HFT broker exposes both a no-queue model and a probabilistic model initialized from displayed size at the order's price. The no-queue path caps fillable volume by the trade but assigns zero volume ahead. [Queue models](https://github.com/cloudQuant/backtrader/blob/7196567284af97b536a7f8d8b817fce70554b330/backtrader/brokers/hft/queue.py#L10-L35), [queue initialization](https://github.com/cloudQuant/backtrader/blob/7196567284af97b536a7f8d8b817fce70554b330/backtrader/brokers/hft/queue.py#L82-L126).

## Important limit

A probabilistic queue estimate is not observed order priority. Missing price levels yield zero queue ahead in the inspected initializer, which needs explicit treatment in any sparse-book dataset. [Fallback](https://github.com/cloudQuant/backtrader/blob/7196567284af97b536a7f8d8b817fce70554b330/backtrader/brokers/hft/queue.py#L101-L108).

## Questions to take into your own design

- What queue assumption supports a simulated maker fill?
- What queue state is assigned when the order's price level is missing?

## Why this score for a trading system

3/5: concrete market-replay logic, but its queue assumptions need venue-specific calibration and the fork adds substantial implementation surface.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
