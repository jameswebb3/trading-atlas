# AIAlpha — A one-row split gap does not purge a multi-row target

**Decision question:** Can labels overlap the test period after a chronological split?

| Field | Review |
| --- | --- |
| Upstream | [VivekPa/AIAlpha](https://github.com/VivekPa/AIAlpha) |
| Primary area | Testing & Verification |
| Source commit | [fd5a531471317db7819bbb90988fdd299cd6bd54](https://github.com/VivekPa/AIAlpha/commit/fd5a531471317db7819bbb90988fdd299cd6bd54) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/VivekPa/AIAlpha/blob/fd5a531471317db7819bbb90988fdd299cd6bd54/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The target uses a future close at t+window, but train and test arrays are cut around a fixed one-row gap regardless of that window length. For windows longer than one row, training labels near the boundary use prices from the test period. The label is also the log of current over future close, so its sign needs explicit interpretation. |

## What this project does

Equity-return modeling example with rolling features and a train/test builder. [README](https://github.com/VivekPa/AIAlpha/blob/fd5a531471317db7819bbb90988fdd299cd6bd54/README.md).

## Mechanism inspected

The target uses a future close at t+window, but train and test arrays are cut around a fixed one-row gap regardless of that window length. [Implementation](https://github.com/VivekPa/AIAlpha/blob/fd5a531471317db7819bbb90988fdd299cd6bd54/data_processor/data_processing.py#L67-L90).

## Limitation that matters

For windows longer than one row, training labels near the boundary use prices from the test period. The label is also the log of current over future close, so its sign needs explicit interpretation. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Purge at least the full target horizon across split boundaries and assert train-label endpoints precede the first test observation.

## Why this score

The target uses a future close at t+window, but train and test arrays are cut around a fixed one-row gap regardless of that window length. For windows longer than one row, training labels near the boundary use prices from the test period. The label is also the log of current over future close, so its sign needs explicit interpretation.

## Source trail

[README](https://github.com/VivekPa/AIAlpha/blob/fd5a531471317db7819bbb90988fdd299cd6bd54/README.md) · [Implementation](https://github.com/VivekPa/AIAlpha/blob/fd5a531471317db7819bbb90988fdd299cd6bd54/data_processor/data_processing.py#L67-L90) · [License](https://github.com/VivekPa/AIAlpha/blob/fd5a531471317db7819bbb90988fdd299cd6bd54/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
