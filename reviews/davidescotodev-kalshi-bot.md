# kalshi_bot - What does a kill switch prove when the account check fails?

**Decision question:** What does a kill switch prove when the account check fails?

| Field | Review |
| --- | --- |
| Upstream | [DavidEscotoDev/kalshi_bot](https://github.com/DavidEscotoDev/kalshi_bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [faf5d74740f833c8881707a35e79ad08c9037398](https://github.com/DavidEscotoDev/kalshi_bot/commit/faf5d74740f833c8881707a35e79ad08c9037398) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Triggers platform-wide cancellation after a failed balance check and counts per-order cancel successes. The fail-closed trigger is an attempt; completion still requires account-side verification that no resting orders remain. |

## What this project does

A Kalshi trading bot with balance monitoring, attempted mass cancellation, an execution engine and a local audit log.

## Mechanism inspected

The kill-switch path treats a failed balance read as a trigger and calls cancel_all_orders. That method enumerates resting orders and records a per-order successful cancellation count, rather than merely marking the alert handled.

## Limitation that matters

The fallback does not prove all orders were canceled: cancel_all_orders can itself fail or return fewer cancellations than resting orders. A trigger is therefore an attempted control action, and no account-side reconciliation after the cancellation loop was established in the inspected source.

## Practical check for a trading system

Report trigger, cancel requests, individual ACKs and a later account-side no-open-orders check as separate evidence states.

## Why this score

2/5 because A concrete fail-closed intent and per-order cancellation count are visible, but the path does not certify completion under the same API failure that invoked it.

## Source trail

[README kill-switch scope](https://github.com/DavidEscotoDev/kalshi_bot/blob/faf5d74740f833c8881707a35e79ad08c9037398/README.md#L20); [Cancellation count](https://github.com/DavidEscotoDev/kalshi_bot/blob/faf5d74740f833c8881707a35e79ad08c9037398/safety/kill_switch.py#L47); [Balance-failure branch](https://github.com/DavidEscotoDev/kalshi_bot/blob/faf5d74740f833c8881707a35e79ad08c9037398/safety/kill_switch.py#L106); [License](https://github.com/DavidEscotoDev/kalshi_bot/blob/faf5d74740f833c8881707a35e79ad08c9037398/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
