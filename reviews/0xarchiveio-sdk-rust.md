# 0xArchive Rust SDK — A reconstructable book can still contain gaps

**Decision question:** Does L2 replay stop when delta sequence is discontinuous?

| Field | Review |
| --- | --- |
| Upstream | [0xArchive Rust SDK](https://github.com/0xArchiveIO/sdk-rust) |
| Primary area | Market Data & Ingestion |
| Source commit | [b219352189083dca6995eacd0447794df8b500f0](https://github.com/0xArchiveIO/sdk-rust/commit/b219352189083dca6995eacd0447794df8b500f0) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/0xArchiveIO/sdk-rust/blob/b219352189083dca6995eacd0447794df8b500f0/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | It resets from a checkpoint and sorts deltas before applying them; a separate detect_gaps function reports missing sequence numbers. The reconstruction methods do not call detect_gaps, so a plausible snapshot may be emitted despite missing deltas. Availability and coverage of the upstream service are unverified. |

## What this project does

A typed client for commercial Hyperliquid and Lighter data; the inspected reconstruction implementation is for Lighter, not HL. [README](https://github.com/0xArchiveIO/sdk-rust/blob/b219352189083dca6995eacd0447794df8b500f0/README.md).

## Mechanism inspected

It resets from a checkpoint and sorts deltas before applying them; a separate detect_gaps function reports missing sequence numbers. [Implementation](https://github.com/0xArchiveIO/sdk-rust/blob/b219352189083dca6995eacd0447794df8b500f0/src/orderbook_reconstructor.rs#L222-L317).

## Limitation that matters

The reconstruction methods do not call detect_gaps, so a plausible snapshot may be emitted despite missing deltas. Availability and coverage of the upstream service are unverified. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Gate local L2 reconstruction on checkpoint identity and contiguous sequences; emit unknown instead of a book after a gap.

## Why this score

Direct trading-system relevance: It resets from a checkpoint and sorts deltas before applying them; a separate detect_gaps function reports missing sequence numbers. The reconstruction methods do not call detect_gaps, so a plausible snapshot may be emitted despite missing deltas. Availability and coverage of the upstream service are unverified.

## Source trail

[README](https://github.com/0xArchiveIO/sdk-rust/blob/b219352189083dca6995eacd0447794df8b500f0/README.md) · [Implementation](https://github.com/0xArchiveIO/sdk-rust/blob/b219352189083dca6995eacd0447794df8b500f0/src/orderbook_reconstructor.rs#L222-L317).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
