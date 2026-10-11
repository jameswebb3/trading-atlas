# Pointblank — Draft checks need an approval boundary

**Decision question:** When should inferred data-quality rules become binding?

| Field | Review |
| --- | --- |
| Upstream | [rstudio/pointblank](https://github.com/rstudio/pointblank) |
| Primary area | Data Quality & Lineage |
| Source commit | [0dc5ae0e5e00ca579fa8436598f2cd75d8218344](https://github.com/rstudio/pointblank/commit/0dc5ae0e5e00ca579fa8436598f2cd75d8218344) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/rstudio/pointblank/blob/0dc5ae0e5e00ca579fa8436598f2cd75d8218344/LICENSE.md#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | draft_validation scans a table and writes a starter validation plan to a separate file for domain-specific editing. Rules inferred from a sample can encode its quirks; generating them from evaluation data would contaminate a holdout. |

## What this project does

An R package for validating data frames and database tables and reporting data quality. [Project README](https://github.com/rstudio/pointblank/blob/0dc5ae0e5e00ca579fa8436598f2cd75d8218344/README.md#L26).

## Mechanism inspected

draft_validation scans a table and writes a starter validation plan to a separate file for domain-specific editing. [Implementation](https://github.com/rstudio/pointblank/blob/0dc5ae0e5e00ca579fa8436598f2cd75d8218344/R/draft_validation.R#L22).

## Limitation that matters

Rules inferred from a sample can encode its quirks; generating them from evaluation data would contaminate a holdout. The R package is larger than the pattern needed. This is a source review, not a runtime or security test.

## Practical check for a trading system

Version the draft, have a reviewer approve domain limits, then freeze the rules before evaluating unseen trading data.

## Why this score

The draft-versus-approved distinction is directly useful for preventing retrospective data-quality thresholds.

## Source trail

[README](https://github.com/rstudio/pointblank/blob/0dc5ae0e5e00ca579fa8436598f2cd75d8218344/README.md#L26); [Implementation](https://github.com/rstudio/pointblank/blob/0dc5ae0e5e00ca579fa8436598f2cd75d8218344/R/draft_validation.R#L22) - [License](https://github.com/rstudio/pointblank/blob/0dc5ae0e5e00ca579fa8436598f2cd75d8218344/LICENSE.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
