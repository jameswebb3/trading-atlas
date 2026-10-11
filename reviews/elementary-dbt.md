# Elementary dbt: detect restatements of settled history

**Decision question:** Can a historical aggregate change after it was treated as settled without triggering a review?

| Field | Review |
| --- | --- |
| Upstream | [Elementary dbt package](https://github.com/elementary-data/dbt-data-reliability) |
| Primary area | Data Quality & Lineage |
| Source commit | [5d22e8d9a43e9175a7132886141fdcf59c1f1349](https://github.com/elementary-data/dbt-data-reliability/commit/5d22e8d9a43e9175a7132886141fdcf59c1f1349) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/elementary-data/dbt-data-reliability/blob/5d22e8d9a43e9175a7132886141fdcf59c1f1349/LICENSE) |
| Review depth | 3/3: README, documented macro contract, comparison SQL and integration-test source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Stores dbt metadata, run evidence, and quality metrics. Its stability check compares settled time buckets against prior and first retained measurements, detecting both sudden rewrites and accumulated drift within the rescanned window. |

## Project overview

A dbt package captures run artifacts in warehouse tables and provides native quality and anomaly checks, including metric stability. [Project documentation](https://github.com/elementary-data/dbt-data-reliability/blob/5d22e8d9a43e9175a7132886141fdcf59c1f1349/README.md#L20-L35).

## Mechanism worth inspecting

The [stability query](https://github.com/elementary-data/dbt-data-reliability/blob/5d22e8d9a43e9175a7132886141fdcf59c1f1349/macros/edr/data_monitoring/monitors_query/metric_stability_query.sql#L25-L53) restricts baselines to measurements taken after settling. [Versioned comparison](https://github.com/elementary-data/dbt-data-reliability/blob/5d22e8d9a43e9175a7132886141fdcf59c1f1349/macros/edr/data_monitoring/monitors_query/metric_stability_query.sql#L124-L162) retains previous and first measurements. [Scan-window restrictions](https://github.com/elementary-data/dbt-data-reliability/blob/5d22e8d9a43e9175a7132886141fdcf59c1f1349/macros/edr/data_monitoring/monitors_query/metric_stability_query.sql#L97-L108) prevent unscanned history from being declared missing. The [first-baseline test](https://github.com/elementary-data/dbt-data-reliability/blob/5d22e8d9a43e9175a7132886141fdcf59c1f1349/integration_tests/tests/test_metric_stability.py#L127-L137) addresses drift too small to trigger any single-step comparison.

## Important limit

The check operates inside a configured observation and retention window. Its [missing-bucket tests](https://github.com/elementary-data/dbt-data-reliability/blob/5d22e8d9a43e9175a7132886141fdcf59c1f1349/integration_tests/tests/test_metric_stability.py#L399-L447) distinguish disappearance from off-window or unscanned data. It can reveal restatement, not certify that either version was correct or available to a historical trader.

## Questions to take into your own design

- Does an experiment record the exact metric vintage it used before a provider revision?
- Are first-publication and previous-check comparisons retained alongside a settling policy?

## Why this score for a trading system

3/5: a concrete transferable method for detecting silent historical revisions, with relevant edge-case test source. Deployment is dbt/warehouse-specific and historical correctness still needs separate evidence.

**Scope of this review:** README, stability macro contract, baseline/window comparison SQL, and selected restatement/disappearance integration-test source.
