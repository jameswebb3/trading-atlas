# OntoPoc: How can a proposed data model expose identity and join risks before acceptance?

**Decision question:** How can a proposed data model expose identity and join risks before acceptance?

| Field | Review |
| --- | --- |
| Upstream | [Longado/ontopoc](https://github.com/Longado/ontopoc) |
| Primary area | Data Quality & Lineage |
| Source commit | [619ddf4b844b9e8225c7a79057b25b9c69bb7a7e](https://github.com/Longado/ontopoc/commit/619ddf4b844b9e8225c7a79057b25b9c69bb7a7e) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/Longado/ontopoc/blob/619ddf4b844b9e8225c7a79057b25b9c69bb7a7e/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The data-fit evaluator collects identity conflicts, unresolved references, disconnected sources and orphaned records. It flags identity based only on name-like fields, and offers a bridge only when filled values match a unique candidate key in another source. Join hints can pass by coincidence, especially on small samples, and the source calls the project an early version without independent end-to-end users. Human confirmation remains necessary. |

## What this project does

Checks a proposed ontology against source rows, reporting missing references, orphaned objects and identity keys based only on names. It also offers cross-table join hints with counts, leaving semantic approval to a person.

## Mechanism inspected

The data-fit evaluator collects identity conflicts, unresolved references, disconnected sources and orphaned records. It flags identity based only on name-like fields, and offers a bridge only when filled values match a unique candidate key in another source.

## Limitation that matters

Join hints can pass by coincidence, especially on small samples, and the source calls the project an early version without independent end-to-end users. Human confirmation remains necessary.

## Practical check for a trading system

When joining market, instrument, account or event tables, test key stability and cross-source coverage; show counterexamples and require human signoff for inferred relationships.

## Why this score

3/5 transferable: identity stability and join coverage can prevent silent research errors, but the general ontology generator is not a trading-specific data contract.

## Source trail

[README.md](https://github.com/Longado/ontopoc/blob/619ddf4b844b9e8225c7a79057b25b9c69bb7a7e/README.md#L1); [src/ontology_poc_generator/ontology_eval.py](https://github.com/Longado/ontopoc/blob/619ddf4b844b9e8225c7a79057b25b9c69bb7a7e/src/ontology_poc_generator/ontology_eval.py#L187); [src/ontology_poc_generator/ontology_eval.py](https://github.com/Longado/ontopoc/blob/619ddf4b844b9e8225c7a79057b25b9c69bb7a7e/src/ontology_poc_generator/ontology_eval.py#L217); [tests/test_identity_risk.py](https://github.com/Longado/ontopoc/blob/619ddf4b844b9e8225c7a79057b25b9c69bb7a7e/tests/test_identity_risk.py#L18)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
