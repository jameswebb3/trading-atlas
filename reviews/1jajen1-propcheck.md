# propCheck - Can a property failure be replayed with the same size and seed?

**Decision question:** Can a property failure be replayed with the same size and seed?

| Field | Review |
| --- | --- |
| Upstream | [1Jajen1/propCheck](https://github.com/1Jajen1/propCheck) |
| Primary area | Testing & Verification |
| Source commit | [8842d641270a461e829feab7b5d3b749372ac440](https://github.com/1Jajen1/propCheck/commit/8842d641270a461e829feab7b5d3b749372ac440) |
| Reviewed | 2026-10-11 |
| Declared license | BSD-3-Clause |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The API exposes recheck(size, seed, property) and tracks test count, discards, size, seed and coverage in run state. A seed reproduces generator choices only under the same code and configuration; confidence checks do not replace domain-specific invariants. |

## What this project does

A Kotlin property-based testing library.

## Mechanism inspected

The API exposes recheck(size, seed, property) and tracks test count, discards, size, seed and coverage in run state.

## Limitation that matters

A seed reproduces generator choices only under the same code and configuration; confidence checks do not replace domain-specific invariants.

## Practical check for a trading system

Store seed, generator version and event fixture when a trading-state property fails.

## Why this score

2/5. The replay contract and explicit discard count are useful test-design references.

## Source trail

[README](https://github.com/1Jajen1/propCheck/blob/8842d641270a461e829feab7b5d3b749372ac440/README.md#L1); [src/main/kotlin/propCheck/PropCheck.kt](https://github.com/1Jajen1/propCheck/blob/8842d641270a461e829feab7b5d3b749372ac440/src/main/kotlin/propCheck/PropCheck.kt#L79); [src/main/kotlin/propCheck/PropCheck.kt](https://github.com/1Jajen1/propCheck/blob/8842d641270a461e829feab7b5d3b749372ac440/src/main/kotlin/propCheck/PropCheck.kt#L155).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
