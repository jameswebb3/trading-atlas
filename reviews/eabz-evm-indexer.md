# evm-indexer - When should an indexer refuse to repair a deep chain reorganization?

**Decision question:** When should an indexer refuse to repair a deep chain reorganization?

| Field | Review |
| --- | --- |
| Upstream | [eabz/evm-indexer](https://github.com/eabz/evm-indexer) |
| Primary area | Market Data & Ingestion |
| Source commit | [e4ca46486837b85aadccd009ca742f1799801a67](https://github.com/eabz/evm-indexer/commit/e4ca46486837b85aadccd009ca742f1799801a67) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | The reorg guard compares a stored block hash with the incoming chain and raises an error when the rollback depth exceeds a configured maximum. The bound protects against destructive automatic rewrites, but data inside the confirmation window is still delayed and consumers need epoch-aware validity. |

## What this project does

A SQL indexer for EVM chains with explicit fork detection and rollback.

## Mechanism inspected

The reorg guard compares a stored block hash with the incoming chain and raises an error when the rollback depth exceeds a configured maximum.

## Limitation that matters

The bound protects against destructive automatic rewrites, but data inside the confirmation window is still delayed and consumers need epoch-aware validity.

## Practical check for a trading system

Expose canonical hash, repair epoch and finality policy with every on-chain-derived feature.

## Why this score

4/5. The fail-closed depth bound is a strong data-correctness pattern for mutable chain history.

## Source trail

[README](https://github.com/eabz/evm-indexer/blob/e4ca46486837b85aadccd009ca742f1799801a67/README.md#L1); [docs/design.md](https://github.com/eabz/evm-indexer/blob/e4ca46486837b85aadccd009ca742f1799801a67/docs/design.md#L1); [src/reorg/guard.rs](https://github.com/eabz/evm-indexer/blob/e4ca46486837b85aadccd009ca742f1799801a67/src/reorg/guard.rs#L242); [Root license](https://github.com/eabz/evm-indexer/blob/e4ca46486837b85aadccd009ca742f1799801a67/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
