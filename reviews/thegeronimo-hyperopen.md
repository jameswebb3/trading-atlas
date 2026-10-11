# Hyperopen — Reconcile the live view without rewriting the audit ledger

**Decision question:** How can a resting order leave the UI without falsifying its submission record?

| Field | Review |
| --- | --- |
| Upstream | [thegeronimo/hyperopen](https://github.com/thegeronimo/hyperopen) |
| Primary area | Execution & Exchange Integration |
| Source commit | [2765b4f49584c8826093f2beb3c07ea9e9a738ef](https://github.com/thegeronimo/hyperopen/commit/2765b4f49584c8826093f2beb3c07ea9e9a738ef) |
| Reviewed | 2026-10-10 |
| Declared license | AGPL-3.0 ([source](https://github.com/thegeronimo/hyperopen/blob/2765b4f49584c8826093f2beb3c07ea9e9a738ef/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | A documented fix overlays live fills and open orders onto a frozen submission ledger, using exchange order IDs and client-order ownership to identify the order. A live overlay can be stale or incomplete after a feed gap; disappearance from open orders alone is not proof of fill. |

## What this project does

A Hyperliquid trading interface with execution and portfolio views. [Project README](https://github.com/thegeronimo/hyperopen/blob/2765b4f49584c8826093f2beb3c07ea9e9a738ef/README.md#L118).

## Mechanism inspected

A documented fix overlays live fills and open orders onto a frozen submission ledger, using exchange order IDs and client-order ownership to identify the order. [Implementation](https://github.com/thegeronimo/hyperopen/blob/2765b4f49584c8826093f2beb3c07ea9e9a738ef/src/hyperopen/portfolio/optimizer/application/execution_cloid.cljs#L74). [Related source 1](https://github.com/thegeronimo/hyperopen/blob/2765b4f49584c8826093f2beb3c07ea9e9a738ef/docs/exec-plans/active/2026-06-30-optimizer-execution-resting-fill-reconcile.md#L7).

## Limitation that matters

A live overlay can be stale or incomplete after a feed gap; disappearance from open orders alone is not proof of fill. Account-scoped reconciliation and positive fill evidence remain essential. This is a source review, not a runtime or security test.

## Practical check for a trading system

Keep immutable submission evidence and derive current status from account-scoped exchange facts, with Unknown on missing coverage.

## Why this score

Directly addresses order-state drift and preserves audit history; venue-feed completeness still needs separate proof.

## Source trail

[README](https://github.com/thegeronimo/hyperopen/blob/2765b4f49584c8826093f2beb3c07ea9e9a738ef/README.md#L118); [Implementation](https://github.com/thegeronimo/hyperopen/blob/2765b4f49584c8826093f2beb3c07ea9e9a738ef/src/hyperopen/portfolio/optimizer/application/execution_cloid.cljs#L74); [Related source 1](https://github.com/thegeronimo/hyperopen/blob/2765b4f49584c8826093f2beb3c07ea9e9a738ef/docs/exec-plans/active/2026-06-30-optimizer-execution-resting-fill-reconcile.md#L7) - [License](https://github.com/thegeronimo/hyperopen/blob/2765b4f49584c8826093f2beb3c07ea9e9a738ef/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
