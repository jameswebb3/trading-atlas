# dbt-superset-lineage — A parser fallback can weaken lineage without failing

**Decision question:** What happens when SQL lineage extraction fails to parse a dashboard query?

| Field | Review |
| --- | --- |
| Upstream | [slidoapp/dbt-superset-lineage](https://github.com/slidoapp/dbt-superset-lineage) |
| Primary area | Data Quality & Lineage |
| Source commit | [7e5cd202c1aaa916df5f52d6604eafaacd7dfd87](https://github.com/slidoapp/dbt-superset-lineage/commit/7e5cd202c1aaa916df5f52d6604eafaacd7dfd87) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/slidoapp/dbt-superset-lineage/blob/7e5cd202c1aaa916df5f52d6604eafaacd7dfd87/LICENSE.md)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Dashboard extraction tries SQLFluff, logs a warning on parse failure and falls back to regex before matching schema-and-name keys in a dbt manifest. The fallback can infer less reliable dependencies while the pipeline continues; table lineage is not row-level or publication-time lineage. |

## What this project does

Links Superset dashboards to dbt models by parsing SQL and matching manifest tables. [README](https://github.com/slidoapp/dbt-superset-lineage/blob/7e5cd202c1aaa916df5f52d6604eafaacd7dfd87/README.md).

## Mechanism inspected

Dashboard extraction tries SQLFluff, logs a warning on parse failure and falls back to regex before matching schema-and-name keys in a dbt manifest. [Implementation](https://github.com/slidoapp/dbt-superset-lineage/blob/7e5cd202c1aaa916df5f52d6604eafaacd7dfd87/dbt_superset_lineage/pull_dashboards.py#L58-L106).

## Limitation that matters

The fallback can infer less reliable dependencies while the pipeline continues; table lineage is not row-level or publication-time lineage. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Record parser mode and confidence for each inferred lineage edge; block decisions that require exact provenance when fallback was used.

## Why this score

Dashboard extraction tries SQLFluff, logs a warning on parse failure and falls back to regex before matching schema-and-name keys in a dbt manifest. The fallback can infer less reliable dependencies while the pipeline continues; table lineage is not row-level or publication-time lineage.

## Source trail

[README](https://github.com/slidoapp/dbt-superset-lineage/blob/7e5cd202c1aaa916df5f52d6604eafaacd7dfd87/README.md) · [Implementation](https://github.com/slidoapp/dbt-superset-lineage/blob/7e5cd202c1aaa916df5f52d6604eafaacd7dfd87/dbt_superset_lineage/pull_dashboards.py#L58-L106) · [License](https://github.com/slidoapp/dbt-superset-lineage/blob/7e5cd202c1aaa916df5f52d6604eafaacd7dfd87/LICENSE.md).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
