# Aster and HL Bot — A local lock timeout is not an exchange ACK

**Decision question:** Can a timed unlock race with an unresolved cancel?

| Field | Review |
| --- | --- |
| Upstream | [mooncitydev/asterdex-hl-trading-bot](https://github.com/mooncitydev/asterdex-hl-trading-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [c57ab477f85a45e7b764202ab3b617ca042170d2](https://github.com/mooncitydev/asterdex-hl-trading-bot/commit/c57ab477f85a45e7b764202ab3b617ca042170d2) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The order coordinator releases a local operation lock and clears its pending marker after a fixed three-second timer. A venue request can remain unresolved beyond the timer. |

## What this project does

A Bun-based perpetual trading workstation for Aster and Hyperliquid. [Project README](https://github.com/mooncitydev/asterdex-hl-trading-bot/blob/c57ab477f85a45e7b764202ab3b617ca042170d2/README.md#L5).

## Mechanism inspected

The order coordinator releases a local operation lock and clears its pending marker after a fixed three-second timer. [Implementation](https://github.com/mooncitydev/asterdex-hl-trading-bot/blob/c57ab477f85a45e7b764202ab3b617ca042170d2/src/core/order-coordinator.ts#L48). [Related source 1](https://github.com/mooncitydev/asterdex-hl-trading-bot/blob/c57ab477f85a45e7b764202ab3b617ca042170d2/src/strategy/maker-engine.ts#L329).

## Limitation that matters

A venue request can remain unresolved beyond the timer. Clearing local state does not prove the order was cancelled or safe to replace. This is a source review, not a runtime or security test.

## Practical check for a trading system

Keep pending intent until exchange status or a reconciled timeout outcome is known; inject delayed ACK and cancel races.

## Why this score

Directly relevant execution race, but its timed local release is a counterexample rather than a safe template.

## Source trail

[README](https://github.com/mooncitydev/asterdex-hl-trading-bot/blob/c57ab477f85a45e7b764202ab3b617ca042170d2/README.md#L5); [Implementation](https://github.com/mooncitydev/asterdex-hl-trading-bot/blob/c57ab477f85a45e7b764202ab3b617ca042170d2/src/core/order-coordinator.ts#L48); [Related source 1](https://github.com/mooncitydev/asterdex-hl-trading-bot/blob/c57ab477f85a45e7b764202ab3b617ca042170d2/src/strategy/maker-engine.ts#L329).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
