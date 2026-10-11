# ferrofluid - Can a CLOID lookup survive an execution-process restart?

**Decision question:** Can a CLOID lookup survive an execution-process restart?

| Field | Review |
| --- | --- |
| Upstream | [ControlCplusControlV/ferrofluid](https://github.com/ControlCplusControlV/ferrofluid) |
| Primary area | Execution & Exchange Integration |
| Source commit | [a3a3f74cba3c5e88d3960e72f5d81ff69bc18d07](https://github.com/ControlCplusControlV/ferrofluid/commit/a3a3f74cba3c5e88d3960e72f5d81ff69bc18d07) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The tracker associates client order IDs with requests, timestamps, statuses and exchange responses in a shared in-memory map. There is no durable store in the inspected tracker, so a restarted process loses its order identity map. |

## What this project does

A Rust Hyperliquid provider and strategy framework.

## Mechanism inspected

The tracker associates client order IDs with requests, timestamps, statuses and exchange responses in a shared in-memory map.

## Limitation that matters

There is no durable store in the inspected tracker, so a restarted process loses its order identity map.

## Practical check for a trading system

Persist each intent and outcome before submission and reconcile CLOIDs against exchange state after restart.

## Why this score

2/5. CLOID identity is explicit, but process-local state is insufficient for live recovery.

## Source trail

[README](https://github.com/ControlCplusControlV/ferrofluid/blob/a3a3f74cba3c5e88d3960e72f5d81ff69bc18d07/README.md#L1); [src/providers/order_tracker.rs](https://github.com/ControlCplusControlV/ferrofluid/blob/a3a3f74cba3c5e88d3960e72f5d81ff69bc18d07/src/providers/order_tracker.rs#L38); [Root license](https://github.com/ControlCplusControlV/ferrofluid/blob/a3a3f74cba3c5e88d3960e72f5d81ff69bc18d07/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
