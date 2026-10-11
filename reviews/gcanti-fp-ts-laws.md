# fp-ts-laws — Test algebraic rules, not just examples

**Decision question:** Can an order-state reducer satisfy the same invariants for every event permutation?

| Field | Review |
| --- | --- |
| Upstream | [gcanti/fp-ts-laws](https://github.com/gcanti/fp-ts-laws) |
| Primary area | Testing & Verification |
| Source commit | [d93963a91df443af9177aa74b768549a0ebe31c1](https://github.com/gcanti/fp-ts-laws/commit/d93963a91df443af9177aa74b768549a0ebe31c1) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/gcanti/fp-ts-laws/blob/d93963a91df443af9177aa74b768549a0ebe31c1/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its equality tests generate reflexivity, symmetry, and transitivity properties through fast-check rather than enumerating handpicked examples. A law suite is only as complete as its specified laws and generators. |

## What this project does

A TypeScript package that tests algebraic laws using generated values. [Project README](https://github.com/gcanti/fp-ts-laws/blob/d93963a91df443af9177aa74b768549a0ebe31c1/README.md#L1).

## Mechanism inspected

Its equality tests generate reflexivity, symmetry, and transitivity properties through fast-check rather than enumerating handpicked examples. [Implementation](https://github.com/gcanti/fp-ts-laws/blob/d93963a91df443af9177aa74b768549a0ebe31c1/src/index.ts#L24).

## Limitation that matters

A law suite is only as complete as its specified laws and generators. Exchange event ordering and missing fills need explicit stateful generators. This is a source review, not a runtime or security test.

## Practical check for a trading system

State reducer laws such as idempotent duplicate fill and monotone cumulative quantity as generated properties.

## Why this score

A useful property-design reference, although its functional types are not a trading implementation.

## Source trail

[README](https://github.com/gcanti/fp-ts-laws/blob/d93963a91df443af9177aa74b768549a0ebe31c1/README.md#L1); [Implementation](https://github.com/gcanti/fp-ts-laws/blob/d93963a91df443af9177aa74b768549a0ebe31c1/src/index.ts#L24) - [License](https://github.com/gcanti/fp-ts-laws/blob/d93963a91df443af9177aa74b768549a0ebe31c1/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
