# TimescaleDB — Which buckets did a successful aggregate refresh actually rebuild

**Decision question:** Which buckets did a successful aggregate refresh actually rebuild?

| Field | Review |
| --- | --- |
| Upstream | [TimescaleDB](https://github.com/timescale/timescaledb) |
| Primary area | Data Quality & Lineage |
| Source commit | [83699ebf0a37f95826d18df406f969e536684820](https://github.com/timescale/timescaledb/commit/83699ebf0a37f95826d18df406f969e536684820) |
| Reviewed | 2026-09-26 |
| Declared license | [Mixed Apache-2.0 and Timescale License; inspected refresh code under TSL](https://github.com/timescale/timescaledb/blob/83699ebf0a37f95826d18df406f969e536684820/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A practical time-series storage reference for explicit aggregation boundaries. Refresh windows select complete buckets, so data arrival, late corrections and retained source coverage need separate checks. |

## Project overview

TimescaleDB extends PostgreSQL for time-series data, including tick aggregation and continuous aggregates. [Project documentation](https://github.com/timescale/timescaledb/blob/83699ebf0a37f95826d18df406f969e536684820/docs/getting-started/financial-ticks/README.md#L1-L16).

## Mechanism worth inspecting

The refresh code shrinks a requested interval to fully enclosed buckets. It documents why partial buckets are excluded when retention may have removed part of their source data. [Refresh-window contract](https://github.com/timescale/timescaledb/blob/83699ebf0a37f95826d18df406f969e536684820/tsl/src/continuous_aggs/refresh.c#L145-L218).

## Important limit

A completed refresh does not mean every requested boundary bucket was rebuilt or all upstream ticks had arrived. The inspected aggregate code uses the Timescale License, distinct from Apache-licensed components. [License split](https://github.com/timescale/timescaledb/blob/83699ebf0a37f95826d18df406f969e536684820/LICENSE#L1-L16).

## Questions to take into your own design

- Which buckets did a successful aggregate refresh actually rebuild?
- What interval was actually refreshed, and which late corrections remain outside it?

## Why this score for a trading system

3/5: directly relevant financial time-series aggregation, with concrete boundary semantics; mixed licensing and broader storage behavior require separate assessment.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
