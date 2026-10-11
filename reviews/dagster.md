# Dagster: Freshness needs a deadline and a reason

**Decision question:** Is a data asset current enough for the decision that uses it?

| Field | Review |
| --- | --- |
| Upstream | [dagster-io/dagster](https://github.com/dagster-io/dagster) |
| Primary area | Operations & Observability |
| Source commit | [0b3bc29879ee28089be8fddb0dc5ac1d302f5dff](https://github.com/dagster-io/dagster/commit/0b3bc29879ee28089be8fddb0dc5ac1d302f5dff) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/dagster-io/dagster/blob/0b3bc29879ee28089be8fddb0dc5ac1d302f5dff/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Checks an asset’s last update against a computed lower bound and records the threshold and observed timestamp. A recent update can still coexist with missing interior observations or stale values inside the asset. |

## Project overview

Data orchestrator organized around assets such as datasets, models, and reports. Combines scheduling, lineage, and freshness checks to show how research inputs are produced and updated.

[Project documentation](https://github.com/dagster-io/dagster/blob/0b3bc29879ee28089be8fddb0dc5ac1d302f5dff/python_modules/dagster/README.md#L31-L35).

## Mechanism worth inspecting

The freshness guide defines a scheduled check. The implementation calculates a last-update lower bound, compares the latest record timestamp, and emits metadata with the bound, observed update, and fresh-until time. Those fields make a freshness verdict explainable.

**Source trail:** [project overview](https://github.com/dagster-io/dagster/blob/0b3bc29879ee28089be8fddb0dc5ac1d302f5dff/README.md) · [documentation](https://github.com/dagster-io/dagster/blob/0b3bc29879ee28089be8fddb0dc5ac1d302f5dff/docs/docs/guides/test/data-freshness-testing.md#L12-L38) · [implementation](https://github.com/dagster-io/dagster/blob/0b3bc29879ee28089be8fddb0dc5ac1d302f5dff/python_modules/dagster/dagster/_core/definitions/asset_checks/asset_check_factories/freshness_checks/last_update.py#L195-L240).

## Important limit

Last-update freshness is not continuity, completeness, or publication-time correctness. A newly materialized incomplete partition can pass unless the pipeline adds those checks.

## Questions to take into your own design

- Does each freshness verdict include the deadline and observed timestamp?
- Are interior gaps checked independently of last update?

## Why this score for a trading system

Freshness receipts with thresholds and timestamps help operational data gates, but a recent incomplete trading feed can pass.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
