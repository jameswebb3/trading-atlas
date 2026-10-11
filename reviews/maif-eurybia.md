# eurybia — A drift classifier is not a strategy kill switch

**Decision question:** Can current and baseline feature populations be distinguished?

| Field | Review |
| --- | --- |
| Upstream | [MAIF/eurybia](https://github.com/MAIF/eurybia) |
| Primary area | Signals & Models |
| Source commit | [51ee4af30c1ebe6beb4ac5f68b1f5abb46ced91c](https://github.com/MAIF/eurybia/commit/51ee4af30c1ebe6beb4ac5f68b1f5abb46ced91c) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/MAIF/eurybia/blob/51ee4af30c1ebe6beb4ac5f68b1f5abb46ced91c/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | It combines baseline and current rows, random-splits them, trains CatBoost to classify period membership and reports held-out AUC plus feature importances. A random split does not preserve temporal dependence; distribution shift alone says neither why a trading signal changed nor whether returns deteriorated. |

## What this project does

Python library for data/model drift reports using a dataset discriminator. [README](https://github.com/MAIF/eurybia/blob/51ee4af30c1ebe6beb4ac5f68b1f5abb46ced91c/README.md).

## Mechanism inspected

It combines baseline and current rows, random-splits them, trains CatBoost to classify period membership and reports held-out AUC plus feature importances. [Implementation](https://github.com/MAIF/eurybia/blob/51ee4af30c1ebe6beb4ac5f68b1f5abb46ced91c/eurybia/core/smartdrift.py#L267-L355).

## Limitation that matters

A random split does not preserve temporal dependence; distribution shift alone says neither why a trading signal changed nor whether returns deteriorated. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Use drift as diagnostic evidence with time-blocked calibration and separate outcome tests, never as an automatic weight change.

## Why this score

It combines baseline and current rows, random-splits them, trains CatBoost to classify period membership and reports held-out AUC plus feature importances. A random split does not preserve temporal dependence; distribution shift alone says neither why a trading signal changed nor whether returns deteriorated.

## Source trail

[README](https://github.com/MAIF/eurybia/blob/51ee4af30c1ebe6beb4ac5f68b1f5abb46ced91c/README.md) · [Implementation](https://github.com/MAIF/eurybia/blob/51ee4af30c1ebe6beb4ac5f68b1f5abb46ced91c/eurybia/core/smartdrift.py#L267-L355) · [License](https://github.com/MAIF/eurybia/blob/51ee4af30c1ebe6beb4ac5f68b1f5abb46ced91c/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
