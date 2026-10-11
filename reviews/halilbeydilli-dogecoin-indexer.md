# Dogecoin Indexer - Which write marks an indexed batch as committed?

**Decision question:** Which write marks an indexed batch as committed?

| Field | Review |
| --- | --- |
| Upstream | [halilbeydilli/dogecoin-indexer](https://github.com/halilbeydilli/dogecoin-indexer) |
| Primary area | Market Data & Ingestion |
| Source commit | [281e015163fc1719178535f7e9d6b79ec64eac1d](https://github.com/halilbeydilli/dogecoin-indexer/commit/281e015163fc1719178535f7e9d6b79ec64eac1d) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The indexer writes undo data and derived rows before advancing sync state, then checks stored block hashes for reorganization on live cycles. The pattern is tied to UTXO block effects and MongoDB writes; it does not define the publication clock of a trading feature. |

## What this project does

A UTXO indexer with startup cleanup and block-undo records.

## Mechanism inspected

The indexer writes undo data and derived rows before advancing sync state, then checks stored block hashes for reorganization on live cycles.

## Limitation that matters

The pattern is tied to UTXO block effects and MongoDB writes; it does not define the publication clock of a trading feature.

## Practical check for a trading system

Write recovery evidence before progress markers and verify a restarted collector cannot silently skip a partial batch.

## Why this score

3/5. The commit-marker ordering provides a concrete crash-recovery reference for data collectors.

## Source trail

[README](https://github.com/halilbeydilli/dogecoin-indexer/blob/281e015163fc1719178535f7e9d6b79ec64eac1d/README.md#L1); [internal/indexer/indexer.go](https://github.com/halilbeydilli/dogecoin-indexer/blob/281e015163fc1719178535f7e9d6b79ec64eac1d/internal/indexer/indexer.go#L792); [Root license](https://github.com/halilbeydilli/dogecoin-indexer/blob/281e015163fc1719178535f7e9d6b79ec64eac1d/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
