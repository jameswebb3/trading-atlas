# ETLX — Define what zero rows means

**Decision question:** Is an empty validation query a clean result or a missing test?

| Field | Review |
| --- | --- |
| Upstream | [realdatadriven/etlx](https://github.com/realdatadriven/etlx) |
| Primary area | Data Quality & Lineage |
| Source commit | [ea45714d82594513a10e3811264c4197c84175b7](https://github.com/realdatadriven/etlx/commit/ea45714d82594513a10e3811264c4197c84175b7) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/realdatadriven/etlx/blob/ea45714d82594513a10e3811264c4197c84175b7/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its data-quality helper records query errors as failure, but treats a successful query returning zero rows as success with nrows zero. Zero rows can mean no violations or no evaluated universe; the query contract must say which. |

## What this project does

A SQL-first workflow engine whose Markdown files serve as executable pipeline definitions and documentation. [Project README](https://github.com/realdatadriven/etlx/blob/ea45714d82594513a10e3811264c4197c84175b7/README.md#L1).

## Mechanism inspected

Its data-quality helper records query errors as failure, but treats a successful query returning zero rows as success with nrows zero. [Implementation](https://github.com/realdatadriven/etlx/blob/ea45714d82594513a10e3811264c4197c84175b7/internal/etlx/run_etl.go#L1225). [Related source 1](https://github.com/realdatadriven/etlx/blob/ea45714d82594513a10e3811264c4197c84175b7/README.md#L37). [Related source 2](https://github.com/realdatadriven/etlx/blob/ea45714d82594513a10e3811264c4197c84175b7/internal/etlx/data_quality.go#L70).

## Limitation that matters

Zero rows can mean no violations or no evaluated universe; the query contract must say which. This general SQL/Markdown runner is larger than a trading-data check layer. This is a source review, not a runtime or security test.

## Practical check for a trading system

Define expected input cardinality and an explicit result type for zero violations, empty universe, and query error.

## Why this score

The result-state distinction is useful; the framework itself is too broad for a simple trading data contract.

## Source trail

[README](https://github.com/realdatadriven/etlx/blob/ea45714d82594513a10e3811264c4197c84175b7/README.md#L1); [Implementation](https://github.com/realdatadriven/etlx/blob/ea45714d82594513a10e3811264c4197c84175b7/internal/etlx/run_etl.go#L1225); [Related source 1](https://github.com/realdatadriven/etlx/blob/ea45714d82594513a10e3811264c4197c84175b7/README.md#L37); [Related source 2](https://github.com/realdatadriven/etlx/blob/ea45714d82594513a10e3811264c4197c84175b7/internal/etlx/data_quality.go#L70) - [License](https://github.com/realdatadriven/etlx/blob/ea45714d82594513a10e3811264c4197c84175b7/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
