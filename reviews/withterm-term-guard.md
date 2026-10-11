# term-guard — Suggest cross-table checks from schema shape

**Decision question:** Which relationships need a coverage or consistency assertion?

| Field | Review |
| --- | --- |
| Upstream | [withterm/term-guard](https://github.com/withterm/term-guard) |
| Primary area | Data Quality & Lineage |
| Source commit | [23b71bee02731a774ed82ca12b8e0f1f22a1c984](https://github.com/withterm/term-guard/commit/23b71bee02731a774ed82ca12b8e0f1f22a1c984) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/withterm/term-guard/blob/23b71bee02731a774ed82ca12b8e0f1f22a1c984/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The analyzer recognizes likely foreign keys, time, amount and quantity columns from names and emits prioritized constraint suggestions with confidence and rationale. Name-based inference can mistake trading fields and cannot establish economic meaning; every generated check needs explicit review. |

## What this project does

DataFusion-backed validation framework with a schema analyzer for candidate cross-table constraints. [README](https://github.com/withterm/term-guard/blob/23b71bee02731a774ed82ca12b8e0f1f22a1c984/README.md).

## Mechanism inspected

The analyzer recognizes likely foreign keys, time, amount and quantity columns from names and emits prioritized constraint suggestions with confidence and rationale. [Implementation](https://github.com/withterm/term-guard/blob/23b71bee02731a774ed82ca12b8e0f1f22a1c984/term-guard/src/analyzers/schema_analyzer.rs#L47-L125).

## Limitation that matters

Name-based inference can mistake trading fields and cannot establish economic meaning; every generated check needs explicit review. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Use schema heuristics to propose, not auto-approve, join coverage and conservation checks across raw, normalized and replay tables.

## Why this score

The analyzer recognizes likely foreign keys, time, amount and quantity columns from names and emits prioritized constraint suggestions with confidence and rationale. Name-based inference can mistake trading fields and cannot establish economic meaning; every generated check needs explicit review.

## Source trail

[README](https://github.com/withterm/term-guard/blob/23b71bee02731a774ed82ca12b8e0f1f22a1c984/README.md) · [Implementation](https://github.com/withterm/term-guard/blob/23b71bee02731a774ed82ca12b8e0f1f22a1c984/term-guard/src/analyzers/schema_analyzer.rs#L47-L125) · [License](https://github.com/withterm/term-guard/blob/23b71bee02731a774ed82ca12b8e0f1f22a1c984/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
