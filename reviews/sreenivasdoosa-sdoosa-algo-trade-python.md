# sdoosa-algo-trade-python - Does a partially filled cancelled order remain distinguishable from completion?

**Decision question:** Does a partially filled cancelled order remain distinguishable from completion?

| Field | Review |
| --- | --- |
| Upstream | [sreenivasdoosa/sdoosa-algo-trade-python](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python) |
| Primary area | Execution Exchange Integration |
| Source commit | [fd119b12b7f5176d4d5274120edaad2c59b2b5b8](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python/commit/fd119b12b7f5176d4d5274120edaad2c59b2b5b8) |
| Reviewed | 2026-10-10 |
| Declared license | No root LICENSE file found at the reviewed commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Updates quantity, filled quantity and pending quantity from the broker book, then rewrites CANCELLED with any fill as COMPLETED. The status rewrite hides that a residual quantity was cancelled; the example is for Indian equities, not Hyperliquid. |

## What this project does

An educational Python algorithmic-trading project for Indian brokers. The inspected Zerodha adapter refreshes local order objects from broker order-book records.

## Mechanism inspected

The update copies broker quantity, filled and pending quantities, status, price and average fill price into a local order object. That is useful account evidence, but the following branch replaces a cancelled status with COMPLETED whenever filled quantity is positive.

## Limitation that matters

A partial fill followed by cancellation has two facts: filled exposure and cancelled residual. Renaming it completed erases the terminal cause and can make a strategy believe its intended full quantity was filled. The source does retain filledQty and pendingQty, but a consumer looking only at orderStatus loses the distinction. This is a source review, not a runtime test.

## Practical check for a trading system

Represent terminal order state and cumulative filled amount separately. In a replay or restart test, feed partial fill followed by cancel and assert both exposure and residual-cancel evidence survive.

## Why this score

2/5 because the code exposes a directly relevant order-state hazard, but it is an educational adapter for a different venue and offers no verified reconciliation protocol.

## Source trail

[README](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python/blob/fd119b12b7f5176d4d5274120edaad2c59b2b5b8/README.md#L1); [Broker-book update](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python/blob/fd119b12b7f5176d4d5274120edaad2c59b2b5b8/src/ordermgmt/ZerodhaOrderManager.py#L92); [Partial-cancel rewrite](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python/blob/fd119b12b7f5176d4d5274120edaad2c59b2b5b8/src/ordermgmt/ZerodhaOrderManager.py#L113).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
