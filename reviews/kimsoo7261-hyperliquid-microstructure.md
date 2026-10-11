# hyperliquid_microstructure — Carry timestamp provenance into L4 replay

**Decision question:** What evidence supports the timestamp assigned to an untimed Hyperliquid order-book diff?

| Field | Review |
| --- | --- |
| Upstream | [KimSoo7261/hyperliquid_microstructure](https://github.com/KimSoo7261/hyperliquid_microstructure) |
| Primary area | Market Data & Ingestion |
| Source commit | [5c1ee3488c9780b98e42f6077dd4d0434d52ce2a](https://github.com/KimSoo7261/hyperliquid_microstructure/commit/5c1ee3488c9780b98e42f6077dd4d0434d52ce2a) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant source and relevant test source inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | It reconstructs missing diff times from order-status and trade anchors, records the source of each assigned time, and marks re-emitted history after collector restarts. Recovered times can use later status or trade records and even backward-filled anchors; they are historical reconstructions, not available_at timestamps for live decisions. |

## What this project does

A research pipeline for public Hyperliquid L4 diffs, statuses and trades, producing book states, order lifecycles and fill-level microstructure tables. [Project README](https://github.com/KimSoo7261/hyperliquid_microstructure/blob/5c1ee3488c9780b98e42f6077dd4d0434d52ce2a/README.md#L1).

## Mechanism inspected

The timestamp recovery joins diff order IDs to open/cancel status and trades, demotes inconsistent anchors, detects long re-emitted runs, and records src codes for direct, trade-based and fallback times. The replay stage reports gap resets and skipped replayed rows. Tests cover mixed anchors, demotion and re-emitted history. [Timestamp reconstruction](https://github.com/KimSoo7261/hyperliquid_microstructure/blob/5c1ee3488c9780b98e42f6077dd4d0434d52ce2a/src/hlmicro/timestamps.py#L1).

## Limitation that matters

The resulting book time is inferred after the fact. Stage six also infers the aggressor when one or both order statuses are absent; such rows need their inference rule and uncertainty retained with downstream statistics. This is a source review, not a runtime or security test.

## Practical check for a trading system

Keep raw file order, reconstructed event_time, provenance code and observation/receipt time as separate fields. Exclude backfilled or inferred times from any live-causality claim unless an actual available_at receipt exists.

## Why this score

4/5 because explicit timestamp provenance, replayed-history detection and source tests address a direct Hyperliquid L4 research hazard; the reconstructed clock still cannot certify live causality.

## Source trail

[README](https://github.com/KimSoo7261/hyperliquid_microstructure/blob/5c1ee3488c9780b98e42f6077dd4d0434d52ce2a/README.md#L1); [Timestamp reconstruction](https://github.com/KimSoo7261/hyperliquid_microstructure/blob/5c1ee3488c9780b98e42f6077dd4d0434d52ce2a/src/hlmicro/timestamps.py#L1); [Recovery pipeline](https://github.com/KimSoo7261/hyperliquid_microstructure/blob/5c1ee3488c9780b98e42f6077dd4d0434d52ce2a/pipeline/04_recover_diff_timestamps.py#L1); [Replay accounting](https://github.com/KimSoo7261/hyperliquid_microstructure/blob/5c1ee3488c9780b98e42f6077dd4d0434d52ce2a/pipeline/05_replay_book.py#L68); [Inference tests](https://github.com/KimSoo7261/hyperliquid_microstructure/blob/5c1ee3488c9780b98e42f6077dd4d0434d52ce2a/tests/test_timestamps.py#L39); [Fill provenance](https://github.com/KimSoo7261/hyperliquid_microstructure/blob/5c1ee3488c9780b98e42f6077dd4d0434d52ce2a/pipeline/06_build_fills.py#L1); [License](https://github.com/KimSoo7261/hyperliquid_microstructure/blob/5c1ee3488c9780b98e42f6077dd4d0434d52ce2a/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
