# scala-hedgehog — Shrinking numeric failures must guard finite bounds

**Decision question:** Can a property-test failure be reduced without inventing invalid numbers?

| Field | Review |
| --- | --- |
| Upstream | [hedgehogqa/scala-hedgehog](https://github.com/hedgehogqa/scala-hedgehog) |
| Primary area | Testing & Verification |
| Source commit | [03383f0ecdbfed5d82f6dbe33d537c7a274782c3](https://github.com/hedgehogqa/scala-hedgehog/commit/03383f0ecdbfed5d82f6dbe33d537c7a274782c3) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/hedgehogqa/scala-hedgehog/blob/03383f0ecdbfed5d82f6dbe33d537c7a274782c3/LICENSE)) |
| Review depth | 3/3: documentation and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | towardsFloat halves the distance to a target, stopping on duplicates, NaN, infinity and values outside the original interval. The shrinker is generic and overlaps other property-testing references; it does not model event ordering or exchange races. |

## What this project does

Scala property-testing library with generated tests and shrinkers. [README](https://github.com/hedgehogqa/scala-hedgehog/blob/03383f0ecdbfed5d82f6dbe33d537c7a274782c3/README.md).

## Mechanism inspected

towardsFloat halves the distance to a target, stopping on duplicates, NaN, infinity and values outside the original interval. [Implementation](https://github.com/hedgehogqa/scala-hedgehog/blob/03383f0ecdbfed5d82f6dbe33d537c7a274782c3/core/shared/src/main/scala/hedgehog/core/Shrink.scala#L31-L55). [Test source](https://github.com/hedgehogqa/scala-hedgehog/blob/03383f0ecdbfed5d82f6dbe33d537c7a274782c3/test/shared/src/test/scala/hedgehog/ShrinkTest.scala#L46-L55).

## Limitation that matters

The shrinker is generic and overlaps other property-testing references; it does not model event ordering or exchange races. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

If minimizing a failed replay, preserve event-time ordering and order-state invariants while shrinking values and sequence length.

## Why this score

towardsFloat halves the distance to a target, stopping on duplicates, NaN, infinity and values outside the original interval. The shrinker is generic and overlaps other property-testing references; it does not model event ordering or exchange races.

## Source trail

[README](https://github.com/hedgehogqa/scala-hedgehog/blob/03383f0ecdbfed5d82f6dbe33d537c7a274782c3/README.md) · [Implementation](https://github.com/hedgehogqa/scala-hedgehog/blob/03383f0ecdbfed5d82f6dbe33d537c7a274782c3/core/shared/src/main/scala/hedgehog/core/Shrink.scala#L31-L55) · [Test source](https://github.com/hedgehogqa/scala-hedgehog/blob/03383f0ecdbfed5d82f6dbe33d537c7a274782c3/test/shared/src/test/scala/hedgehog/ShrinkTest.scala#L46-L55) · [License](https://github.com/hedgehogqa/scala-hedgehog/blob/03383f0ecdbfed5d82f6dbe33d537c7a274782c3/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
