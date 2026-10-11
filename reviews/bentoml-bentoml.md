# BentoML - Will a monitor stop on unequal column lengths?

**Decision question:** Will a monitor stop on unequal column lengths?

| Field | Review |
| --- | --- |
| Upstream | [bentoml/BentoML](https://github.com/bentoml/BentoML) |
| Primary area | Research & Reproducibility |
| Source commit | [517b343b81aeb0b01bbd908e58e53ad9c12ef7eb](https://github.com/bentoml/BentoML/commit/517b343b81aeb0b01bbd908e58e53ad9c12ef7eb) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The monitor collects feature, prediction and target columns for export. The unequal-length branch constructs ValueError inside assert rather than raising it; the inspected path can continue to export malformed column groups. |

## What this project does

A model-serving framework with request monitoring hooks.

## Mechanism inspected

The monitor collects feature, prediction and target columns for export.

## Limitation that matters

The unequal-length branch constructs ValueError inside assert rather than raising it; the inspected path can continue to export malformed column groups.

## Practical check for a trading system

Use explicit invariant checks before writing evidence and test them with assertions disabled.

## Why this score

2/5. A concrete monitoring failure mode in a large serving framework.

## Source trail

[README](https://github.com/bentoml/BentoML/blob/517b343b81aeb0b01bbd908e58e53ad9c12ef7eb/README.md#L1); [src/bentoml/_internal/monitoring/base.py](https://github.com/bentoml/BentoML/blob/517b343b81aeb0b01bbd908e58e53ad9c12ef7eb/src/bentoml/_internal/monitoring/base.py#L74); [Root license](https://github.com/bentoml/BentoML/blob/517b343b81aeb0b01bbd908e58e53ad9c12ef7eb/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
