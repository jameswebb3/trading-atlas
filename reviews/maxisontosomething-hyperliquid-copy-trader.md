# Hyperliquid Copy Trader - Can position events be parsed before a copy trade is considered?

**Decision question:** Can position events be parsed before a copy trade is considered?

| Field | Review |
| --- | --- |
| Upstream | [MaxIsOntoSomething/Hyperliquid_Copy_Trader](https://github.com/MaxIsOntoSomething/Hyperliquid_Copy_Trader) |
| Primary area | Execution & Exchange Integration |
| Source commit | [78858611fd418bab5eb0e558ecd1145b3d66bc12](https://github.com/MaxIsOntoSomething/Hyperliquid_Copy_Trader/commit/78858611fd418bab5eb0e558ecd1145b3d66bc12) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The monitor refreshes target account state when fills arrive, then calls copy callbacks. It also has a separate position-update path meant to identify new and closed positions. The position handler calls positions.get on a list, then the broad event handler catches and logs the error; a live WebSocket does not prove these events were applied. |

## What this project does

A Hyperliquid wallet monitor and copy-trading engine with WebSocket subscriptions, position sizing and optional simulated execution.

## Mechanism inspected

The monitor refreshes target account state when fills arrive, then calls copy callbacks. It also has a separate position-update path meant to identify new and closed positions.

## Limitation that matters

The position handler calls positions.get on a list, then the broad event handler catches and logs the error; a live WebSocket does not prove these events were applied.

## Practical check for a trading system

Test fill-before-position and position-before-fill events, and assert every event is either applied or surfaced as an explicit failure before any copy order is sent.

## Why this score

2/5. It exposes a direct, source-visible event-handling failure that matters for copy execution, while the inspected path cannot be treated as a working reference.

## Source trail

[README](https://github.com/MaxIsOntoSomething/Hyperliquid_Copy_Trader/blob/78858611fd418bab5eb0e558ecd1145b3d66bc12/README.md#L1); [src/copy_engine/monitor.py](https://github.com/MaxIsOntoSomething/Hyperliquid_Copy_Trader/blob/78858611fd418bab5eb0e558ecd1145b3d66bc12/src/copy_engine/monitor.py#L133); [src/copy_engine/monitor.py](https://github.com/MaxIsOntoSomething/Hyperliquid_Copy_Trader/blob/78858611fd418bab5eb0e558ecd1145b3d66bc12/src/copy_engine/monitor.py#L106); [src/copy_engine/monitor.py](https://github.com/MaxIsOntoSomething/Hyperliquid_Copy_Trader/blob/78858611fd418bab5eb0e558ecd1145b3d66bc12/src/copy_engine/monitor.py#L101); [Root license](https://github.com/MaxIsOntoSomething/Hyperliquid_Copy_Trader/blob/78858611fd418bab5eb0e558ecd1145b3d66bc12/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
