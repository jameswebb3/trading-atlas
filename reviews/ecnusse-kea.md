# Kea - Can state-based tests recognize equivalent states without raw-screen equality?

**Decision question:** Can state-based tests recognize equivalent states without raw-screen equality?

| Field | Review |
| --- | --- |
| Upstream | [ecnusse/Kea](https://github.com/ecnusse/Kea) |
| Primary area | Testing & Verification |
| Source commit | [28b0b41249c56056e29e5c3b56d56babdc9b6773](https://github.com/ecnusse/Kea/commit/28b0b41249c56056e29e5c3b56d56babdc9b6773) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | DeviceState builds a content-free signature from activity and sorted view signatures, then hashes it for state identity. The hash deliberately drops content; two materially different UI states can collapse, just as two trading states can share a superficial status. |

## What this project does

A property-based Android GUI testing framework.

## Mechanism inspected

DeviceState builds a content-free signature from activity and sorted view signatures, then hashes it for state identity.

## Limitation that matters

The hash deliberately drops content; two materially different UI states can collapse, just as two trading states can share a superficial status.

## Practical check for a trading system

Define state identity from fields that matter to the invariant, and test collisions deliberately.

## Why this score

2/5. Its state-abstraction tradeoff is useful for order-lifecycle testing.

## Source trail

[README](https://github.com/ecnusse/Kea/blob/28b0b41249c56056e29e5c3b56d56babdc9b6773/README.md#L1); [kea/device_state.py](https://github.com/ecnusse/Kea/blob/28b0b41249c56056e29e5c3b56d56babdc9b6773/kea/device_state.py#L188); [kea/device_state.py](https://github.com/ecnusse/Kea/blob/28b0b41249c56056e29e5c3b56d56babdc9b6773/kea/device_state.py#L171); [kea/device_state.py](https://github.com/ecnusse/Kea/blob/28b0b41249c56056e29e5c3b56d56babdc9b6773/kea/device_state.py#L208).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
