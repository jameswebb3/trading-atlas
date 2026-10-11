# bulbea — Split overlapping windows with a purge boundary

**Decision question:** Does a chronological split avoid overlap after rolling windows are built?

| Field | Review |
| --- | --- |
| Upstream | [achillesrasquinha/bulbea](https://github.com/achillesrasquinha/bulbea) |
| Primary area | Testing & Verification |
| Source commit | [4caba8f042f1d87ec0b41ec8e14d3a458a7409a4](https://github.com/achillesrasquinha/bulbea/commit/4caba8f042f1d87ec0b41ec8e14d3a458a7409a4) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/achillesrasquinha/bulbea/blob/4caba8f042f1d87ec0b41ec8e14d3a458a7409a4/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | `split` creates overlapping windows across the full price series and only then divides the window array into train and test slices. Neighboring train/test windows share observations; there is no purge or embargo in the inspected function, and the source is equity-oriented. |

## What this project does

Stock-market prediction library using sliding windows and neural models. [README](https://github.com/achillesrasquinha/bulbea/blob/4caba8f042f1d87ec0b41ec8e14d3a458a7409a4/README.md).

## Mechanism inspected

`split` creates overlapping windows across the full price series and only then divides the window array into train and test slices. [Implementation](https://github.com/achillesrasquinha/bulbea/blob/4caba8f042f1d87ec0b41ec8e14d3a458a7409a4/bulbea/learn/evaluation/split.py#L39-L60).

## Limitation that matters

Neighboring train/test windows share observations; there is no purge or embargo in the inspected function, and the source is equity-oriented. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Compare the last training window and first test window by raw timestamps and purge overlap before scoring any model.

## Why this score

`split` creates overlapping windows across the full price series and only then divides the window array into train and test slices. Neighboring train/test windows share observations; there is no purge or embargo in the inspected function, and the source is equity-oriented.

## Source trail

[README](https://github.com/achillesrasquinha/bulbea/blob/4caba8f042f1d87ec0b41ec8e14d3a458a7409a4/README.md) · [Implementation](https://github.com/achillesrasquinha/bulbea/blob/4caba8f042f1d87ec0b41ec8e14d3a458a7409a4/bulbea/learn/evaluation/split.py#L39-L60) · [License](https://github.com/achillesrasquinha/bulbea/blob/4caba8f042f1d87ec0b41ec8e14d3a458a7409a4/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
