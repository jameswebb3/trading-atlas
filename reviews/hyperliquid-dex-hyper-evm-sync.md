# hyper-evm-sync - Can reconstructed chain states be compared deterministically?

**Decision question:** Can reconstructed chain states be compared deterministically?

| Field | Review |
| --- | --- |
| Upstream | [hyperliquid-dex/hyper-evm-sync](https://github.com/hyperliquid-dex/hyper-evm-sync) |
| Primary area | Data Quality & Lineage |
| Source commit | [d0945c699d9d4774417f4355b10744e7cd420df8](https://github.com/hyperliquid-dex/hyper-evm-sync/commit/d0945c699d9d4774417f4355b10744e7cd420df8) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Executive assessment | It hashes sorted accounts, contracts, storage and block hashes into separate digests. This concerns HyperEVM state, not perpetual order execution; block-hash pruning affects a digest. |

## What this project does

A HyperEVM sync component with an in-memory state representation.

## Mechanism inspected

It hashes sorted accounts, contracts, storage and block hashes into separate digests.

## Limitation that matters

This concerns HyperEVM state, not perpetual order execution; block-hash pruning affects a digest.

## Practical check for a trading system

Use deterministic digests for replay comparison only with canonical inputs.

## Why this score

2/5. Concrete integrity method, but adjacent product scope.

## Source trail

[README](https://github.com/hyperliquid-dex/hyper-evm-sync/blob/d0945c699d9d4774417f4355b10744e7cd420df8/README.md#L1); [src/state.rs](https://github.com/hyperliquid-dex/hyper-evm-sync/blob/d0945c699d9d4774417f4355b10744e7cd420df8/src/state.rs#L18).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
