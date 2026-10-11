# dPro Hyperliquid — Explicit market namespace, unsafe key onboarding

**Decision question:** What must be checked before an agent signs a Hyperliquid order?

| Field | Review |
| --- | --- |
| Upstream | [dProLabs/dpro-hyperliquid](https://github.com/dProLabs/dpro-hyperliquid) |
| Primary area | Execution & Exchange Integration |
| Source commit | [eee6fb730c29a5ee036e1b242ff695d7be608355](https://github.com/dProLabs/dpro-hyperliquid/commit/eee6fb730c29a5ee036e1b242ff695d7be608355) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The trade command rejects read-only accounts and requires an explicit market namespace before signing. The tutorial proposes supplying an API wallet private key in conversation, and the nonce manager is process-local; neither is a safe credential or crash-recovery model. |

## What this project does

An agent-facing Hyperliquid skill covering reads and spot, perpetual, and HIP-3 trading. [Project README](https://github.com/dProLabs/dpro-hyperliquid/blob/eee6fb730c29a5ee036e1b242ff695d7be608355/README.md#L1).

## Mechanism inspected

The trade command rejects read-only accounts and requires an explicit market namespace before signing. [Implementation](https://github.com/dProLabs/dpro-hyperliquid/blob/eee6fb730c29a5ee036e1b242ff695d7be608355/scripts/commands/trade.mjs#L33). [Related source 1](https://github.com/dProLabs/dpro-hyperliquid/blob/eee6fb730c29a5ee036e1b242ff695d7be608355/docs/tutorial-04-trading-desk.md#L18). [Related source 2](https://github.com/dProLabs/dpro-hyperliquid/blob/eee6fb730c29a5ee036e1b242ff695d7be608355/scripts/clients/nonce-manager.mjs#L1).

## Limitation that matters

The tutorial proposes supplying an API wallet private key in conversation, and the nonce manager is process-local; neither is a safe credential or crash-recovery model. This is a source review, not a runtime or security test.

## Practical check for a trading system

Keep keys outside the conversational context; require explicit market class and durable signing controls.

## Why this score

The namespace check is useful, but key handling and agent write access are serious adoption limits.

## Source trail

[README](https://github.com/dProLabs/dpro-hyperliquid/blob/eee6fb730c29a5ee036e1b242ff695d7be608355/README.md#L1); [Implementation](https://github.com/dProLabs/dpro-hyperliquid/blob/eee6fb730c29a5ee036e1b242ff695d7be608355/scripts/commands/trade.mjs#L33); [Related source 1](https://github.com/dProLabs/dpro-hyperliquid/blob/eee6fb730c29a5ee036e1b242ff695d7be608355/docs/tutorial-04-trading-desk.md#L18); [Related source 2](https://github.com/dProLabs/dpro-hyperliquid/blob/eee6fb730c29a5ee036e1b242ff695d7be608355/scripts/clients/nonce-manager.mjs#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
