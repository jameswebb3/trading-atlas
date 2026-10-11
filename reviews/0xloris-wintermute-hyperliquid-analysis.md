# wintermute-hyperliquid-analysis - Can a visible quoting tier be mistaken for hidden strategy intent?

**Decision question:** Can a visible quoting tier be mistaken for hidden strategy intent?

| Field | Review |
| --- | --- |
| Upstream | [0xLoris/wintermute-hyperliquid-analysis](https://github.com/0xLoris/wintermute-hyperliquid-analysis) |
| Primary area | Signals & Models |
| Source commit | [a70ba3438a47ecbe665073353403cf0bd16fb0f9](https://github.com/0xLoris/wintermute-hyperliquid-analysis/commit/a70ba3438a47ecbe665073353403cf0bd16fb0f9) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | It sorts bids and asks, groups displayed sizes into tiers and computes each order's distance from mid. Displayed orders are a mutable snapshot; inferred tiers do not prove fills, motives or future quoting behavior. |

## What this project does

A script analyzing one Hyperliquid account's open orders and mid prices.

## Mechanism inspected

It sorts bids and asks, groups displayed sizes into tiers and computes each order's distance from mid.

## Limitation that matters

Displayed orders are a mutable snapshot; inferred tiers do not prove fills, motives or future quoting behavior.

## Practical check for a trading system

Treat size-tier clustering as descriptive market structure and preregister any predictive hypothesis separately.

## Why this score

2/5. The calculation is transparent but has no demonstrated alpha or temporal validation.

## Source trail

[README](https://github.com/0xLoris/wintermute-hyperliquid-analysis/blob/a70ba3438a47ecbe665073353403cf0bd16fb0f9/README.md#L1); [scripts/fetch_orders.py](https://github.com/0xLoris/wintermute-hyperliquid-analysis/blob/a70ba3438a47ecbe665073353403cf0bd16fb0f9/scripts/fetch_orders.py#L60).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
