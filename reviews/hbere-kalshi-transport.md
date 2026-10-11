# kalshi-transport - What survives a crash between order intent and exchange response?

**Decision question:** What survives a crash between order intent and exchange response?

| Field | Review |
| --- | --- |
| Upstream | [hbere/kalshi-transport](https://github.com/hbere/kalshi-transport) |
| Primary area | Execution & Exchange Integration |
| Source commit | [e09974e177e91541e9cb6344f684594b76e6c749](https://github.com/hbere/kalshi-transport/commit/e09974e177e91541e9cb6344f684594b76e6c749) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The submitter writes a pending payload before POST and uses a stable client order ID to resolve duplicate submissions after restart. The 409 path can return a deduped result even when the best-effort order lookup fails, so duplicate rejection does not itself prove order state or fills. |

## What this project does

A small Kalshi REST and WebSocket transport with fee and submission helpers.

## Mechanism inspected

The submitter writes a pending payload before POST and uses a stable client order ID to resolve duplicate submissions after restart.

## Limitation that matters

The 409 path can return a deduped result even when the best-effort order lookup fails, so duplicate rejection does not itself prove order state or fills.

## Practical check for a trading system

Persist intent before send, then reconcile the exact client ID and fill history before new decisions.

## Why this score

3/5. The crash window is treated explicitly; completion evidence still needs independent reconciliation.

## Source trail

[README](https://github.com/hbere/kalshi-transport/blob/e09974e177e91541e9cb6344f684594b76e6c749/README.md#L1); [docs/backtesting.md](https://github.com/hbere/kalshi-transport/blob/e09974e177e91541e9cb6344f684594b76e6c749/docs/backtesting.md#L1); [kalshi_transport/idempotency.py](https://github.com/hbere/kalshi-transport/blob/e09974e177e91541e9cb6344f684594b76e6c749/kalshi_transport/idempotency.py#L176); [kalshi_transport/idempotency.py](https://github.com/hbere/kalshi-transport/blob/e09974e177e91541e9cb6344f684594b76e6c749/kalshi_transport/idempotency.py#L241); [Root license](https://github.com/hbere/kalshi-transport/blob/e09974e177e91541e9cb6344f684594b76e6c749/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
