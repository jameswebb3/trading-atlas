# quant-mind — Persist batch state before a failed run disappears

**Decision question:** Can a cancelled experiment distinguish completed batches from the failed one?

| Field | Review |
| --- | --- |
| Upstream | [LLMQuant/quant-mind](https://github.com/LLMQuant/quant-mind) |
| Primary area | Research & Reproducibility |
| Source commit | [10e9dbd0c7254edc5a091b852122ebe72e06092a](https://github.com/LLMQuant/quant-mind/commit/10e9dbd0c7254edc5a091b852122ebe72e06092a) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/LLMQuant/quant-mind/blob/10e9dbd0c7254edc5a091b852122ebe72e06092a/LICENSE)) |
| Review depth | 3/3: README and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its run record writes an atomic JSON snapshot with state, stage, config and progress, and the batch tests specify that failure or cancellation at batch two retains completion of batch one. The lifecycle event append is best effort and the snapshot alone does not prove downstream load idempotence or power-loss durability; the ETL is generic rather than venue-specific. |

## What this project does

Financial-knowledge toolkit with a batch ETL path that records run state, stage and progress locally. [README](https://github.com/LLMQuant/quant-mind/blob/10e9dbd0c7254edc5a091b852122ebe72e06092a/README.md).

## Mechanism inspected

Its run record writes an atomic JSON snapshot with state, stage, config and progress, and the batch tests specify that failure or cancellation at batch two retains completion of batch one. [Implementation](https://github.com/LLMQuant/quant-mind/blob/10e9dbd0c7254edc5a091b852122ebe72e06092a/quantmind/etl/_record.py#L510-L550). [Test source](https://github.com/LLMQuant/quant-mind/blob/10e9dbd0c7254edc5a091b852122ebe72e06092a/tests/etl/test_batch.py#L440-L527).

## Limitation that matters

The lifecycle event append is best effort and the snapshot alone does not prove downstream load idempotence or power-loss durability; the ETL is generic rather than venue-specific. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Expose completed batch index and terminal state beside each research or collector artifact, then reconcile those records with actual persisted outputs before resume.

## Why this score

Its run record writes an atomic JSON snapshot with state, stage, config and progress, and the batch tests specify that failure or cancellation at batch two retains completion of batch one. The lifecycle event append is best effort and the snapshot alone does not prove downstream load idempotence or power-loss durability; the ETL is generic rather than venue-specific.

## Source trail

[README](https://github.com/LLMQuant/quant-mind/blob/10e9dbd0c7254edc5a091b852122ebe72e06092a/README.md) · [Implementation](https://github.com/LLMQuant/quant-mind/blob/10e9dbd0c7254edc5a091b852122ebe72e06092a/quantmind/etl/_record.py#L510-L550) · [Test source](https://github.com/LLMQuant/quant-mind/blob/10e9dbd0c7254edc5a091b852122ebe72e06092a/tests/etl/test_batch.py#L440-L527) · [License](https://github.com/LLMQuant/quant-mind/blob/10e9dbd0c7254edc5a091b852122ebe72e06092a/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
