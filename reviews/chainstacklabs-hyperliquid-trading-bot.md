# Chainstack Hyperliquid Trading Bot - What happens when a protective order vanishes while a position remains open?

**Decision question:** What happens when a protective order vanishes while a position remains open?

| Field | Review |
| --- | --- |
| Upstream | [chainstacklabs/hyperliquid-trading-bot](https://github.com/chainstacklabs/hyperliquid-trading-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [7e930aa6b0d296f029943834c2133beff6174d80](https://github.com/chainstacklabs/hyperliquid-trading-bot/commit/7e930aa6b0d296f029943834c2133beff6174d80) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Checks a live position for vanished protective orders and attempts to re-arm them. A skipped fill snapshot still needs independent missed-fill reconciliation. |

## What this project does

An extensible Hyperliquid grid bot with a risk engine, user-fill stream and grouped take-profit/stop-loss orders.

## Mechanism inspected

The engine ignores the initial historical userFills snapshot, records live fills, and periodically compares registered trigger order IDs with venue open orders and the current position. If protection is missing, it re-arms after a recent-fill debounce.

## Limitation that matters

Skipping the snapshot avoids replaying old fill actions but does not itself book fills missed while offline. A failed venue query skips recovery for that cycle, and the shown path does not certify restart reconciliation.

## Practical check for a trading system

Test fill-before-ACK, external trigger cancellation and reconnect ordering against venue position and open-order truth.

## Why this score

4/5. A directly relevant protective-order recovery path is visible, with explicit race mitigation and clear restart boundaries.

## Source trail

[README](https://github.com/chainstacklabs/hyperliquid-trading-bot/blob/7e930aa6b0d296f029943834c2133beff6174d80/README.md#L1); [src/core/engine.py](https://github.com/chainstacklabs/hyperliquid-trading-bot/blob/7e930aa6b0d296f029943834c2133beff6174d80/src/core/engine.py#L431); [src/core/engine.py](https://github.com/chainstacklabs/hyperliquid-trading-bot/blob/7e930aa6b0d296f029943834c2133beff6174d80/src/core/engine.py#L621); [src/core/engine.py](https://github.com/chainstacklabs/hyperliquid-trading-bot/blob/7e930aa6b0d296f029943834c2133beff6174d80/src/core/engine.py#L652); [License text](https://github.com/chainstacklabs/hyperliquid-trading-bot/blob/7e930aa6b0d296f029943834c2133beff6174d80/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
