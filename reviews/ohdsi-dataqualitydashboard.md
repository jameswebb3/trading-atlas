# DataQualityDashboard — Missing prerequisites are not a pass

**Decision question:** What should a quality check report when its prerequisite checks are absent?

| Field | Review |
| --- | --- |
| Upstream | [OHDSI/DataQualityDashboard](https://github.com/OHDSI/DataQualityDashboard) |
| Primary area | Data Quality & Lineage |
| Source commit | [9b72f1c8f3db537faa9f59dbe860d8850937aad7](https://github.com/OHDSI/DataQualityDashboard/commit/9b72f1c8f3db537faa9f59dbe860d8850937aad7) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 declared in package metadata ([source](https://github.com/OHDSI/DataQualityDashboard/blob/9b72f1c8f3db537faa9f59dbe860d8850937aad7/DESCRIPTION#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | It calculates Not Applicable only when required prerequisite checks exist; otherwise the fallback sets Passed from failed and error flags. A missing prerequisite can therefore leave a check green without proving that it was applicable. |

## What this project does

A medical observational-data quality system with explicit Error, Not Applicable, Failed, and Passed states. [Project README](https://github.com/OHDSI/DataQualityDashboard/blob/9b72f1c8f3db537faa9f59dbe860d8850937aad7/README.md#L11).

## Mechanism inspected

It calculates Not Applicable only when required prerequisite checks exist; otherwise the fallback sets Passed from failed and error flags. [Implementation](https://github.com/OHDSI/DataQualityDashboard/blob/9b72f1c8f3db537faa9f59dbe860d8850937aad7/R/evaluateThresholds.R#L177). [Related source 1](https://github.com/OHDSI/DataQualityDashboard/blob/9b72f1c8f3db537faa9f59dbe860d8850937aad7/vignettes/CheckStatusDefinitions.rmd#L18). [Related source 2](https://github.com/OHDSI/DataQualityDashboard/blob/9b72f1c8f3db537faa9f59dbe860d8850937aad7/R/calculateNotApplicableStatus.R#L35).

## Limitation that matters

A missing prerequisite can therefore leave a check green without proving that it was applicable. The OMOP data model and R stack do not transfer directly to market data. This is a source review, not a runtime or security test.

## Practical check for a trading system

Require a prerequisite matrix; absent source, schema, or baseline yields Unknown or Not Evaluated, never Pass.

## Why this score

Its status model and fallback branch expose a general false-green risk in data gates.

## Source trail

[README](https://github.com/OHDSI/DataQualityDashboard/blob/9b72f1c8f3db537faa9f59dbe860d8850937aad7/README.md#L11); [Implementation](https://github.com/OHDSI/DataQualityDashboard/blob/9b72f1c8f3db537faa9f59dbe860d8850937aad7/R/evaluateThresholds.R#L177); [Related source 1](https://github.com/OHDSI/DataQualityDashboard/blob/9b72f1c8f3db537faa9f59dbe860d8850937aad7/vignettes/CheckStatusDefinitions.rmd#L18); [Related source 2](https://github.com/OHDSI/DataQualityDashboard/blob/9b72f1c8f3db537faa9f59dbe860d8850937aad7/R/calculateNotApplicableStatus.R#L35) - [License](https://github.com/OHDSI/DataQualityDashboard/blob/9b72f1c8f3db537faa9f59dbe860d8850937aad7/DESCRIPTION#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
