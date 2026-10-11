# lakebridge - Count reconciliation failures before sampling them

**Decision question:** Does a short mismatch report hide the scale of divergence?

| Field | Review |
| --- | --- |
| Upstream | [databrickslabs/lakebridge](https://github.com/databrickslabs/lakebridge) |
| Primary area | Data Quality & Lineage |
| Source commit | [b9cfdf3a466091f00fa14adcaacd0ad7afd9b0b8](https://github.com/databrickslabs/lakebridge/commit/b9cfdf3a466091f00fa14adcaacd0ad7afd9b0b8) |
| Reviewed | 2026-10-10 |
| Declared license | Databricks License (custom) ([source](https://github.com/databrickslabs/lakebridge/blob/b9cfdf3a466091f00fa14adcaacd0ad7afd9b0b8/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | reconcile_data uses a full outer join, counts rows missing on each side and mismatched hashes, then limits only the displayed example rows. This is Spark/Databricks-oriented and the root license is the Databricks License; adapt the pattern, do not adopt the package. |

## What this project does

A Databricks migration tool reconciles source and target datasets and reports key-level differences. [README](https://github.com/databrickslabs/lakebridge/blob/b9cfdf3a466091f00fa14adcaacd0ad7afd9b0b8/README.md).

## Mechanism inspected

reconcile_data uses a full outer join, counts rows missing on each side and mismatched hashes, then limits only the displayed example rows. [Implementation](https://github.com/databrickslabs/lakebridge/blob/b9cfdf3a466091f00fa14adcaacd0ad7afd9b0b8/src/databricks/labs/lakebridge/reconcile/compare.py#L57-L124).

## Limitation that matters

This is Spark/Databricks-oriented and the root license is the Databricks License; adapt the pattern, do not adopt the package. This conclusion is limited to the inspected path at the pinned commit.

## Practical check for a trading system

For producer-versus-replay and backfill comparisons, report full mismatch counts and denominators separately from the bounded example list.

## Why this score

reconcile_data uses a full outer join, counts rows missing on each side and mismatched hashes, then limits only the displayed example rows. This is Spark/Databricks-oriented and the root license is the Databricks License; adapt the pattern, do not adopt the package.

## Source trail

[README](https://github.com/databrickslabs/lakebridge/blob/b9cfdf3a466091f00fa14adcaacd0ad7afd9b0b8/README.md) - [Implementation](https://github.com/databrickslabs/lakebridge/blob/b9cfdf3a466091f00fa14adcaacd0ad7afd9b0b8/src/databricks/labs/lakebridge/reconcile/compare.py#L57-L124) - [License](https://github.com/databrickslabs/lakebridge/blob/b9cfdf3a466091f00fa14adcaacd0ad7afd9b0b8/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
