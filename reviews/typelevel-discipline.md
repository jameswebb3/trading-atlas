# discipline — Composable law sets keep invariants named and reusable

**Decision question:** How can the same invariant be checked across implementations?

| Field | Review |
| --- | --- |
| Upstream | [typelevel/discipline](https://github.com/typelevel/discipline) |
| Primary area | Testing & Verification |
| Source commit | [7658404a2ed98d75f3860b7e6a4f80f146e2700d](https://github.com/typelevel/discipline/commit/7658404a2ed98d75f3860b7e6a4f80f146e2700d) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/typelevel/discipline/blob/7658404a2ed98d75f3860b7e6a4f80f146e2700d/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | A RuleSet composes parent and base laws, prefixing inherited law names to avoid collisions in the test runner. The framework supplies test composition, not market-specific invariants or a guarantee that generators cover race conditions. |

## What this project does

Scala framework for reusable law-based property tests. [README](https://github.com/typelevel/discipline/blob/7658404a2ed98d75f3860b7e6a4f80f146e2700d/README.md).

## Mechanism inspected

A RuleSet composes parent and base laws, prefixing inherited law names to avoid collisions in the test runner. [Implementation](https://github.com/typelevel/discipline/blob/7658404a2ed98d75f3860b7e6a4f80f146e2700d/core/src/main/scala/org/typelevel/discipline/Laws.scala#L79-L91).

## Limitation that matters

The framework supplies test composition, not market-specific invariants or a guarantee that generators cover race conditions. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Name and reuse order-journal, replay and accounting laws across adapters while keeping venue-specific examples.

## Why this score

A RuleSet composes parent and base laws, prefixing inherited law names to avoid collisions in the test runner. The framework supplies test composition, not market-specific invariants or a guarantee that generators cover race conditions.

## Source trail

[README](https://github.com/typelevel/discipline/blob/7658404a2ed98d75f3860b7e6a4f80f146e2700d/README.md) · [Implementation](https://github.com/typelevel/discipline/blob/7658404a2ed98d75f3860b7e6a4f80f146e2700d/core/src/main/scala/org/typelevel/discipline/Laws.scala#L79-L91) · [License](https://github.com/typelevel/discipline/blob/7658404a2ed98d75f3860b7e6a4f80f146e2700d/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
