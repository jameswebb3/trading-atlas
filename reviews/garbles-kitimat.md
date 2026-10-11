# Kitimat — Shrink the sequence, not just one value

**Decision question:** How can a failing event trace be reduced without losing the race?

| Field | Review |
| --- | --- |
| Upstream | [garbles/kitimat](https://github.com/garbles/kitimat) |
| Primary area | Testing & Verification |
| Source commit | [a27d8c9daf98974b2df58d86aabd48d52b687886](https://github.com/garbles/kitimat/commit/a27d8c9daf98974b2df58d86aabd48d52b687886) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/garbles/kitimat/blob/a27d8c9daf98974b2df58d86aabd48d52b687886/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its array shrinker both reduces individual elements and removes portions of the sequence. A smaller array is useful only if the trading state-machine invariant still fails when replayed; timing and external fills need deterministic fixtures. |

## What this project does

A TypeScript property-testing library with composable shrinkers. [Project README](https://github.com/garbles/kitimat/blob/a27d8c9daf98974b2df58d86aabd48d52b687886/README.md#L1).

## Mechanism inspected

Its array shrinker both reduces individual elements and removes portions of the sequence. [Implementation](https://github.com/garbles/kitimat/blob/a27d8c9daf98974b2df58d86aabd48d52b687886/packages/kitimat/src/shrink.ts#L99).

## Limitation that matters

A smaller array is useful only if the trading state-machine invariant still fails when replayed; timing and external fills need deterministic fixtures. This is a source review, not a runtime or security test.

## Practical check for a trading system

Shrink duplicate ACK, partial-fill, cancel, and reconnect traces into the minimal reproducible sequence.

## Why this score

Directly useful for debugging stateful execution tests, with replay determinism as the condition.

## Source trail

[README](https://github.com/garbles/kitimat/blob/a27d8c9daf98974b2df58d86aabd48d52b687886/README.md#L1); [Implementation](https://github.com/garbles/kitimat/blob/a27d8c9daf98974b2df58d86aabd48d52b687886/packages/kitimat/src/shrink.ts#L99) - [License](https://github.com/garbles/kitimat/blob/a27d8c9daf98974b2df58d86aabd48d52b687886/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
