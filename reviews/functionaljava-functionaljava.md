# Functional Java — Compose invariants as properties

**Decision question:** Can related execution invariants be checked together without losing failure context?

| Field | Review |
| --- | --- |
| Upstream | [functionaljava/functionaljava](https://github.com/functionaljava/functionaljava) |
| Primary area | Testing & Verification |
| Source commit | [a2f7ebe5ef319df492f547e0be4cc965af667e35](https://github.com/functionaljava/functionaljava/commit/a2f7ebe5ef319df492f547e0be4cc965af667e35) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its Property type composes conjunctions and disjunctions of generated checks and carries run parameters through the checker. A property framework only tests the invariants its user writes; it cannot discover missing venue events or prove a matching model is faithful. |

## What this project does

A Java functional-programming library with a property-testing module. [Project README](https://github.com/functionaljava/functionaljava/blob/a2f7ebe5ef319df492f547e0be4cc965af667e35/README.adoc#L11).

## Mechanism inspected

Its Property type composes conjunctions and disjunctions of generated checks and carries run parameters through the checker. [Implementation](https://github.com/functionaljava/functionaljava/blob/a2f7ebe5ef319df492f547e0be4cc965af667e35/quickcheck/src/main/java/fj/test/Property.java#L61).

## Limitation that matters

A property framework only tests the invariants its user writes; it cannot discover missing venue events or prove a matching model is faithful. This is a source review, not a runtime or security test.

## Practical check for a trading system

Express idempotency, cumulative-fill monotonicity, and cancel/fill races as explicit generated state properties.

## Why this score

The composition model is useful for adversarial testing, though this Java library is a poor dependency fit.

## Source trail

[README](https://github.com/functionaljava/functionaljava/blob/a2f7ebe5ef319df492f547e0be4cc965af667e35/README.adoc#L11); [Implementation](https://github.com/functionaljava/functionaljava/blob/a2f7ebe5ef319df492f547e0be4cc965af667e35/quickcheck/src/main/java/fj/test/Property.java#L61).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
