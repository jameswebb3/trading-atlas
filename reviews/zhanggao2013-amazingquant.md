# AmazingQuant — Preflight available balance and closable position

**Decision question:** Can an order be rejected before it consumes unavailable capital or position?

| Field | Review |
| --- | --- |
| Upstream | [AmazingQuant](https://github.com/zhanggao2013/AmazingQuant) |
| Primary area | Portfolio & Risk |
| Source commit | [a1d2cc37c1c76234a60913a1936d0ef2fcf420f3](https://github.com/zhanggao2013/AmazingQuant/commit/a1d2cc37c1c76234a60913a1936d0ef2fcf420f3) |
| Reviewed | 2026-10-06 |
| Declared license | [AGPL-3.0](https://github.com/zhanggao2013/AmazingQuant/blob/a1d2cc37c1c76234a60913a1936d0ef2fcf420f3/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The order event handler sets a withdrawn status when buy notional exceeds available account balance or a close exceeds available position. It uses mutable global environment state and equity/futures conventions; the checks do not establish HL margin or reduce-only correctness. |

## What this project does

A modular quant platform with data, factor, strategy and performance components. [README](https://github.com/zhanggao2013/AmazingQuant/blob/a1d2cc37c1c76234a60913a1936d0ef2fcf420f3/README.md).

## Mechanism inspected

The order event handler sets a withdrawn status when buy notional exceeds available account balance or a close exceeds available position. [Implementation](https://github.com/zhanggao2013/AmazingQuant/blob/a1d2cc37c1c76234a60913a1936d0ef2fcf420f3/AmazingQuant/trade_center/event_order.py#L28-L69).

## Limitation that matters

It uses mutable global environment state and equity/futures conventions; the checks do not establish HL margin or reduce-only correctness. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Add a fixture for insufficient collateral and insufficient closable size at the order boundary.

## Why this score

Direct trading-system relevance: The order event handler sets a withdrawn status when buy notional exceeds available account balance or a close exceeds available position. It uses mutable global environment state and equity/futures conventions; the checks do not establish HL margin or reduce-only correctness.

## Source trail

[README](https://github.com/zhanggao2013/AmazingQuant/blob/a1d2cc37c1c76234a60913a1936d0ef2fcf420f3/README.md) · [Implementation](https://github.com/zhanggao2013/AmazingQuant/blob/a1d2cc37c1c76234a60913a1936d0ef2fcf420f3/AmazingQuant/trade_center/event_order.py#L28-L69).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
