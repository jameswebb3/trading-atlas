# weightslab — Deduplication changes the experimental population

**Decision question:** What happens to sample count when the same ID appears across splits?

| Field | Review |
| --- | --- |
| Upstream | [GrayboxTech/weightslab](https://github.com/GrayboxTech/weightslab) |
| Primary area | Testing & Verification |
| Source commit | [345c6225825ae83f2301a66bf6fcaac31f177b36](https://github.com/GrayboxTech/weightslab/commit/345c6225825ae83f2301a66bf6fcaac31f177b36) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/GrayboxTech/weightslab/blob/345c6225825ae83f2301a66bf6fcaac31f177b36/LICENSE)) |
| Review depth | 3/3: documentation and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A dataset wrapper keeps first occurrences within a loader and can remove IDs already present in another loader, logging the removals. Automatic removal changes N and the sampled population; a warning alone may not satisfy a preregistered denominator. |

## What this project does

Experiment and dataset tracking system with per-sample IDs and leakage checks. [README](https://github.com/GrayboxTech/weightslab/blob/345c6225825ae83f2301a66bf6fcaac31f177b36/README.md).

## Mechanism inspected

A dataset wrapper keeps first occurrences within a loader and can remove IDs already present in another loader, logging the removals. [Implementation](https://github.com/GrayboxTech/weightslab/blob/345c6225825ae83f2301a66bf6fcaac31f177b36/weightslab/data/data_samples_with_ops.py#L280-L340). [Test source](https://github.com/GrayboxTech/weightslab/blob/345c6225825ae83f2301a66bf6fcaac31f177b36/tests/data/test_data_samples_with_ops.py#L647-L669).

## Limitation that matters

Automatic removal changes N and the sampled population; a warning alone may not satisfy a preregistered denominator. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Report duplicate IDs, affected splits and before/after N; require an explicit decision to exclude or retain before scoring.

## Why this score

A dataset wrapper keeps first occurrences within a loader and can remove IDs already present in another loader, logging the removals. Automatic removal changes N and the sampled population; a warning alone may not satisfy a preregistered denominator.

## Source trail

[README](https://github.com/GrayboxTech/weightslab/blob/345c6225825ae83f2301a66bf6fcaac31f177b36/README.md) · [Implementation](https://github.com/GrayboxTech/weightslab/blob/345c6225825ae83f2301a66bf6fcaac31f177b36/weightslab/data/data_samples_with_ops.py#L280-L340) · [Test source](https://github.com/GrayboxTech/weightslab/blob/345c6225825ae83f2301a66bf6fcaac31f177b36/tests/data/test_data_samples_with_ops.py#L647-L669) · [License](https://github.com/GrayboxTech/weightslab/blob/345c6225825ae83f2301a66bf6fcaac31f177b36/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
