# BEC - Can an order intent survive an uncertain submission?

**Decision question:** Can an order intent survive an uncertain submission?

| Field | Review |
| --- | --- |
| Upstream | [jptsantossilva/BEC](https://github.com/jptsantossilva/BEC) |
| Primary area | Execution & Exchange Integration |
| Source commit | [923386c7757275caeab6632ef89a99b4751be840](https://github.com/jptsantossilva/BEC/commit/923386c7757275caeab6632ef89a99b4751be840) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | It creates a durable intent before submitting and marks uncertain failures for later reconciliation. It targets spot venues, so Hyperliquid perps identity and partial fills need their own implementation. |

## What this project does

A spot trading application with gated live intents and reconciliation.

## Mechanism inspected

It creates a durable intent before submitting and marks uncertain failures for later reconciliation.

## Limitation that matters

It targets spot venues, so Hyperliquid perps identity and partial fills need their own implementation.

## Practical check for a trading system

Persist intent before network I/O and reconcile unknown outcomes before retry.

## Why this score

3/5. Relevant durable-intent pattern with different venue semantics.

## Source trail

[README](https://github.com/jptsantossilva/BEC/blob/923386c7757275caeab6632ef89a99b4751be840/README.md#L1); [docs/index.md](https://github.com/jptsantossilva/BEC/blob/923386c7757275caeab6632ef89a99b4751be840/docs/index.md#L1); [bec/exchanges/live_execution.py](https://github.com/jptsantossilva/BEC/blob/923386c7757275caeab6632ef89a99b4751be840/bec/exchanges/live_execution.py#L405); [Root license](https://github.com/jptsantossilva/BEC/blob/923386c7757275caeab6632ef89a99b4751be840/LICENSE.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
