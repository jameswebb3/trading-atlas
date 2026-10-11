# greenrock — A failed book fetch should not look like an empty book

**Decision question:** Can credentials or network failures be mistaken for zero market liquidity?

| Field | Review |
| --- | --- |
| Upstream | [pinsky-three/greenrock](https://github.com/pinsky-three/greenrock) |
| Primary area | Execution & Exchange Integration |
| Source commit | [315f930df7f954ae3dff454e22a1402fd7aa9e27](https://github.com/pinsky-three/greenrock/commit/315f930df7f954ae3dff454e22a1402fd7aa9e27) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/pinsky-three/greenrock/blob/315f930df7f954ae3dff454e22a1402fd7aa9e27/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The adapter returns an empty order list after credential/API errors and an empty OrderBook with update ID zero after book fetch failure. The observed branch is Binance-specific and may be unreachable in a configured run; it documents a failure shape, not a directly portable implementation. |

## What this project does

Rust trading engine with a Binance broker adapter and order-book retrieval. [README](https://github.com/pinsky-three/greenrock/blob/315f930df7f954ae3dff454e22a1402fd7aa9e27/README.md).

## Mechanism inspected

The adapter returns an empty order list after credential/API errors and an empty OrderBook with update ID zero after book fetch failure. [Implementation](https://github.com/pinsky-three/greenrock/blob/315f930df7f954ae3dff454e22a1402fd7aa9e27/crates/greenrock-engine/src/brokers/binance.rs#L178-L228).

## Limitation that matters

The observed branch is Binance-specific and may be unreachable in a configured run; it documents a failure shape, not a directly portable implementation. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Keep Unknown/Failed separate from genuinely empty book or account state and assert fail-closed behavior in the silent-failure zoo.

## Why this score

The adapter returns an empty order list after credential/API errors and an empty OrderBook with update ID zero after book fetch failure. The observed branch is Binance-specific and may be unreachable in a configured run; it documents a failure shape, not a directly portable implementation.

## Source trail

[README](https://github.com/pinsky-three/greenrock/blob/315f930df7f954ae3dff454e22a1402fd7aa9e27/README.md) · [Implementation](https://github.com/pinsky-three/greenrock/blob/315f930df7f954ae3dff454e22a1402fd7aa9e27/crates/greenrock-engine/src/brokers/binance.rs#L178-L228) · [License](https://github.com/pinsky-three/greenrock/blob/315f930df7f954ae3dff454e22a1402fd7aa9e27/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
