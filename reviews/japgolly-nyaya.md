# Nyaya - Can generic property composition replace venue-specific invariants?

**Decision question:** Can generic property composition replace venue-specific invariants?

| Field | Review |
| --- | --- |
| Upstream | [japgolly/nyaya](https://github.com/japgolly/nyaya) |
| Primary area | Testing & Verification |
| Source commit | [91032192f02af479662e50ee06e78bde873c6c1b](https://github.com/japgolly/nyaya/commit/91032192f02af479662e50ee06e78bde873c6c1b) |
| Reviewed | 2026-10-11 |
| Declared license | GPL |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Transferable |
| Executive assessment | Properties are composed over generated or finite input domains. Generic property execution does not encode partial-fill, order-state or availability rules by itself. |

## What this project does

A Scala property-testing library.

## Mechanism inspected

Properties are composed over generated or finite input domains.

## Limitation that matters

Generic property execution does not encode partial-fill, order-state or availability rules by itself.

## Practical check for a trading system

Use property generators to exercise explicit trading state invariants.

## Why this score

1/5. The technique transfers, but the Scala dependency adds little to a Python-heavy stack.

## Source trail

[README](https://github.com/japgolly/nyaya/blob/91032192f02af479662e50ee06e78bde873c6c1b/README.md#L1); [prop/shared/src/main/scala/nyaya/prop/Prop.scala](https://github.com/japgolly/nyaya/blob/91032192f02af479662e50ee06e78bde873c6c1b/prop/shared/src/main/scala/nyaya/prop/Prop.scala#L8); [Root license](https://github.com/japgolly/nyaya/blob/91032192f02af479662e50ee06e78bde873c6c1b/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
