# databricks-dbt-factory - Block runtime flags that change a manifest-derived plan

**Decision question:** Can a run silently select different tasks than the plan that was reviewed?

| Field | Review |
| --- | --- |
| Upstream | [mwojtyczka/databricks-dbt-factory](https://github.com/mwojtyczka/databricks-dbt-factory) |
| Primary area | Research & Reproducibility |
| Source commit | [006f45826e06e391e50129251f672af340b682b3](https://github.com/mwojtyczka/databricks-dbt-factory/commit/006f45826e06e391e50129251f672af340b682b3) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/mwojtyczka/databricks-dbt-factory/blob/006f45826e06e391e50129251f672af340b682b3/LICENSE.txt)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Before constructing commands, it rejects dbt selection flags, parse-context overrides and dynamic references that could change the resource selected by a factory-owned task. It also constrains the target option to its intended position. This guards runtime options after a manifest exists; it cannot establish that the manifest, source data or task results were correct. The full execution stack depends on dbt and Databricks. |

## What this project does

Databricks dbt factory turns a dbt manifest into task-level Databricks jobs. [README](https://github.com/mwojtyczka/databricks-dbt-factory/blob/006f45826e06e391e50129251f672af340b682b3/README.md).

## Mechanism inspected

Before constructing commands, it rejects dbt selection flags, parse-context overrides and dynamic references that could change the resource selected by a factory-owned task. It also constrains the target option to its intended position. [Implementation](https://github.com/mwojtyczka/databricks-dbt-factory/blob/006f45826e06e391e50129251f672af340b682b3/src/databricks_dbt_factory/task_factory.py#L100-L156). [Related path](https://github.com/mwojtyczka/databricks-dbt-factory/blob/006f45826e06e391e50129251f672af340b682b3/src/databricks_dbt_factory/task_factory.py#L273-L296).

## Limitation that matters

This guards runtime options after a manifest exists; it cannot establish that the manifest, source data or task results were correct. The full execution stack depends on dbt and Databricks. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

After preregistration, explicitly reject command-line or environment overrides that could change the asset universe, split, time window or objective under the same run identifier.

## Why this score

It offers a narrow, testable boundary between a reviewed plan and runtime invocation without requiring the upstream platform.

## Source trail

[README](https://github.com/mwojtyczka/databricks-dbt-factory/blob/006f45826e06e391e50129251f672af340b682b3/README.md) - [Implementation](https://github.com/mwojtyczka/databricks-dbt-factory/blob/006f45826e06e391e50129251f672af340b682b3/src/databricks_dbt_factory/task_factory.py#L100-L156) - [Related path](https://github.com/mwojtyczka/databricks-dbt-factory/blob/006f45826e06e391e50129251f672af340b682b3/src/databricks_dbt_factory/task_factory.py#L273-L296) - [License](https://github.com/mwojtyczka/databricks-dbt-factory/blob/006f45826e06e391e50129251f672af340b682b3/LICENSE.txt).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
