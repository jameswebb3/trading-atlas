# PolyKalshi Client - What should a reconstructed book do after a Kalshi sequence gap?

**Decision question:** What should a reconstructed book do after a Kalshi sequence gap?

| Field | Review |
| --- | --- |
| Upstream | [RohitDayanand/PolyKalshi_Client](https://github.com/RohitDayanand/PolyKalshi_Client) |
| Primary area | Market Data & Ingestion |
| Source commit | [e585025e6de9de45c13d9f20a5ea253e9b91ff39](https://github.com/RohitDayanand/PolyKalshi_Client/commit/e585025e6de9de45c13d9f20a5ea253e9b91ff39) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Detects missing Kalshi book sequence numbers before applying deltas. The last cached book is not visibly invalidated or resynchronized after a gap. |

## What this project does

A Kalshi and Polymarket real-time analytics platform with separate market message processors.

## Mechanism inspected

The Kalshi processor rejects older snapshots and requires the next delta sequence to be exactly previous plus one. The Polymarket processor applies full book snapshots separately from price-level changes.

## Limitation that matters

On a Kalshi gap it logs an error and returns without applying that delta, but the shown path does not invalidate the last book or request a resnapshot. Downstream readers may still see a stale book as current. No root license text was verified.

## Practical check for a trading system

Treat a sequence gap as a capability loss: invalidate dependent prices until a new snapshot is accepted.

## Why this score

2/5. Sequence checking is the right primitive, but the recovery state remains incomplete.

## Source trail

[README](https://github.com/RohitDayanand/PolyKalshi_Client/blob/e585025e6de9de45c13d9f20a5ea253e9b91ff39/README.md#L19); [backend/master_manager/kalshi_client/message_processor.py](https://github.com/RohitDayanand/PolyKalshi_Client/blob/e585025e6de9de45c13d9f20a5ea253e9b91ff39/backend/master_manager/kalshi_client/message_processor.py#L246); [backend/master_manager/kalshi_client/message_processor.py](https://github.com/RohitDayanand/PolyKalshi_Client/blob/e585025e6de9de45c13d9f20a5ea253e9b91ff39/backend/master_manager/kalshi_client/message_processor.py#L291); [backend/master_manager/kalshi_client/message_processor.py](https://github.com/RohitDayanand/PolyKalshi_Client/blob/e585025e6de9de45c13d9f20a5ea253e9b91ff39/backend/master_manager/kalshi_client/message_processor.py#L316); [backend/master_manager/polymarket_client/polymarket_message_processor.py](https://github.com/RohitDayanand/PolyKalshi_Client/blob/e585025e6de9de45c13d9f20a5ea253e9b91ff39/backend/master_manager/polymarket_client/polymarket_message_processor.py#L117).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
