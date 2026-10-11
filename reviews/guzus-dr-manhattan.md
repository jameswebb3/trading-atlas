# dr-manhattan - Can a WebSocket fill callback safely define an order terminal state?

**Decision question:** Can a WebSocket fill callback safely define an order terminal state?

| Field | Review |
| --- | --- |
| Upstream | [guzus/dr-manhattan](https://github.com/guzus/dr-manhattan) |
| Primary area | Execution & Exchange Integration |
| Source commit | [7c15fad9ab32749fc7bcc6679ab6a22d9200c328](https://github.com/guzus/dr-manhattan/commit/7c15fad9ab32749fc7bcc6679ab6a22d9200c328) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Turns user trade callbacks into partial and terminal order events. Duplicate or missed callbacks can make local filled quantity diverge from venue truth. |

## What this project does

A CCXT-style prediction-market adapter with a local tracker for order and partial-fill callbacks.

## Mechanism inspected

OrderTracker accumulates trade sizes by order ID, emits partial or complete callbacks, and removes the tracked order once its sum reaches requested size.

## Limitation that matters

The inspected callback does not deduplicate trade IDs or reconcile filled quantity with the venue after reconnect. Replayed or repeated events can inflate local filled size; an unknown order is ignored. No root license text was verified.

## Practical check for a trading system

Use callbacks for latency, but confirm cumulative fills and terminal state from durable venue records.

## Why this score

2/5. The lifecycle code is useful mainly as a concrete warning about event-only accounting.

## Source trail

[README](https://github.com/guzus/dr-manhattan/blob/7c15fad9ab32749fc7bcc6679ab6a22d9200c328/README.md#L65); [dr_manhattan/base/order_tracker.py](https://github.com/guzus/dr-manhattan/blob/7c15fad9ab32749fc7bcc6679ab6a22d9200c328/dr_manhattan/base/order_tracker.py#L93); [dr_manhattan/base/order_tracker.py](https://github.com/guzus/dr-manhattan/blob/7c15fad9ab32749fc7bcc6679ab6a22d9200c328/dr_manhattan/base/order_tracker.py#L117); [dr_manhattan/base/order_tracker.py](https://github.com/guzus/dr-manhattan/blob/7c15fad9ab32749fc7bcc6679ab6a22d9200c328/dr_manhattan/base/order_tracker.py#L154).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
