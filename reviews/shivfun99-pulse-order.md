# Pulse-Order - Should an imbalance signal run on an incomplete visible book?

**Decision question:** Should an imbalance signal run on an incomplete visible book?

| Field | Review |
| --- | --- |
| Upstream | [Shivfun99/Pulse-Order](https://github.com/Shivfun99/Pulse-Order) |
| Primary area | Market Data & Ingestion |
| Source commit | [2763bea071053c3bc63d3f1780af1e8c5853b29e](https://github.com/Shivfun99/Pulse-Order/commit/2763bea071053c3bc63d3f1780af1e8c5853b29e) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The fixed-depth book rejects invalid side, action, depth and price and exposes a completeness check across visible bid and ask levels. Completeness here means populated slots, not sequence continuity, age or crossed-book validity. |

## What this project does

A compact low-latency L2 book and order-processing prototype.

## Mechanism inspected

The fixed-depth book rejects invalid side, action, depth and price and exposes a completeness check across visible bid and ask levels.

## Limitation that matters

Completeness here means populated slots, not sequence continuity, age or crossed-book validity.

## Practical check for a trading system

Gate any depth or imbalance feature on complete, current, source-consistent book evidence.

## Why this score

3/5. The explicit visible-depth precondition is useful, but it is not a full feed-quality contract.

## Source trail

[README](https://github.com/Shivfun99/Pulse-Order/blob/2763bea071053c3bc63d3f1780af1e8c5853b29e/README.md#L1); [include/pulsebook/book/fixed_l2_book.hpp](https://github.com/Shivfun99/Pulse-Order/blob/2763bea071053c3bc63d3f1780af1e8c5853b29e/include/pulsebook/book/fixed_l2_book.hpp#L48); [Root license](https://github.com/Shivfun99/Pulse-Order/blob/2763bea071053c3bc63d3f1780af1e8c5853b29e/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
