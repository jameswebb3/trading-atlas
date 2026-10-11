# RDFUnit - Can a data test be rejected before it runs against production data?

**Decision question:** Can a data test be rejected before it runs against production data?

| Field | Review |
| --- | --- |
| Upstream | [AKSW/RDFUnit](https://github.com/AKSW/RDFUnit) |
| Primary area | Data Quality & Lineage |
| Source commit | [4d98ab1c488fddbee6db696cdb1d26a775bc752c](https://github.com/AKSW/RDFUnit/commit/4d98ab1c488fddbee6db696cdb1d26a775bc752c) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The TestCaseValidator prepares SELECT, extended SELECT, COUNT and ASK query variants and checks each generated query. Syntactic validity of generated queries does not establish that a test expresses the intended market-data invariant. |

## What this project does

A unit-testing suite for RDF graphs.

## Mechanism inspected

The TestCaseValidator prepares SELECT, extended SELECT, COUNT and ASK query variants and checks each generated query.

## Limitation that matters

Syntactic validity of generated queries does not establish that a test expresses the intended market-data invariant.

## Practical check for a trading system

Compile and validate data contracts before applying them, then test their semantics on known counterexamples.

## Why this score

2/5. The preflight is useful for contract tooling, with a clear syntax-versus-meaning boundary.

## Source trail

[README](https://github.com/AKSW/RDFUnit/blob/4d98ab1c488fddbee6db696cdb1d26a775bc752c/README.md#L1); [rdfunit-core/src/main/java/org/aksw/rdfunit/tests/TestCaseValidator.java](https://github.com/AKSW/RDFUnit/blob/4d98ab1c488fddbee6db696cdb1d26a775bc752c/rdfunit-core/src/main/java/org/aksw/rdfunit/tests/TestCaseValidator.java#L28); [rdfunit-core/src/main/java/org/aksw/rdfunit/tests/TestCaseValidator.java](https://github.com/AKSW/RDFUnit/blob/4d98ab1c488fddbee6db696cdb1d26a775bc752c/rdfunit-core/src/main/java/org/aksw/rdfunit/tests/TestCaseValidator.java#L31); [rdfunit-core/src/main/java/org/aksw/rdfunit/tests/TestCaseValidator.java](https://github.com/AKSW/RDFUnit/blob/4d98ab1c488fddbee6db696cdb1d26a775bc752c/rdfunit-core/src/main/java/org/aksw/rdfunit/tests/TestCaseValidator.java#L36).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
