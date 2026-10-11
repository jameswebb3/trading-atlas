# spark-sql-flow-plugin — Logical plans expose column dependencies

**Decision question:** Can a derived column be tied to its source attributes?

| Field | Review |
| --- | --- |
| Upstream | [spark-sql-flow-plugin](https://github.com/maropu/spark-sql-flow-plugin) |
| Primary area | Data Quality & Lineage |
| Source commit | [57d9db75d544706f1693d9a06a9202fc96e64b3e](https://github.com/maropu/spark-sql-flow-plugin/commit/57d9db75d544706f1693d9a06a9202fc96e64b3e) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/maropu/spark-sql-flow-plugin/blob/57d9db75d544706f1693d9a06a9202fc96e64b3e/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The collector traverses logical-plan expressions and reference attributes to build graph edges. Spark lineage cannot prove receipt time or source-file identity, and Spark itself is not required for the current pipeline. |

## What this project does

A Spark SQL plugin that walks analyzed plans to build table and column lineage graphs. [README](https://github.com/maropu/spark-sql-flow-plugin/blob/57d9db75d544706f1693d9a06a9202fc96e64b3e/README.md).

## Mechanism inspected

The collector traverses logical-plan expressions and reference attributes to build graph edges. [Implementation](https://github.com/maropu/spark-sql-flow-plugin/blob/57d9db75d544706f1693d9a06a9202fc96e64b3e/src/main/scala/org/apache/spark/sql/flow/SQLFlow.scala#L42-L99).

## Limitation that matters

Spark lineage cannot prove receipt time or source-file identity, and Spark itself is not required for the current pipeline. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Record input columns and transform version for derived features if absent from existing receipts.

## Why this score

Transferable engineering pattern: The collector traverses logical-plan expressions and reference attributes to build graph edges. Spark lineage cannot prove receipt time or source-file identity, and Spark itself is not required for the current pipeline.

## Source trail

[README](https://github.com/maropu/spark-sql-flow-plugin/blob/57d9db75d544706f1693d9a06a9202fc96e64b3e/README.md) · [Implementation](https://github.com/maropu/spark-sql-flow-plugin/blob/57d9db75d544706f1693d9a06a9202fc96e64b3e/src/main/scala/org/apache/spark/sql/flow/SQLFlow.scala#L42-L99).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
