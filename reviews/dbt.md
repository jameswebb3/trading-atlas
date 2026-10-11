# dbt: protect a freshness receipt from an empty selection

**Decision question:** Can an empty freshness selection overwrite useful prior evidence?

| Field | Review |
| --- | --- |
| Upstream | [dbt-labs/dbt](https://github.com/dbt-labs/dbt) |
| Primary area | Data Quality & Lineage |
| Source commit | [7e4e937c4eef07e3837960507dea46c15c1db42b](https://github.com/dbt-labs/dbt/commit/7e4e937c4eef07e3837960507dea46c15c1db42b) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/dbt-labs/dbt/blob/7e4e937c4eef07e3837960507dea46c15c1db42b/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Guards the source-freshness artifact against replacement by a model-only run with no selected sources. The source-only command still writes an empty artifact, and newest-row freshness does not prove interior feed coverage. |

## Mechanism worth inspecting

The [overview](https://github.com/dbt-labs/dbt/blob/7e4e937c4eef07e3837960507dea46c15c1db42b/README.md#L12-L24) frames dbt as a transformation system that produces queryable artifacts. Its [freshness documentation](https://docs.getdbt.com/reference/resource-configs/freshness) defines warning and error thresholds. In the pinned implementation, the unified freshness command [writes sources.json only when the selection includes sources](https://github.com/dbt-labs/dbt/blob/7e4e937c4eef07e3837960507dea46c15c1db42b/crates/dbt-main/src/freshness.rs#L61-L100). The code comment explains why: a model-only run could replace a meaningful source result with an empty artifact. The [fixture](https://github.com/dbt-labs/dbt/blob/7e4e937c4eef07e3837960507dea46c15c1db42b/crates/dbt-sa-python/tests/integration/fixtures/freshness/models/_sources.yml#L3-L20) shows distinct warning and error thresholds.

For trading-data receipts, an inapplicable check should not silently replace the last applicable result. The retained receipt still needs its original run ID and timestamp.

## Important limit

The same branch explicitly writes sources.json for the source-only command even when its result is empty. The [threshold evaluator](https://github.com/dbt-labs/dbt/blob/7e4e937c4eef07e3837960507dea46c15c1db42b/crates/dbt-freshness/src/freshness.rs#L153-L177) classifies age, but a recent maximum timestamp does not establish per-symbol coverage or absence of interior gaps.

## Questions to take into your own design

- Can an empty verification overwrite a meaningful prior receipt?
- Is a retained receipt labeled with its original run and time?
- Are newest-row freshness and interval completeness checked separately?

## Why this score for a trading system

The artifact guard is a transferable data-quality pattern for trading pipelines, but the inspected freshness workflow is not trading-specific.

**Scope of this review:** We read the pinned overview, documentation, fixture, and selected implementation. We did not install or run dbt, inspect every adapter, or establish later-commit behavior.
