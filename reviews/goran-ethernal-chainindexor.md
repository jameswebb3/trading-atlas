# ChainIndexor - Will an indexer detect a changed block before publishing data?

**Decision question:** Will an indexer detect a changed block before publishing data?

| Field | Review |
| --- | --- |
| Upstream | [goran-ethernal/ChainIndexor](https://github.com/goran-ethernal/ChainIndexor) |
| Primary area | Data Quality & Lineage |
| Source commit | [cf1cde7fc4c0fdcbaf0228e5a4e7982034ed1dbe](https://github.com/goran-ethernal/ChainIndexor/commit/cf1cde7fc4c0fdcbaf0228e5a4e7982034ed1dbe) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | It compares incoming headers and logs with stored hashes inside a DB transaction and returns an explicit reorg error. Detection alone does not retract already derived features. |

## What this project does

An EVM log indexer with a reorg detector and stored block hashes.

## Mechanism inspected

It compares incoming headers and logs with stored hashes inside a DB transaction and returns an explicit reorg error.

## Limitation that matters

Detection alone does not retract already derived features.

## Practical check for a trading system

Attach canonical block hash and finality state to observations and retract derived records after reorg.

## Why this score

4/5. Source revision becomes visible rather than silently rewriting history.

## Source trail

[README](https://github.com/goran-ethernal/ChainIndexor/blob/cf1cde7fc4c0fdcbaf0228e5a4e7982034ed1dbe/README.md#L1); [internal/reorg/reorg_detector.go](https://github.com/goran-ethernal/ChainIndexor/blob/cf1cde7fc4c0fdcbaf0228e5a4e7982034ed1dbe/internal/reorg/reorg_detector.go#L132); [internal/reorg/reorg_detector.go](https://github.com/goran-ethernal/ChainIndexor/blob/cf1cde7fc4c0fdcbaf0228e5a4e7982034ed1dbe/internal/reorg/reorg_detector.go#L138); [Root license](https://github.com/goran-ethernal/ChainIndexor/blob/cf1cde7fc4c0fdcbaf0228e5a4e7982034ed1dbe/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
