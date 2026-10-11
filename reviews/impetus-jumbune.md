# Jumbune - Are dirty rows and total rule violations the same count?

**Decision question:** Are dirty rows and total rule violations the same count?

| Field | Review |
| --- | --- |
| Upstream | [Impetus/jumbune](https://github.com/Impetus/jumbune) |
| Primary area | Data Quality & Lineage |
| Source commit | [21f94af367dba489909255d68203b20018f097a8](https://github.com/Impetus/jumbune/commit/21f94af367dba489909255d68203b20018f097a8) |
| Reviewed | 2026-10-11 |
| Declared license | LGPL-3.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The reducer maintains sets of dirty row identities separately from violation totals by rule type. Its Hadoop implementation is distant from live feeds and does not establish temporal availability. |

## What this project does

A Hadoop-era data-validation system.

## Mechanism inspected

The reducer maintains sets of dirty row identities separately from violation totals by rule type.

## Limitation that matters

Its Hadoop implementation is distant from live feeds and does not establish temporal availability.

## Practical check for a trading system

Report both unique bad records and violation counts in quality receipts.

## Why this score

2/5. The two-denominator pattern is useful despite the old stack.

## Source trail

[README](https://github.com/Impetus/jumbune/blob/21f94af367dba489909255d68203b20018f097a8/README.md#L1); [datavalidation/src/main/java/org/jumbune/datavalidation/DataValidationReducer.java](https://github.com/Impetus/jumbune/blob/21f94af367dba489909255d68203b20018f097a8/datavalidation/src/main/java/org/jumbune/datavalidation/DataValidationReducer.java#L113); [datavalidation/src/main/java/org/jumbune/datavalidation/DataValidationReducer.java](https://github.com/Impetus/jumbune/blob/21f94af367dba489909255d68203b20018f097a8/datavalidation/src/main/java/org/jumbune/datavalidation/DataValidationReducer.java#L243); [Root license](https://github.com/Impetus/jumbune/blob/21f94af367dba489909255d68203b20018f097a8/LICENSE.txt#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
