# linesql - Keep one lineage result per SQL statement

**Decision question:** Which statement in a multi-statement transform failed to yield trustworthy lineage?

| Field | Review |
| --- | --- |
| Upstream | [jarredhj0214/linesql](https://github.com/jarredhj0214/linesql) |
| Primary area | Data Quality & Lineage |
| Source commit | [4f122a1dc29282af8fed163be044b0e1cdaf468e](https://github.com/jarredhj0214/linesql/commit/4f122a1dc29282af8fed163be044b0e1cdaf468e) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/jarredhj0214/linesql/blob/4f122a1dc29282af8fed163be044b0e1cdaf468e/LICENSE)) |
| Review depth | 2/3: README, documentation where present and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | It splits a script, selects a dialect per statement, and returns a LineageResult for each; a missing parser produces an explicit DIALECT_NOT_REGISTERED error with confidence and detection reason attached. Dialect detection is heuristic and static parsing cannot prove that a statement executed or that dynamically generated SQL matches the text analyzed. |

## What this project does

LineSQL parses several SQL dialects into table and column lineage with diagnostics. [README](https://github.com/jarredhj0214/linesql/blob/4f122a1dc29282af8fed163be044b0e1cdaf468e/README.md).

## Mechanism inspected

It splits a script, selects a dialect per statement, and returns a LineageResult for each; a missing parser produces an explicit DIALECT_NOT_REGISTERED error with confidence and detection reason attached. [Implementation](https://github.com/jarredhj0214/linesql/blob/4f122a1dc29282af8fed163be044b0e1cdaf468e/linesql-core/src/main/java/io/github/linesql/core/internal/DefaultSqlLineageParser.java#L39-L62). [Related path](https://github.com/jarredhj0214/linesql/blob/4f122a1dc29282af8fed163be044b0e1cdaf468e/linesql-core/src/main/java/io/github/linesql/core/internal/DefaultSqlLineageParser.java#L65-L114).

## Limitation that matters

Dialect detection is heuristic and static parsing cannot prove that a statement executed or that dynamically generated SQL matches the text analyzed. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Reconcile statement counts and error states before using a parsed lineage graph to claim complete data provenance.

## Why this score

Per-statement diagnostics prevent a partial parse from masquerading as full lineage, though the method needs runtime reconciliation.

## Source trail

[README](https://github.com/jarredhj0214/linesql/blob/4f122a1dc29282af8fed163be044b0e1cdaf468e/README.md) - [Implementation](https://github.com/jarredhj0214/linesql/blob/4f122a1dc29282af8fed163be044b0e1cdaf468e/linesql-core/src/main/java/io/github/linesql/core/internal/DefaultSqlLineageParser.java#L39-L62) - [Related path](https://github.com/jarredhj0214/linesql/blob/4f122a1dc29282af8fed163be044b0e1cdaf468e/linesql-core/src/main/java/io/github/linesql/core/internal/DefaultSqlLineageParser.java#L65-L114) - [License](https://github.com/jarredhj0214/linesql/blob/4f122a1dc29282af8fed163be044b0e1cdaf468e/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
