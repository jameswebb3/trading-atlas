# Yrel - Can invalid input ever be returned as usable data?

**Decision question:** Can invalid input ever be returned as usable data?

| Field | Review |
| --- | --- |
| Upstream | [romelperez/yrel](https://github.com/romelperez/yrel) |
| Primary area | Data Quality & Lineage |
| Source commit | [9d947de7faef13bc5e2a8c5a66d4d423082b8b45](https://github.com/romelperez/yrel/commit/9d947de7faef13bc5e2a8c5a66d4d423082b8b45) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its result type carries either valid typed data or path-specific issues with data undefined. Schema validation alone cannot check exchange sequence, availability time or coverage. |

## What this project does

A TypeScript schema validation library.

## Mechanism inspected

Its result type carries either valid typed data or path-specific issues with data undefined.

## Limitation that matters

Schema validation alone cannot check exchange sequence, availability time or coverage.

## Practical check for a trading system

Keep invalid market records out of typed downstream paths and add domain invariants separately.

## Why this score

2/5. The discriminated result is sound interface design, but too generic to score higher.

## Source trail

[README](https://github.com/romelperez/yrel/blob/9d947de7faef13bc5e2a8c5a66d4d423082b8b45/README.md#L1); [src/validateYrel.ts](https://github.com/romelperez/yrel/blob/9d947de7faef13bc5e2a8c5a66d4d423082b8b45/src/validateYrel.ts#L9); [src/validateYrel.ts](https://github.com/romelperez/yrel/blob/9d947de7faef13bc5e2a8c5a66d4d423082b8b45/src/validateYrel.ts#L52); [Root license](https://github.com/romelperez/yrel/blob/9d947de7faef13bc5e2a8c5a66d4d423082b8b45/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
