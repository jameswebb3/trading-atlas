# chaos_theory — Mutate real failure cases alongside fresh fuzz input

**Decision question:** Do fuzz tests revisit and perturb actual incidents?

| Field | Review |
| --- | --- |
| Upstream | [flyingmutant/chaos_theory](https://github.com/flyingmutant/chaos_theory) |
| Primary area | Testing & Verification |
| Source commit | [08a96e102b0efdb1768077de18d447acba81711a](https://github.com/flyingmutant/chaos_theory/commit/08a96e102b0efdb1768077de18d447acba81711a) |
| Reviewed | 2026-10-09 |
| Declared license | MPL ([source](https://github.com/flyingmutant/chaos_theory/blob/08a96e102b0efdb1768077de18d447acba81711a/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | A generator can use supplied domain seeds as exact values or mutated variants while still producing other values; filters can report inability to construct a valid sample. Its generic mutation distribution gives no coverage guarantee for trading event order or time semantics; seeds must be redacted and serialized reproducibly. |

## What this project does

Rust property and fuzz testing library with seed-biased generators. [README](https://github.com/flyingmutant/chaos_theory/blob/08a96e102b0efdb1768077de18d447acba81711a/README.md).

## Mechanism inspected

A generator can use supplied domain seeds as exact values or mutated variants while still producing other values; filters can report inability to construct a valid sample. [Implementation](https://github.com/flyingmutant/chaos_theory/blob/08a96e102b0efdb1768077de18d447acba81711a/chaos_theory/src/generator.rs#L39-L106).

## Limitation that matters

Its generic mutation distribution gives no coverage guarantee for trading event order or time semantics; seeds must be redacted and serialized reproducibly. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Seed the local replay fuzz harness with sanitized historical failure traces, preserve the seed and shrink path, and assert coverage of critical order-state transitions.

## Why this score

A generator can use supplied domain seeds as exact values or mutated variants while still producing other values; filters can report inability to construct a valid sample. Its generic mutation distribution gives no coverage guarantee for trading event order or time semantics; seeds must be redacted and serialized reproducibly.

## Source trail

[README](https://github.com/flyingmutant/chaos_theory/blob/08a96e102b0efdb1768077de18d447acba81711a/README.md) · [Implementation](https://github.com/flyingmutant/chaos_theory/blob/08a96e102b0efdb1768077de18d447acba81711a/chaos_theory/src/generator.rs#L39-L106) · [License](https://github.com/flyingmutant/chaos_theory/blob/08a96e102b0efdb1768077de18d447acba81711a/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
