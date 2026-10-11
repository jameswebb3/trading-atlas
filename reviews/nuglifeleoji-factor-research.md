# Factor-Research — A rolling operator does not validate a factor

**Decision question:** What does the published factor code establish beyond window arithmetic?

| Field | Review |
| --- | --- |
| Upstream | [nuglifeleoji/Factor-Research](https://github.com/nuglifeleoji/Factor-Research) |
| Primary area | Signals & Models |
| Source commit | [5b6acf723c522b8bb0a200c26f311f4916f2acf5](https://github.com/nuglifeleoji/Factor-Research/commit/5b6acf723c522b8bb0a200c26f311f4916f2acf5) |
| Reviewed | 2026-10-09 |
| Declared license | No root license file found |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | The Python operator module uses `sliding_window_view` and NaN-aware reductions to produce trailing maximum, minimum, mean and median features. The inspected operator proves only arithmetic over supplied arrays; it carries no publication-time contract, causal split or independent validation of the README's performance claims. |

## What this project does

Stock-factor research repository with notebooks, saved data and claimed model metrics. [README](https://github.com/nuglifeleoji/Factor-Research/blob/5b6acf723c522b8bb0a200c26f311f4916f2acf5/README.md).

## Mechanism inspected

The Python operator module uses `sliding_window_view` and NaN-aware reductions to produce trailing maximum, minimum, mean and median features. [Implementation](https://github.com/nuglifeleoji/Factor-Research/blob/5b6acf723c522b8bb0a200c26f311f4916f2acf5/data/raw/datamin4/operator.py#L5-L31).

## Limitation that matters

The inspected operator proves only arithmetic over supplied arrays; it carries no publication-time contract, causal split or independent validation of the README's performance claims. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Demand source-vintage and holdout evidence before treating a factor library as an alpha source.

## Why this score

The Python operator module uses `sliding_window_view` and NaN-aware reductions to produce trailing maximum, minimum, mean and median features. The inspected operator proves only arithmetic over supplied arrays; it carries no publication-time contract, causal split or independent validation of the README's performance claims.

## Source trail

[README](https://github.com/nuglifeleoji/Factor-Research/blob/5b6acf723c522b8bb0a200c26f311f4916f2acf5/README.md) · [Implementation](https://github.com/nuglifeleoji/Factor-Research/blob/5b6acf723c522b8bb0a200c26f311f4916f2acf5/data/raw/datamin4/operator.py#L5-L31).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
