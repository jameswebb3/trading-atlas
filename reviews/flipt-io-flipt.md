# flipt — Stable rollout hashing can gate a controlled release

**Decision question:** Can a rollout keep the same entity in the same cohort?

| Field | Review |
| --- | --- |
| Upstream | [flipt-io/flipt](https://github.com/flipt-io/flipt) |
| Primary area | Operations & Observability |
| Source commit | [f97a84d4ad9f1ed305212eb15120b059b1f00d7c](https://github.com/flipt-io/flipt/commit/f97a84d4ad9f1ed305212eb15120b059b1f00d7c) |
| Reviewed | 2026-10-09 |
| Declared license | FCL-1.0-MIT ([source](https://github.com/flipt-io/flipt/blob/f97a84d4ad9f1ed305212eb15120b059b1f00d7c/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Boolean evaluation rejects out-of-order rollout ranks and hashes entity ID with flag key to apply a stable threshold cohort. Stable assignment is not experiment randomization or a safe trading canary by itself; the root license is Fair Core with MIT future terms. |

## What this project does

Feature-flag service with ranked rules, segmentation and percentage rollouts. [README](https://github.com/flipt-io/flipt/blob/f97a84d4ad9f1ed305212eb15120b059b1f00d7c/README.md).

## Mechanism inspected

Boolean evaluation rejects out-of-order rollout ranks and hashes entity ID with flag key to apply a stable threshold cohort. [Implementation](https://github.com/flipt-io/flipt/blob/f97a84d4ad9f1ed305212eb15120b059b1f00d7c/internal/server/evaluation/evaluation.go#L409-L434).

## Limitation that matters

Stable assignment is not experiment randomization or a safe trading canary by itself; the root license is Fair Core with MIT future terms. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

If a research-only canary is needed, pin cohort assignment and measure exposure while keeping money-moving rollout in the operational channel.

## Why this score

Boolean evaluation rejects out-of-order rollout ranks and hashes entity ID with flag key to apply a stable threshold cohort. Stable assignment is not experiment randomization or a safe trading canary by itself; the root license is Fair Core with MIT future terms.

## Source trail

[README](https://github.com/flipt-io/flipt/blob/f97a84d4ad9f1ed305212eb15120b059b1f00d7c/README.md) · [Implementation](https://github.com/flipt-io/flipt/blob/f97a84d4ad9f1ed305212eb15120b059b1f00d7c/internal/server/evaluation/evaluation.go#L409-L434) · [License](https://github.com/flipt-io/flipt/blob/f97a84d4ad9f1ed305212eb15120b059b1f00d7c/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
