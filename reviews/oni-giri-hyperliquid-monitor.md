# Hyperliquid Monitor — Callback delivery is not a durable fill tape

**Decision question:** Can a fill monitor recover after its WebSocket disconnects?

| Field | Review |
| --- | --- |
| Upstream | [Oni-giri/hyperliquid-monitor](https://github.com/Oni-giri/hyperliquid-monitor) |
| Primary area | Execution & Exchange Integration |
| Source commit | [b0e11cf830d446e8bb4cad5d3fba05de900a9a07](https://github.com/Oni-giri/hyperliquid-monitor/commit/b0e11cf830d446e8bb4cad5d3fba05de900a9a07) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/Oni-giri/hyperliquid-monitor/blob/b0e11cf830d446e8bb4cad5d3fba05de900a9a07/LICENSE.md#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The monitor dispatches fill events to a handler and can store records while holding a local synchronization lock. The inspected path does not show a durable cursor, trade-ID deduplication, or an exchange backfill after disconnection. |

## What this project does

A Hyperliquid address monitor with callbacks and optional SQLite persistence. [Project README](https://github.com/Oni-giri/hyperliquid-monitor/blob/b0e11cf830d446e8bb4cad5d3fba05de900a9a07/README.md#L5).

## Mechanism inspected

The monitor dispatches fill events to a handler and can store records while holding a local synchronization lock. [Implementation](https://github.com/Oni-giri/hyperliquid-monitor/blob/b0e11cf830d446e8bb4cad5d3fba05de900a9a07/src/hyperliquid_monitor/monitor.py#L60). [Related source 1](https://github.com/Oni-giri/hyperliquid-monitor/blob/b0e11cf830d446e8bb4cad5d3fba05de900a9a07/tests/test_monitor.py#L42).

## Limitation that matters

The inspected path does not show a durable cursor, trade-ID deduplication, or an exchange backfill after disconnection. This is a source review, not a runtime or security test.

## Practical check for a trading system

Persist fill identity and reconcile a bounded overlap window on every reconnect.

## Why this score

Useful callback structure, but insufficient evidence of complete historical fill capture.

## Source trail

[README](https://github.com/Oni-giri/hyperliquid-monitor/blob/b0e11cf830d446e8bb4cad5d3fba05de900a9a07/README.md#L5); [Implementation](https://github.com/Oni-giri/hyperliquid-monitor/blob/b0e11cf830d446e8bb4cad5d3fba05de900a9a07/src/hyperliquid_monitor/monitor.py#L60); [Related source 1](https://github.com/Oni-giri/hyperliquid-monitor/blob/b0e11cf830d446e8bb4cad5d3fba05de900a9a07/tests/test_monitor.py#L42) - [License](https://github.com/Oni-giri/hyperliquid-monitor/blob/b0e11cf830d446e8bb4cad5d3fba05de900a9a07/LICENSE.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
