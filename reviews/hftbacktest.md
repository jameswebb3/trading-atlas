# HftBacktest: Validate exchange and local event clocks independently

**Decision question:** Can a feed look ordered in one clock while being disordered in another?

| Field | Review |
| --- | --- |
| Upstream | [nkaz001/hftbacktest](https://github.com/nkaz001/hftbacktest) |
| Primary area | Backtesting & Simulation |
| Source commit | [5f3ec40b2afb764e0fea112f941ed85523ef4e88](https://github.com/nkaz001/hftbacktest/commit/5f3ec40b2afb764e0fea112f941ed85523ef4e88) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Rejects decreasing exchange timestamps and decreasing local timestamps on their respective event streams. Clock monotonicity does not prove no events are missing, and queue models still assume no market impact. |

## Project overview

Market replay backtester for high-frequency and market-making strategies. Models feed latency, order latency, and queue position using order-book and trade data.

[Project documentation](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/README.rst#L7-L21).

## Mechanism worth inspecting

The validation function selects exchange and local events separately and raises if timestamps go backward in either subset. Its discrepancy guide also calls out queue calibration and the no-market-impact assumption. The two-clock check is a useful precondition for event replay.

**Source trail:** [project overview](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/README.rst) · [documentation](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/docs/debugging_backtesting_and_live_discrepancies.rst#L20-L35) · [implementation](https://github.com/nkaz001/hftbacktest/blob/5f3ec40b2afb764e0fea112f941ed85523ef4e88/py-hftbacktest/hftbacktest/data/validation.py#L139-L152).

## Important limit

A monotonic stream can have gaps, duplicate IDs, or late publications. The simulator’s queue assumptions still need comparison with venue evidence.

## Questions to take into your own design

- Are exchange and receipt clocks validated separately before replay?
- Is an ordered-but-incomplete event stream marked unusable for fill-sensitive tests?

## Why this score for a trading system

Separating exchange and local event-order checks directly improves market replay; monotonic clocks still cannot prove completeness.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
