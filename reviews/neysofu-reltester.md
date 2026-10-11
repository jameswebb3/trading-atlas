# Reltester - Which algebraic invariants should an identity or ordering implementation satisfy?

**Decision question:** Which algebraic invariants should an identity or ordering implementation satisfy?

| Field | Review |
| --- | --- |
| Upstream | [neysofu/reltester](https://github.com/neysofu/reltester) |
| Primary area | Testing & Verification |
| Source commit | [e5ee0a7850a8fc8a747604dc3084530a63eecfd9](https://github.com/neysofu/reltester/commit/e5ee0a7850a8fc8a747604dc3084530a63eecfd9) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It checks consistency between equality and inequality and offers symmetry and transitivity probes. Generated examples are only as broad as the generator; these generic laws do not encode venue-specific order semantics. |

## What this project does

A small Rust utility for checking equality, ordering, hashing and iterator contracts.

## Mechanism inspected

It checks consistency between equality and inequality and offers symmetry and transitivity probes.

## Limitation that matters

Generated examples are only as broad as the generator; these generic laws do not encode venue-specific order semantics.

## Practical check for a trading system

Apply reflexivity, symmetry and transitivity checks to order keys, event ordering and dedup identities.

## Why this score

2/5. The invariant library is compact and directly adaptable to contract tests.

## Source trail

[README](https://github.com/neysofu/reltester/blob/e5ee0a7850a8fc8a747604dc3084530a63eecfd9/README.md#L1); [src/invariants.rs](https://github.com/neysofu/reltester/blob/e5ee0a7850a8fc8a747604dc3084530a63eecfd9/src/invariants.rs#L17); [src/invariants.rs](https://github.com/neysofu/reltester/blob/e5ee0a7850a8fc8a747604dc3084530a63eecfd9/src/invariants.rs#L30).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
