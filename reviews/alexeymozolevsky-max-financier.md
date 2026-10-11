# financier - Can duplicate execution reports change the same position twice?

**Decision question:** Can duplicate execution reports change the same position twice?

| Field | Review |
| --- | --- |
| Upstream | [alexeymozolevsky-max/financier](https://github.com/alexeymozolevsky-max/financier) |
| Primary area | Execution & Exchange Integration |
| Source commit | [3708a31d77cb57c0f972828488449efc341dfbf1](https://github.com/alexeymozolevsky-max/financier/commit/3708a31d77cb57c0f972828488449efc341dfbf1) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The order router checks an execution ID against a Redis dedup key before applying quantity and P&L under a shared per-ticker lock. Reports without an execution ID bypass this dedup path; a TTL-bound cache alone is not a permanent fill ledger. |

## What this project does

An event-driven crypto system with separate paper, backtest and live execution paths.

## Mechanism inspected

The order router checks an execution ID against a Redis dedup key before applying quantity and P&L under a shared per-ticker lock.

## Limitation that matters

Reports without an execution ID bypass this dedup path; a TTL-bound cache alone is not a permanent fill ledger.

## Practical check for a trading system

Keep an append-only fill identity and replay test duplicates across restart and cache expiry.

## Why this score

3/5. The inspected fill guard targets a live-money failure, but its durability boundary is narrower than the README suggests.

## Source trail

[README](https://github.com/alexeymozolevsky-max/financier/blob/3708a31d77cb57c0f972828488449efc341dfbf1/README.md#L1); [docs/ARCHITECTURE.md](https://github.com/alexeymozolevsky-max/financier/blob/3708a31d77cb57c0f972828488449efc341dfbf1/docs/ARCHITECTURE.md#L1); [engine/app/core/order_router.py](https://github.com/alexeymozolevsky-max/financier/blob/3708a31d77cb57c0f972828488449efc341dfbf1/engine/app/core/order_router.py#L404); [Root license](https://github.com/alexeymozolevsky-max/financier/blob/3708a31d77cb57c0f972828488449efc341dfbf1/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
