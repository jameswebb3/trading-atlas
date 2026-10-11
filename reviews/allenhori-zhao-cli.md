# zhao-cli - Assess schema changes by real downstream use

**Decision question:** Which column changes can break a dependent model or report?

| Field | Review |
| --- | --- |
| Upstream | [allenhori/zhao-cli](https://github.com/allenhori/zhao-cli) |
| Primary area | Data Quality & Lineage |
| Source commit | [35b972938dff89ed05ced429502015cd1f685221](https://github.com/allenhori/zhao-cli/commit/35b972938dff89ed05ced429502015cd1f685221) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/allenhori/zhao-cli/blob/35b972938dff89ed05ced429502015cd1f685221/LICENSE)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Rules distinguish a removed actively referenced column, a changed expression, and a loosened join; each has a default severity and a configurable override Its static SQL model cannot establish external market-data publication time or runtime completeness. Nested struct fields lack reference-level precision in the inspected rule |

## What this project does

A dbt-oriented static change gate with model and column lineage [README](https://github.com/allenhori/zhao-cli/blob/35b972938dff89ed05ced429502015cd1f685221/README.md).

## Mechanism inspected

Rules distinguish a removed actively referenced column, a changed expression, and a loosened join; each has a default severity and a configurable override [Implementation](https://github.com/allenhori/zhao-cli/blob/35b972938dff89ed05ced429502015cd1f685221/crates/zhao-core/src/rules.rs#L50-L123). [Related path](https://github.com/allenhori/zhao-cli/blob/35b972938dff89ed05ced429502015cd1f685221/crates/zhao-core/src/lineage.rs#L1-L95).

## Limitation that matters

Its static SQL model cannot establish external market-data publication time or runtime completeness. Nested struct fields lack reference-level precision in the inspected rule This review covers the pinned source paths, not independent runtime behavior.

## Practical check for a trading system

Map each derived trading feature to its source columns and flag a change only for consumers that actually read them; keep temporal availability a separate gate

## Why this score

Specific, source-backed blast-radius semantics and documented limits; not a replacement for point-in-time validation

## Source trail

[README](https://github.com/allenhori/zhao-cli/blob/35b972938dff89ed05ced429502015cd1f685221/README.md) - [Implementation](https://github.com/allenhori/zhao-cli/blob/35b972938dff89ed05ced429502015cd1f685221/crates/zhao-core/src/rules.rs#L50-L123) - [Related path](https://github.com/allenhori/zhao-cli/blob/35b972938dff89ed05ced429502015cd1f685221/crates/zhao-core/src/lineage.rs#L1-L95) - [License](https://github.com/allenhori/zhao-cli/blob/35b972938dff89ed05ced429502015cd1f685221/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
