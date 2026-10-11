# Zipline Reloaded: a bundle timestamp that the loader does not enforce

**Decision question:** Does a historical data-vintage option actually exclude later ingestions?

| Field | Review |
| --- | --- |
| Upstream | [Zipline Reloaded](https://github.com/stefan-jansen/zipline-reloaded) |
| Primary area | Backtesting & Simulation |
| Source commit | [943010b9da848e317fc520de87edade2b884d329](https://github.com/stefan-jansen/zipline-reloaded/commit/943010b9da848e317fc520de87edade2b884d329) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/stefan-jansen/zipline-reloaded/blob/943010b9da848e317fc520de87edade2b884d329/LICENSE) |
| Review depth | 2/3: documentation, loader, and relevant tests read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The guide says a bundle timestamp loads the last ingestion at or before that time. At this commit the loader passes the timestamp to a selector that chooses the latest visible directory without filtering by it. A vintage setting therefore cannot be trusted from the documented interface alone. |

## Project overview

Python event-driven backtesting engine with historical data bundles and pandas-based inputs and outputs. A reference for organizing strategy simulations, data ingestion, and performance analysis.

[Project documentation](https://github.com/stefan-jansen/zipline-reloaded/blob/943010b9da848e317fc520de87edade2b884d329/README.md#L14-L24).

## Mechanism worth inspecting

The [bundle guide](https://github.com/stefan-jansen/zipline-reloaded/blob/943010b9da848e317fc520de87edade2b884d329/docs/source/bundles.rst#L98-L113) promises an as-of ingestion cutoff. In [load](https://github.com/stefan-jansen/zipline-reloaded/blob/943010b9da848e317fc520de87edade2b884d329/src/zipline/data/bundles/core.py#L535-L558), the requested timestamp reaches most_recent_data. That function [lists all visible ingestion directories and takes their maximum](https://github.com/stefan-jansen/zipline-reloaded/blob/943010b9da848e317fc520de87edade2b884d329/src/zipline/data/bundles/core.py#L494-L533); its timestamp argument is never used in the selection. The [bundle tests](https://github.com/stefan-jansen/zipline-reloaded/blob/943010b9da848e317fc520de87edade2b884d329/tests/data/bundles/test_core.py#L332-L344) create distinct ingestion times but inspect the latest directory, while the [missing-data test](https://github.com/stefan-jansen/zipline-reloaded/blob/943010b9da848e317fc520de87edade2b884d329/tests/data/bundles/test_core.py#L366-L373) checks only the empty case.

## Important limit

This is a source-level finding at the pinned commit, not an executed reproduction. An ingestion timestamp is also a dataset-vintage boundary, not proof that every observation in the bundle was published before each trading decision. Zipline's equity-oriented data model is not a Hyperliquid perpetual simulator.

## Questions to take into your own design

- Can a test request an old data snapshot and prove that a newer snapshot is rejected?
- Does the selected snapshot preserve per-observation publication and correction times?
- Is a documentation promise backed by an adversarial test with both older and newer ingestions?

## Why this score for a trading system

The as-of mismatch is a valuable direct backtest warning, but the documented vintage mechanism is broken in the inspected loader and was not runtime-tested.

**Scope of this review:** We read the README, bundle guide, selection code, and selected tests at the pinned commit. We did not run Zipline or audit every data reader.
