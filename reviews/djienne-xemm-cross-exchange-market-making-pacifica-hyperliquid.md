# XEMM Pacifica–Hyperliquid - When is cross-venue exposure actually neutral after a hedge?

**Decision question:** When is cross-venue exposure actually neutral after a hedge?

| Field | Review |
| --- | --- |
| Upstream | [djienne/XEMM_CROSS_EXCHANGE_MARKET_MAKING_PACIFICA_HYPERLIQUID](https://github.com/djienne/XEMM_CROSS_EXCHANGE_MARKET_MAKING_PACIFICA_HYPERLIQUID) |
| Primary area | Execution & Exchange Integration |
| Source commit | [2260cc353bc7a7e9c35b448df21d0b6f7a7fc8be](https://github.com/djienne/XEMM_CROSS_EXCHANGE_MARKET_MAKING_PACIFICA_HYPERLIQUID/commit/2260cc353bc7a7e9c35b448df21d0b6f7a7fc8be) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Reconciles maker exposure against in-flight hedges before declaring a cycle complete. A bounded dedup cache and cross-venue timing still require durable reconciliation. |

## What this project does

A Rust cross-exchange market maker that quotes on Pacifica and hedges fills on Hyperliquid.

## Mechanism inspected

A lifecycle journal records hedge intent and residual quantities. The reconciler subtracts same-side hedge quantity already reserved in flight, distinguishes tiny unhedgeable residuals, and requires two neutral observations plus no maker orders before completing a cycle. A bounded key set deduplicates fill observations.

## Limitation that matters

It is cross-venue execution with no verified source license at this commit. The bounded dedup set can evict old keys; a very late duplicate would require durable venue-side evidence, and simulated neutrality is not proof of profitable spread capture.

## Practical check for a trading system

Use explicit pending-hedge reservations and venue exposure reads to separate uncovered exposure from a slow hedge.

## Why this score

4/5. The pending-aware reconciliation and neutral-completion gate are strong direct execution references, with durable-identity limits.

## Source trail

[README](https://github.com/djienne/XEMM_CROSS_EXCHANGE_MARKET_MAKING_PACIFICA_HYPERLIQUID/blob/2260cc353bc7a7e9c35b448df21d0b6f7a7fc8be/README.md#L32); [src/services/hedge_store.rs](https://github.com/djienne/XEMM_CROSS_EXCHANGE_MARKET_MAKING_PACIFICA_HYPERLIQUID/blob/2260cc353bc7a7e9c35b448df21d0b6f7a7fc8be/src/services/hedge_store.rs#L76); [src/services/position_reconciler.rs](https://github.com/djienne/XEMM_CROSS_EXCHANGE_MARKET_MAKING_PACIFICA_HYPERLIQUID/blob/2260cc353bc7a7e9c35b448df21d0b6f7a7fc8be/src/services/position_reconciler.rs#L90); [src/services/position_reconciler.rs](https://github.com/djienne/XEMM_CROSS_EXCHANGE_MARKET_MAKING_PACIFICA_HYPERLIQUID/blob/2260cc353bc7a7e9c35b448df21d0b6f7a7fc8be/src/services/position_reconciler.rs#L154); [src/services/fill_dedup.rs](https://github.com/djienne/XEMM_CROSS_EXCHANGE_MARKET_MAKING_PACIFICA_HYPERLIQUID/blob/2260cc353bc7a7e9c35b448df21d0b6f7a7fc8be/src/services/fill_dedup.rs#L89).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
