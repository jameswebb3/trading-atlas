# DuckDB — Does an ASOF join imply that the matched data was already published

**Decision question:** Does an ASOF join imply that the matched data was already published?

| Field | Review |
| --- | --- |
| Upstream | [DuckDB](https://github.com/duckdb/duckdb) |
| Primary area | Data Quality & Lineage |
| Source commit | [d8a1bd4f4fbccdf3d22d8f1fe27a94c11c805d0a](https://github.com/duckdb/duckdb/commit/d8a1bd4f4fbccdf3d22d8f1fe27a94c11c805d0a) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/duckdb/duckdb/blob/d8a1bd4f4fbccdf3d22d8f1fe27a94c11c805d0a/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and tests read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful analytical reference for timestamp alignment and local data queries. ASOF matches the timestamp contract you supply; historical availability and maximum staleness must be expressed separately. |

## Project overview

DuckDB is an analytical SQL database with local file queries and ASOF joins useful for aligning timestamped datasets. [Project documentation](https://github.com/duckdb/duckdb/blob/d8a1bd4f4fbccdf3d22d8f1fe27a94c11c805d0a/README.md#L16-L35).

## Mechanism worth inspecting

The ASOF planner describes at-most-one matching build row per probe row. Timestamp tests show a backward inequality carrying the latest eligible event forward. [Planner](https://github.com/duckdb/duckdb/blob/d8a1bd4f4fbccdf3d22d8f1fe27a94c11c805d0a/src/execution/physical_plan/plan_asof_join.cpp#L43-L60), [timestamp test read](https://github.com/duckdb/duckdb/blob/d8a1bd4f4fbccdf3d22d8f1fe27a94c11c805d0a/test/sql/join/asof/test_asof_join_timestamps.test#L50-L65).

## Important limit

Eligibility follows the supplied predicate. Joining on event time alone does not constrain publication or receipt time, and without an age bound the last observation can be carried forward indefinitely.

## Questions to take into your own design

- Does an ASOF join imply that the matched data was already published?
- Which availability timestamp and maximum age qualify an ASOF match?

## Why this score for a trading system

3/5: concrete transferable join semantics and an inspected test, but SQL cannot infer trading-data availability from event time.

**Scope of this review:** Focused reading of the linked documentation and implementation plus cited tests (read, not executed). Other subsystems and runtime behavior were not assessed.
