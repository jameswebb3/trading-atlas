# Crypto Algo Trading Framework - Which market events may be conflated under load?

**Decision question:** Which market events may be conflated under load?

| Field | Review |
| --- | --- |
| Upstream | [sakshamverma2030/Algorithmic-Trading-Framework-in-Crypto-Python](https://github.com/sakshamverma2030/Algorithmic-Trading-Framework-in-Crypto-Python) |
| Primary area | Market Data & Ingestion |
| Source commit | [2015439422558c57c98e421ec0df48a7c1dd7517](https://github.com/sakshamverma2030/Algorithmic-Trading-Framework-in-Crypto-Python/commit/2015439422558c57c98e421ec0df48a7c1dd7517) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The event bus uses a bounded FIFO for closed bars and a single-slot latest-value mailbox for order-book and tick updates, counting overwritten values. Conflation is acceptable for a latest snapshot consumer but destroys the delta history needed for exact book reconstruction or trade-flow features. |

## What this project does

An educational crypto strategy, backtest and paper/live trading framework.

## Mechanism inspected

The event bus uses a bounded FIFO for closed bars and a single-slot latest-value mailbox for order-book and tick updates, counting overwritten values.

## Limitation that matters

Conflation is acceptable for a latest snapshot consumer but destroys the delta history needed for exact book reconstruction or trade-flow features.

## Practical check for a trading system

Declare per-channel loss policy and forbid latest-value mailboxes for causal delta streams.

## Why this score

3/5. The separate queue policies make an important data-loss tradeoff visible.

## Source trail

[README](https://github.com/sakshamverma2030/Algorithmic-Trading-Framework-in-Crypto-Python/blob/2015439422558c57c98e421ec0df48a7c1dd7517/README.md#L1); [CAPSTONE.md](https://github.com/sakshamverma2030/Algorithmic-Trading-Framework-in-Crypto-Python/blob/2015439422558c57c98e421ec0df48a7c1dd7517/CAPSTONE.md#L1); [live_trader.py](https://github.com/sakshamverma2030/Algorithmic-Trading-Framework-in-Crypto-Python/blob/2015439422558c57c98e421ec0df48a7c1dd7517/live_trader.py#L169).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
