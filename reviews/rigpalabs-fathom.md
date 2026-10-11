# fathom — A plausible L2 snapshot can silently lose levels

**Decision question:** What happens when one Hyperliquid book level cannot be parsed?

| Field | Review |
| --- | --- |
| Upstream | [RigpaLabs/fathom](https://github.com/RigpaLabs/fathom) |
| Primary area | Market Data & Ingestion |
| Source commit | [7b6574293f7195a9212e315f32b9d930c760ee20](https://github.com/RigpaLabs/fathom/commit/7b6574293f7195a9212e315f32b9d930c760ee20) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/RigpaLabs/fathom/blob/7b6574293f7195a9212e315f32b9d930c760ee20/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The HL parser drops individual levels whose price or size fails numeric parsing, then persists the reduced snapshot and derives best bid/ask and OFI from it. HL messages are full snapshots here, with time used as a pseudo sequence; the inspected schema does not retain local receipt time, so completeness and decision availability need separate checks. |

## What this project does

Rust multi-exchange L2 collector with raw and one-second Parquet paths. [README](https://github.com/RigpaLabs/fathom/blob/7b6574293f7195a9212e315f32b9d930c760ee20/README.md).

## Mechanism inspected

The HL parser drops individual levels whose price or size fails numeric parsing, then persists the reduced snapshot and derives best bid/ask and OFI from it. [Implementation](https://github.com/RigpaLabs/fathom/blob/7b6574293f7195a9212e315f32b9d930c760ee20/src/connection/hyperliquid.rs#L35-L65). [Related implementation](https://github.com/RigpaLabs/fathom/blob/7b6574293f7195a9212e315f32b9d930c760ee20/src/connection/hyperliquid.rs#L333-L409).

## Limitation that matters

HL messages are full snapshots here, with time used as a pseudo sequence; the inspected schema does not retain local receipt time, so completeness and decision availability need separate checks. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Reject or quarantine a malformed whole snapshot and record receipt and validation state before it enters a trading feature.

## Why this score

The HL parser drops individual levels whose price or size fails numeric parsing, then persists the reduced snapshot and derives best bid/ask and OFI from it. HL messages are full snapshots here, with time used as a pseudo sequence; the inspected schema does not retain local receipt time, so completeness and decision availability need separate checks.

## Source trail

[README](https://github.com/RigpaLabs/fathom/blob/7b6574293f7195a9212e315f32b9d930c760ee20/README.md) · [Implementation](https://github.com/RigpaLabs/fathom/blob/7b6574293f7195a9212e315f32b9d930c760ee20/src/connection/hyperliquid.rs#L35-L65) · [Related implementation](https://github.com/RigpaLabs/fathom/blob/7b6574293f7195a9212e315f32b9d930c760ee20/src/connection/hyperliquid.rs#L333-L409) · [License](https://github.com/RigpaLabs/fathom/blob/7b6574293f7195a9212e315f32b9d930c760ee20/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
