# hypertrader - How should an entry behave when a limit order is only partly filled?

**Decision question:** How should an entry behave when a limit order is only partly filled?

| Field | Review |
| --- | --- |
| Upstream | [darkerego/hypertrader](https://github.com/darkerego/hypertrader) |
| Primary area | Execution & Exchange Integration |
| Source commit | [55fa4161e8060f37953d3eefecfc984ea057d583](https://github.com/darkerego/hypertrader/commit/55fa4161e8060f37953d3eefecfc984ea057d583) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Reprices a working Hyperliquid entry and rechecks fills and open orders before an optional remainder fallback. A cancel/reconcile sequence still needs authoritative venue evidence under delayed fills. |

## What this project does

A Hyperliquid trading assistant with a repriced working limit order, optional market fallback and account-state checks.

## Mechanism inspected

The entry loop modifies one active order ID, rechecks position after ambiguous responses, then cancels and reconciles outstanding entry orders before sizing any optional market fallback for the remaining quantity.

## Limitation that matters

A live cancel/fill race is not eliminated by this control flow; it depends on the freshness and completeness of account/open-order queries. The optional market fallback can pay adverse slippage and must be a conscious execution policy. No root license was verified.

## Practical check for a trading system

Record initial order identity, each modify result, terminal cancel evidence and the final account position before releasing or replacing exposure.

## Why this score

3/5 because The source shows a concrete partial-entry reconciliation sequence, with unavoidable venue-state and fallback-cost uncertainty.

## Source trail

[README](https://github.com/darkerego/hypertrader/blob/55fa4161e8060f37953d3eefecfc984ea057d583/README.md#L172); [modes/position_management.py](https://github.com/darkerego/hypertrader/blob/55fa4161e8060f37953d3eefecfc984ea057d583/modes/position_management.py#L894); [modes/position_management.py](https://github.com/darkerego/hypertrader/blob/55fa4161e8060f37953d3eefecfc984ea057d583/modes/position_management.py#L940); [modes/position_management.py](https://github.com/darkerego/hypertrader/blob/55fa4161e8060f37953d3eefecfc984ea057d583/modes/position_management.py#L950); [modes/position_management.py](https://github.com/darkerego/hypertrader/blob/55fa4161e8060f37953d3eefecfc984ea057d583/modes/position_management.py#L1003).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
