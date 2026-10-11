# inbq - Trace derived columns through SQL

**Decision question:** Can a feature be traced to the exact input column that produced it?

| Field | Review |
| --- | --- |
| Upstream | [lpraat/inbq](https://github.com/lpraat/inbq) |
| Primary area | Data Quality & Lineage |
| Source commit | [917a2715e3825cbe2cdf6fb26b848ffa6f39b74a](https://github.com/lpraat/inbq/commit/917a2715e3825cbe2cdf6fb26b848ffa6f39b74a) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/lpraat/inbq/blob/917a2715e3825cbe2cdf6fb26b848ffa6f39b74a/LICENSE)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | It constructs source-table nodes from catalog schemas and returns an error for each AST whose lineage extraction fails instead of silently declaring success It only sees SQL and supplied schemas, not the time a market event became available; duplicate catalog objects panic in the inspected path |

## What this project does

A BigQuery SQL parser and schema-aware column-lineage extractor [README](https://github.com/lpraat/inbq/blob/917a2715e3825cbe2cdf6fb26b848ffa6f39b74a/README.md).

## Mechanism inspected

It constructs source-table nodes from catalog schemas and returns an error for each AST whose lineage extraction fails instead of silently declaring success [Implementation](https://github.com/lpraat/inbq/blob/917a2715e3825cbe2cdf6fb26b848ffa6f39b74a/crates/inbq/src/lineage/engine.rs#L6809-L6850). [Related path](https://github.com/lpraat/inbq/blob/917a2715e3825cbe2cdf6fb26b848ffa6f39b74a/crates/inbq/src/lineage/engine.rs#L7040-L7050).

## Limitation that matters

It only sees SQL and supplied schemas, not the time a market event became available; duplicate catalog objects panic in the inspected path This review covers the pinned source paths, not independent runtime behavior.

## Practical check for a trading system

For SQL-built research features, record source columns and unresolved extraction errors. Separately verify available_at and upstream collector coverage

## Why this score

Detailed column tracing is useful for derived features, with clear dialect and runtime limits

## Source trail

[README](https://github.com/lpraat/inbq/blob/917a2715e3825cbe2cdf6fb26b848ffa6f39b74a/README.md) - [Implementation](https://github.com/lpraat/inbq/blob/917a2715e3825cbe2cdf6fb26b848ffa6f39b74a/crates/inbq/src/lineage/engine.rs#L6809-L6850) - [Related path](https://github.com/lpraat/inbq/blob/917a2715e3825cbe2cdf6fb26b848ffa6f39b74a/crates/inbq/src/lineage/engine.rs#L7040-L7050) - [License](https://github.com/lpraat/inbq/blob/917a2715e3825cbe2cdf6fb26b848ffa6f39b74a/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
