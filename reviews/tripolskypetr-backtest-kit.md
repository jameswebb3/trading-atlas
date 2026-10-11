# backtest-kit - Is order-not-found the same as a confirmed terminal outcome?

**Decision question:** Is order-not-found the same as a confirmed terminal outcome?

| Field | Review |
| --- | --- |
| Upstream | [tripolskypetr/backtest-kit](https://github.com/tripolskypetr/backtest-kit) |
| Primary area | Execution & Exchange Integration |
| Source commit | [550238b5bbbeb93847e29ec96cfd62f0fafa5881](https://github.com/tripolskypetr/backtest-kit/commit/550238b5bbbeb93847e29ec96cfd62f0fafa5881) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The contract describes separate transient, deleted and rejected outcomes and a startup orphan sweep. This is interface guidance; the inspected file does not establish a working orphan sweep or fill confirmation. |

## What this project does

A backtest toolkit with a broker adapter interface for live order callbacks.

## Mechanism inspected

The contract describes separate transient, deleted and rejected outcomes and a startup orphan sweep.

## Limitation that matters

This is interface guidance; the inspected file does not establish a working orphan sweep or fill confirmation.

## Practical check for a trading system

Turn outcome classes into adapter tests against real account evidence.

## Why this score

2/5. Useful taxonomy, limited implementation evidence.

## Source trail

[README](https://github.com/tripolskypetr/backtest-kit/blob/550238b5bbbeb93847e29ec96cfd62f0fafa5881/README.md#L1); [docs/index.md](https://github.com/tripolskypetr/backtest-kit/blob/550238b5bbbeb93847e29ec96cfd62f0fafa5881/docs/index.md#L1); [src/classes/Broker.ts](https://github.com/tripolskypetr/backtest-kit/blob/550238b5bbbeb93847e29ec96cfd62f0fafa5881/src/classes/Broker.ts#L918); [Root license](https://github.com/tripolskypetr/backtest-kit/blob/550238b5bbbeb93847e29ec96cfd62f0fafa5881/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
