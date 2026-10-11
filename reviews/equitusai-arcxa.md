# ARCXA - Schema drift needs typed change records and a licensing check

**Decision question:** Can a downstream consumer distinguish a changed field from a broken contract?

| Field | Review |
| --- | --- |
| Upstream | [equitusai/arcxa](https://github.com/equitusai/arcxa) |
| Primary area | Data Quality & Lineage |
| Source commit | [b967df41cfa329d76cfdac317ac5ce97a660a1b4](https://github.com/equitusai/arcxa/commit/b967df41cfa329d76cfdac317ac5ce97a660a1b4) |
| Reviewed | 2026-10-10 |
| Declared license | Business Source License 1.1 (root LICENSE.md) |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Represents schema changes with before and after state, migration context, version ancestry and an explicit breaking flag. The typed flag is not itself a complete compatibility test, and the Business Source License restricts implementation reuse. |

## What this project does

A data integration and lineage platform. The inspected Rust module defines schema-change events and version snapshots; source integration tests exercise recording and querying changes.

## Mechanism inspected

Each change event records datasource, table or column, before and after states, detection time, migration identity and a breaking-change flag. Version snapshots retain tables, a predecessor version and an optional Git commit. Integration tests read in source record an event and query it by datasource and table.

## Limitation that matters

The inspected type holds an is_breaking flag; the type alone does not prove how that flag is derived for every source. The repository is under Business Source License 1.1 rather than a permissive open-source license, so reuse of implementation needs a separate licensing decision. This is a source review, not a runtime or security test.

## Practical check for a trading system

For feed or feature schema changes, store typed before/after evidence and the exact consumer contract version. Derive breaking status with local rules and tests; use the pattern rather than this package.

## Why this score

2/5 because the schema evidence model transfers to trading ingestion but is not trading-specific, and the source-available license limits direct adoption.

## Source trail

[README](https://github.com/equitusai/arcxa/blob/b967df41cfa329d76cfdac317ac5ce97a660a1b4/README.md#L37); [Change event](https://github.com/equitusai/arcxa/blob/b967df41cfa329d76cfdac317ac5ce97a660a1b4/arcxa-core/src/core/lineage/schema_evolution.rs#L14); [Version snapshot](https://github.com/equitusai/arcxa/blob/b967df41cfa329d76cfdac317ac5ce97a660a1b4/arcxa-core/src/core/lineage/schema_evolution.rs#L196); [Integration test](https://github.com/equitusai/arcxa/blob/b967df41cfa329d76cfdac317ac5ce97a660a1b4/arcxa-coordinator/tests/schema_evolution_integration_test.rs#L16); [License](https://github.com/equitusai/arcxa/blob/b967df41cfa329d76cfdac317ac5ce97a660a1b4/LICENSE.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
