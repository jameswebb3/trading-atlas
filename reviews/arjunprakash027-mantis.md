# Mantis - Can paper portfolio updates and their audit events be committed together?

**Decision question:** Can paper portfolio updates and their audit events be committed together?

| Field | Review |
| --- | --- |
| Upstream | [arjunprakash027/Mantis](https://github.com/arjunprakash027/Mantis) |
| Primary area | Backtesting & Simulation |
| Source commit | [a3e376719210fce26f8e5881028c4355b13d842c](https://github.com/arjunprakash027/Mantis/commit/a3e376719210fce26f8e5881028c4355b13d842c) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Atomically applies paper cash/asset changes and logs the trade. Atomic paper settlement does not validate book ordering or venue fills. |

## What this project does

A Polymarket stream processor and paper-trading engine with pluggable backends.

## Mechanism inspected

A Redis Lua transaction checks available cash or assets, updates both balances and appends a trade event atomically. The stream processor keeps a best-price cache from orderbook messages before pushing them to Redis.

## Limitation that matters

Atomic bookkeeping is not evidence of a real fill. The displayed best bid and ask come from the last element of each incoming array, so the price interpretation depends on upstream sort order; the inspected path does not verify venue sequence continuity. No root license was verified.

## Practical check for a trading system

Use an atomic paper ledger, but test book-side ordering, feed gaps and order-arrival depth separately.

## Why this score

3/5. The paper accounting boundary is useful, while the execution and feed assumptions are material.

## Source trail

[README](https://github.com/arjunprakash027/Mantis/blob/a3e376719210fce26f8e5881028c4355b13d842c/README.md#L33); [pkg/backend/trade.lua](https://github.com/arjunprakash027/Mantis/blob/a3e376719210fce26f8e5881028c4355b13d842c/pkg/backend/trade.lua#L16); [streamer/engine.go](https://github.com/arjunprakash027/Mantis/blob/a3e376719210fce26f8e5881028c4355b13d842c/streamer/engine.go#L58); [streamer/engine.go](https://github.com/arjunprakash027/Mantis/blob/a3e376719210fce26f8e5881028c4355b13d842c/streamer/engine.go#L99).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
