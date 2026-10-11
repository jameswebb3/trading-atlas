# 0xArchive SDK — Snapshots and diffs are distinct evidence

**Decision question:** Can an L2 book be reconstructed from diffs without a valid baseline?

| Field | Review |
| --- | --- |
| Upstream | [0xArchiveIO/sdk-typescript](https://github.com/0xArchiveIO/sdk-typescript) |
| Primary area | Execution & Exchange Integration |
| Source commit | [51ae3754607a54b63c70a7f71c09af3524c06aec](https://github.com/0xArchiveIO/sdk-typescript/commit/51ae3754607a54b63c70a7f71c09af3524c06aec) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/0xArchiveIO/sdk-typescript/blob/51ae3754607a54b63c70a7f71c09af3524c06aec/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The L2 resource presents snapshot, history, and diff endpoints as separate operations, making the reconstruction inputs explicit. An SDK interface does not prove gap-free sequencing or historical coverage. |

## What this project does

A TypeScript client for a hosted Hyperliquid and Lighter market-data API. [Project README](https://github.com/0xArchiveIO/sdk-typescript/blob/51ae3754607a54b63c70a7f71c09af3524c06aec/README.md#L5).

## Mechanism inspected

The L2 resource presents snapshot, history, and diff endpoints as separate operations, making the reconstruction inputs explicit. [Implementation](https://github.com/0xArchiveIO/sdk-typescript/blob/51ae3754607a54b63c70a7f71c09af3524c06aec/src/resources/l2-orderbook.ts#L33).

## Limitation that matters

An SDK interface does not prove gap-free sequencing or historical coverage. A hosted API also creates provider dependency and cannot replace an independently checked raw-data lineage. This is a source review, not a runtime or security test.

## Practical check for a trading system

Require a snapshot identity, contiguous diff sequence, and gap/reset handling for any reconstructed book.

## Why this score

Its resource separation is useful for data contracts; the hosted service itself is not an approved data source.

## Source trail

[README](https://github.com/0xArchiveIO/sdk-typescript/blob/51ae3754607a54b63c70a7f71c09af3524c06aec/README.md#L5); [Implementation](https://github.com/0xArchiveIO/sdk-typescript/blob/51ae3754607a54b63c70a7f71c09af3524c06aec/src/resources/l2-orderbook.ts#L33) - [License](https://github.com/0xArchiveIO/sdk-typescript/blob/51ae3754607a54b63c70a7f71c09af3524c06aec/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
