# Openfort Hyperliquid Recipe - Does an accepted order response prove that all fills were reconciled?

**Decision question:** Does an accepted order response prove that all fills were reconciled?

| Field | Review |
| --- | --- |
| Upstream | [openfort-xyz/recipes-hub](https://github.com/openfort-xyz/recipes-hub) |
| Primary area | Execution & Exchange Integration |
| Source commit | [c4d3daa3d979a2d50e104f94534b3b4b67952908](https://github.com/openfort-xyz/recipes-hub/commit/c4d3daa3d979a2d50e104f94534b3b4b67952908) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The result handler distinguishes filled, resting and error statuses, then queries recent fills for a filled order ID. The fill query returns null on a miss or API error, yet the handler still returns filled status and the response average. This is spot-only. |

## What this project does

A wallet integration recipe that submits HYPE spot orders through Hyperliquid.

## Mechanism inspected

The result handler distinguishes filled, resting and error statuses, then queries recent fills for a filled order ID.

## Limitation that matters

The fill query returns null on a miss or API error, yet the handler still returns filled status and the response average. This is spot-only.

## Practical check for a trading system

Keep response status separate from account-side fill evidence and record a reconciliation failure.

## Why this score

2/5. Useful order-state branching, but the optional fill lookup is not a completion certificate.

## Source trail

[README](https://github.com/openfort-xyz/recipes-hub/blob/c4d3daa3d979a2d50e104f94534b3b4b67952908/README.md#L1); [hyperliquid/services/HyperliquidClient.ts](https://github.com/openfort-xyz/recipes-hub/blob/c4d3daa3d979a2d50e104f94534b3b4b67952908/hyperliquid/services/HyperliquidClient.ts#L588); [hyperliquid/services/HyperliquidClient.ts](https://github.com/openfort-xyz/recipes-hub/blob/c4d3daa3d979a2d50e104f94534b3b4b67952908/hyperliquid/services/HyperliquidClient.ts#L625); [hyperliquid/services/HyperliquidClient.ts](https://github.com/openfort-xyz/recipes-hub/blob/c4d3daa3d979a2d50e104f94534b3b4b67952908/hyperliquid/services/HyperliquidClient.ts#L111); [hyperliquid/services/HyperliquidClient.ts](https://github.com/openfort-xyz/recipes-hub/blob/c4d3daa3d979a2d50e104f94534b3b4b67952908/hyperliquid/services/HyperliquidClient.ts#L127).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
