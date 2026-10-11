# oraclebook - What does a recorded-book replay actually reproduce?

**Decision question:** What does a recorded-book replay actually reproduce?

| Field | Review |
| --- | --- |
| Upstream | [jabrahamtech/oraclebook](https://github.com/jabrahamtech/oraclebook) |
| Primary area | Backtesting & Simulation |
| Source commit | [af1ab62c97eb088d9e772f6b96399b95d9ea57b3](https://github.com/jabrahamtech/oraclebook/commit/af1ab62c97eb088d9e772f6b96399b95d9ea57b3) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Replays recorded book events on a virtual clock through the live feed interface; paper orders still fill instantly at their limits. A reproducible signal path does not validate fills, and book_age_ms=0 bypasses the staleness gate. |

## What this project does

An event-driven prediction-market framework with a recorded JSONL feed, virtual replay clock, risk gates and paper executor.

## Mechanism inspected

ReplayFeed advances a virtual clock to each recorded event and republishes it in sequence. The same feed protocol can drive the app in replay mode; a book-age gate can reject orders whose recorded age exceeds a threshold.

## Limitation that matters

The paper executor immediately fills every submitted order at its limit for full size and cancel always returns success. Book age zero is treated as unknown and passes the gate. The replay therefore reproduces a single feed and strategy decisions, not actual venue fill probability.

## Practical check for a trading system

Separate feed reproducibility from execution fidelity; make unknown book age a failed precondition when a strategy depends on a fresh quote.

## Why this score

3/5 because The replay clock and feed protocol are directly useful, but immediate paper fills and an unknown-age pass materially constrain trading conclusions.

## Source trail

[README and scope](https://github.com/jabrahamtech/oraclebook/blob/af1ab62c97eb088d9e772f6b96399b95d9ea57b3/README.md#L50); [Replay clock](https://github.com/jabrahamtech/oraclebook/blob/af1ab62c97eb088d9e772f6b96399b95d9ea57b3/oraclebook/replay/replay_feed.py#L47); [Immediate paper fills](https://github.com/jabrahamtech/oraclebook/blob/af1ab62c97eb088d9e772f6b96399b95d9ea57b3/oraclebook/core/paper_executor.py#L31); [Unknown-age gate](https://github.com/jabrahamtech/oraclebook/blob/af1ab62c97eb088d9e772f6b96399b95d9ea57b3/oraclebook/risk/gates.py#L19); [License](https://github.com/jabrahamtech/oraclebook/blob/af1ab62c97eb088d9e772f6b96399b95d9ea57b3/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
