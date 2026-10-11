# bytex - Can an account fill arrive on a channel other than the subscription name?

**Decision question:** Can an account fill arrive on a channel other than the subscription name?

| Field | Review |
| --- | --- |
| Upstream | [BYTEX-TRADE/bytex](https://github.com/BYTEX-TRADE/bytex) |
| Primary area | Execution & Exchange Integration |
| Source commit | [67b3e103043476a0490bb7afa146ec9ac339b116](https://github.com/BYTEX-TRADE/bytex/commit/67b3e103043476a0490bb7afa146ec9ac339b116) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | The private-stream handler subscribes to userEvents but reads fills from messages whose reply channel is user; it also separates order updates and private errors. The comment reports observed channel behavior, but this review did not independently replay venue messages or prove all terminal statuses. |

## What this project does

A C# trading engine with a Hyperliquid execution adapter.

## Mechanism inspected

The private-stream handler subscribes to userEvents but reads fills from messages whose reply channel is user; it also separates order updates and private errors.

## Limitation that matters

The comment reports observed channel behavior, but this review did not independently replay venue messages or prove all terminal statuses.

## Practical check for a trading system

Test private-stream channel names and fill delivery against raw captured messages before trusting a normalized order lifecycle.

## Why this score

4/5. A venue-specific silent-fill failure is documented at the exact dispatch point.

## Source trail

[README](https://github.com/BYTEX-TRADE/bytex/blob/67b3e103043476a0490bb7afa146ec9ac339b116/README.md#L1); [docs/README.md](https://github.com/BYTEX-TRADE/bytex/blob/67b3e103043476a0490bb7afa146ec9ac339b116/docs/README.md#L1); [src/Bytex.Adapters.Hyperliquid/HyperliquidExecutionClient.cs](https://github.com/BYTEX-TRADE/bytex/blob/67b3e103043476a0490bb7afa146ec9ac339b116/src/Bytex.Adapters.Hyperliquid/HyperliquidExecutionClient.cs#L361); [src/Bytex.Adapters.Hyperliquid/HyperliquidExecutionClient.cs](https://github.com/BYTEX-TRADE/bytex/blob/67b3e103043476a0490bb7afa146ec9ac339b116/src/Bytex.Adapters.Hyperliquid/HyperliquidExecutionClient.cs#L361); [Root license](https://github.com/BYTEX-TRADE/bytex/blob/67b3e103043476a0490bb7afa146ec9ac339b116/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
