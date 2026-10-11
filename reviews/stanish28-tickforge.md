# TickForge — Count replay rejections separately from throughput

**Decision question:** Does a deterministic replay distinguish events handled from events rejected?

| Field | Review |
| --- | --- |
| Upstream | [stanish28/TickForge](https://github.com/stanish28/TickForge) |
| Primary area | Market Data & Ingestion |
| Source commit | [15a960c3f7a4ecbc619b42fd4901a7af70ddc5a4](https://github.com/stanish28/TickForge/commit/15a960c3f7a4ecbc619b42fd4901a7af70ddc5a4) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 3/3: README, relevant source, and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Its replay loop preserves input order through a bounded SPSC queue and reports processed and rejected events separately from timing and final book state. The inspected determinism tests use a short synthetic sequence and compare final summaries; they do not prove real-feed completeness or venue-accurate fills. No root license was found at the pinned commit. |

## What this project does

TickForge is a small C++ market-data replay and limit-order-book experiment with paced and two-thread maximum-throughput modes. [Project README](https://github.com/stanish28/TickForge/blob/15a960c3f7a4ecbc619b42fd4901a7af70ddc5a4/README.md#L1).

## Mechanism inspected

In maximum mode, one producer places events into a bounded ring and one consumer applies them in file order, incrementing processed and rejected counters separately. The tests compare final summaries for the same short event sequence and require zero rejections on a sample. [Replay engine](https://github.com/stanish28/TickForge/blob/15a960c3f7a4ecbc619b42fd4901a7af70ddc5a4/src/replay_engine.cpp#L54).

## Limitation that matters

Throughput excludes CSV parsing and producer waiting from the per-event hot-path measurement. Equal final book summaries on a small sequence do not certify every intermediate event or a real exchange feed. This is a source review, not a runtime or security test.

## Practical check for a trading system

For market replay, report attempted, applied and rejected events with reasons; require the expected conservation identity and fail a study when rejected events are unexplained.

## Why this score

3/5 because distinct processed/rejected counts are useful for market-feed replay, while the small synthetic tests and missing license limit its value as an adoption reference.

## Source trail

[README](https://github.com/stanish28/TickForge/blob/15a960c3f7a4ecbc619b42fd4901a7af70ddc5a4/README.md#L3); [Replay engine](https://github.com/stanish28/TickForge/blob/15a960c3f7a4ecbc619b42fd4901a7af70ddc5a4/src/replay_engine.cpp#L54); [Determinism tests](https://github.com/stanish28/TickForge/blob/15a960c3f7a4ecbc619b42fd4901a7af70ddc5a4/tests/test_replay_determinism.cpp#L41).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
