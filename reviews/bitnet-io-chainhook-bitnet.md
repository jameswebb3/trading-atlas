# chainhook-bitnet - How should an indexer represent competing chain forks?

**Decision question:** How should an indexer represent competing chain forks?

| Field | Review |
| --- | --- |
| Upstream | [bitnet-io/chainhook-bitnet](https://github.com/bitnet-io/chainhook-bitnet) |
| Primary area | Data Quality & Lineage |
| Source commit | [00aa46a653b3aec0f9106186218502c8770cfa03](https://github.com/bitnet-io/chainhook-bitnet/commit/00aa46a653b3aec0f9106186218502c8770cfa03) |
| Reviewed | 2026-10-11 |
| Declared license | AGPL |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its scratch pad retains parent-linked headers, branches forks and emits canonical changes. Bitcoin confirmation rules cannot be copied to other chains or exchange feeds. |

## What this project does

A Bitcoin chainhook indexing SDK.

## Mechanism inspected

Its scratch pad retains parent-linked headers, branches forks and emits canonical changes.

## Limitation that matters

Bitcoin confirmation rules cannot be copied to other chains or exchange feeds.

## Practical check for a trading system

Model provisional and canonical chain observations explicitly.

## Why this score

3/5. Fork-aware indexing helps, with source-specific finality still required.

## Source trail

[README](https://github.com/bitnet-io/chainhook-bitnet/blob/00aa46a653b3aec0f9106186218502c8770cfa03/README.md#L1); [docs/getting-started.md](https://github.com/bitnet-io/chainhook-bitnet/blob/00aa46a653b3aec0f9106186218502c8770cfa03/docs/getting-started.md#L1); [components/chainhook-sdk/src/indexer/fork_scratch_pad.rs](https://github.com/bitnet-io/chainhook-bitnet/blob/00aa46a653b3aec0f9106186218502c8770cfa03/components/chainhook-sdk/src/indexer/fork_scratch_pad.rs#L41); [Root license](https://github.com/bitnet-io/chainhook-bitnet/blob/00aa46a653b3aec0f9106186218502c8770cfa03/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
