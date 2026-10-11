# Encord Active - Can image data and its annotations be tracked as different versions?

**Decision question:** Can image data and its annotations be tracked as different versions?

| Field | Review |
| --- | --- |
| Upstream | [encord-team/encord-active](https://github.com/encord-team/encord-active) |
| Primary area | Data Quality & Lineage |
| Source commit | [5e724ce56f11efefbf199eb792cacd9e6ba7ff9b](https://github.com/encord-team/encord-active/commit/5e724ce56f11efefbf199eb792cacd9e6ba7ff9b) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The COCO export metadata carries distinct label_hash and data_hash fields alongside image identity. These fields are evidence slots, not proof in this file that hashing or downstream validation actually occurs. |

## What this project does

A dataset quality tool for annotated visual data.

## Mechanism inspected

The COCO export metadata carries distinct label_hash and data_hash fields alongside image identity.

## Limitation that matters

These fields are evidence slots, not proof in this file that hashing or downstream validation actually occurs.

## Practical check for a trading system

Track source-payload and label or derived-data hashes separately in each dataset manifest.

## Why this score

2/5. It suggests a useful provenance schema but the inspected type alone is not an end-to-end integrity guarantee.

## Source trail

[README](https://github.com/encord-team/encord-active/blob/5e724ce56f11efefbf199eb792cacd9e6ba7ff9b/README.md#L1); [src/encord_active/lib/coco/datastructure.py](https://github.com/encord-team/encord-active/blob/5e724ce56f11efefbf199eb792cacd9e6ba7ff9b/src/encord_active/lib/coco/datastructure.py#L91); [src/encord_active/lib/coco/datastructure.py](https://github.com/encord-team/encord-active/blob/5e724ce56f11efefbf199eb792cacd9e6ba7ff9b/src/encord_active/lib/coco/datastructure.py#L97); [src/encord_active/lib/coco/datastructure.py](https://github.com/encord-team/encord-active/blob/5e724ce56f11efefbf199eb792cacd9e6ba7ff9b/src/encord_active/lib/coco/datastructure.py#L98).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
