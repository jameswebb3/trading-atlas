# effect — Retry jitter is a narrow scheduling primitive

**Decision question:** How can concurrent retries avoid synchronizing?

| Field | Review |
| --- | --- |
| Upstream | [Effect-TS/effect](https://github.com/Effect-TS/effect) |
| Primary area | Operations & Observability |
| Source commit | [f7c431734583eeffdabd940ca8af9dc21c216782](https://github.com/Effect-TS/effect/commit/f7c431734583eeffdabd940ca8af9dc21c216782) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/Effect-TS/effect/blob/f7c431734583eeffdabd940ca8af9dc21c216782/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | jittered modifies a schedule delay using a random factor between roughly 0.8 and 1.2. Jitter only spreads retry timing; it does not classify permanent errors or make non-idempotent order requests safe. |

## What this project does

TypeScript effect framework with typed errors, scheduling and structured concurrency. [README](https://github.com/Effect-TS/effect/blob/f7c431734583eeffdabd940ca8af9dc21c216782/README.md).

## Mechanism inspected

jittered modifies a schedule delay using a random factor between roughly 0.8 and 1.2. [Implementation](https://github.com/Effect-TS/effect/blob/f7c431734583eeffdabd940ca8af9dc21c216782/packages/effect/src/Schedule.ts#L1123-L1130).

## Limitation that matters

Jitter only spreads retry timing; it does not classify permanent errors or make non-idempotent order requests safe. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Use jitter only after retryability, deadline and idempotency are defined for the operation.

## Why this score

jittered modifies a schedule delay using a random factor between roughly 0.8 and 1.2. Jitter only spreads retry timing; it does not classify permanent errors or make non-idempotent order requests safe.

## Source trail

[README](https://github.com/Effect-TS/effect/blob/f7c431734583eeffdabd940ca8af9dc21c216782/README.md) · [Implementation](https://github.com/Effect-TS/effect/blob/f7c431734583eeffdabd940ca8af9dc21c216782/packages/effect/src/Schedule.ts#L1123-L1130) · [License](https://github.com/Effect-TS/effect/blob/f7c431734583eeffdabd940ca8af9dc21c216782/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
