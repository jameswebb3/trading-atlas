# Data Lineage Parent - Can parsed SQL show column-level data dependencies?

**Decision question:** Can parsed SQL show column-level data dependencies?

| Field | Review |
| --- | --- |
| Upstream | [thestyleofme/data-lineage-parent](https://github.com/thestyleofme/data-lineage-parent) |
| Primary area | Data Quality & Lineage |
| Source commit | [16fd3b14caafdb8ecd506f7d9ead5780ae11a2bf](https://github.com/thestyleofme/data-lineage-parent/commit/16fd3b14caafdb8ecd506f7d9ead5780ae11a2bf) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its HiveQL parser builds table and column lineage from statement syntax. Static Hive parsing does not cover Python transformations, dynamic SQL or runtime source revisions in a trading pipeline. |

## What this project does

A Hive-oriented data lineage hook.

## Mechanism inspected

Its HiveQL parser builds table and column lineage from statement syntax.

## Limitation that matters

Static Hive parsing does not cover Python transformations, dynamic SQL or runtime source revisions in a trading pipeline.

## Practical check for a trading system

Record both parsed dependencies and runtime dataset IDs with availability clocks.

## Why this score

2/5. The parser demonstrates lineage extraction, with a narrow language and runtime boundary.

## Source trail

[README](https://github.com/thestyleofme/data-lineage-parent/blob/16fd3b14caafdb8ecd506f7d9ead5780ae11a2bf/README.md#L1); [lineage-hooks/lineage-hive-hook/src/main/java/org/isaac/lineage/hook/hive/lineage/LineageParser.java](https://github.com/thestyleofme/data-lineage-parent/blob/16fd3b14caafdb8ecd506f7d9ead5780ae11a2bf/lineage-hooks/lineage-hive-hook/src/main/java/org/isaac/lineage/hook/hive/lineage/LineageParser.java#L30).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
