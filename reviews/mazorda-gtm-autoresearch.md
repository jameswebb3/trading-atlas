# gtm-autoresearch — Reject a holdout whose outcomes overlap model search

**Decision question:** Did the search period finish before the later evaluation snapshot?

| Field | Review |
| --- | --- |
| Upstream | [mazorda/gtm-autoresearch](https://github.com/mazorda/gtm-autoresearch) |
| Primary area | Research & Reproducibility |
| Source commit | [a5e4b5db69ef25f6967532b528e8f5550f2e859c](https://github.com/mazorda/gtm-autoresearch/commit/a5e4b5db69ef25f6967532b528e8f5550f2e859c) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/mazorda/gtm-autoresearch/blob/a5e4b5db69ef25f6967532b528e8f5550f2e859c/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The validator requires unique IDs, feature snapshots before their outcomes, mature outcome windows at the review cutoff, and the final search outcome before the first holdout feature snapshot. It checks declared timestamps, not whether the underlying fields were actually available then; a false availability clock still leaks. Its customer scoring objective is unrelated to market returns. |

## What this project does

Scoring-model refresh workflow that searches historical customer outcomes, freezes a candidate, then reviews it on later outcomes. [README](https://github.com/mazorda/gtm-autoresearch/blob/a5e4b5db69ef25f6967532b528e8f5550f2e859c/README.md).

## Mechanism inspected

The validator requires unique IDs, feature snapshots before their outcomes, mature outcome windows at the review cutoff, and the final search outcome before the first holdout feature snapshot. [Implementation](https://github.com/mazorda/gtm-autoresearch/blob/a5e4b5db69ef25f6967532b528e8f5550f2e859c/analysis/refresh.py#L40-L65).

## Limitation that matters

It checks declared timestamps, not whether the underlying fields were actually available then; a false availability clock still leaks. Its customer scoring objective is unrelated to market returns. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

For each proposal-versus-incumbent research split, assert feature availability, outcome maturity, and a strict search/holdout boundary before any model comparison.

## Why this score

The validator requires unique IDs, feature snapshots before their outcomes, mature outcome windows at the review cutoff, and the final search outcome before the first holdout feature snapshot. It checks declared timestamps, not whether the underlying fields were actually available then; a false availability clock still leaks. Its customer scoring objective is unrelated to market returns.

## Source trail

[README](https://github.com/mazorda/gtm-autoresearch/blob/a5e4b5db69ef25f6967532b528e8f5550f2e859c/README.md) · [Implementation](https://github.com/mazorda/gtm-autoresearch/blob/a5e4b5db69ef25f6967532b528e8f5550f2e859c/analysis/refresh.py#L40-L65) · [License](https://github.com/mazorda/gtm-autoresearch/blob/a5e4b5db69ef25f6967532b528e8f5550f2e859c/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
