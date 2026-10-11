# rapidfireai — Scheduler generations should be visible in run records

**Decision question:** Can a resumed experiment be confused with an earlier scheduling attempt?

| Field | Review |
| --- | --- |
| Upstream | [rapidfireai](https://github.com/RapidFireAI/rapidfireai) |
| Primary area | Research & Reproducibility |
| Source commit | [7b4e103b1cec3cdda49b102fac42fad935c5b629](https://github.com/RapidFireAI/rapidfireai/commit/7b4e103b1cec3cdda49b102fac42fad935c5b629) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/RapidFireAI/rapidfireai/blob/7b4e103b1cec3cdda49b102fac42fad935c5b629/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The scheduler tracks run IDs, assigned workers, visited shards and scheduling generation as separate state. Those fields describe scheduling, not independent statistical trials; counting a reschedule as a new sample would inflate N. |

## What this project does

An experiment system for parallel model evaluations. [README](https://github.com/RapidFireAI/rapidfireai/blob/7b4e103b1cec3cdda49b102fac42fad935c5b629/README.md).

## Mechanism inspected

The scheduler tracks run IDs, assigned workers, visited shards and scheduling generation as separate state. [Implementation](https://github.com/RapidFireAI/rapidfireai/blob/7b4e103b1cec3cdda49b102fac42fad935c5b629/rapidfireai/fit/backend/scheduler.py#L38-L75).

## Limitation that matters

Those fields describe scheduling, not independent statistical trials; counting a reschedule as a new sample would inflate N. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Keep execution_attempt distinct from trial_id and statistical sample count in receipts.

## Why this score

Transferable engineering pattern: The scheduler tracks run IDs, assigned workers, visited shards and scheduling generation as separate state. Those fields describe scheduling, not independent statistical trials; counting a reschedule as a new sample would inflate N.

## Source trail

[README](https://github.com/RapidFireAI/rapidfireai/blob/7b4e103b1cec3cdda49b102fac42fad935c5b629/README.md) · [Documentation](https://github.com/RapidFireAI/rapidfireai/blob/7b4e103b1cec3cdda49b102fac42fad935c5b629/docs/BUILD.md) · [Implementation](https://github.com/RapidFireAI/rapidfireai/blob/7b4e103b1cec3cdda49b102fac42fad935c5b629/rapidfireai/fit/backend/scheduler.py#L38-L75).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
