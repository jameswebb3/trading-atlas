# PropCheck.jl — Shrinking makes a numeric failure reviewable

**Decision question:** Can a failing generated case be reduced to a small counterexample?

| Field | Review |
| --- | --- |
| Upstream | [Seelengrab/PropCheck.jl](https://github.com/Seelengrab/PropCheck.jl) |
| Primary area | Testing & Verification |
| Source commit | [c00aa873953d10edb33ac9e5846983d9516dbcab](https://github.com/Seelengrab/PropCheck.jl/commit/c00aa873953d10edb33ac9e5846983d9516dbcab) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/Seelengrab/PropCheck.jl/blob/c00aa873953d10edb33ac9e5846983d9516dbcab/LICENSE.md)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | shrinkTowards moves a numeric failure toward a target and stops on duplicate, nonfinite or exhausted floating-point candidates. A shrinker improves diagnosis after a failing case; it does not establish that the property or generator models exchange behavior. |

## What this project does

Julia property-testing library with numeric and structural shrinkers. [README](https://github.com/Seelengrab/PropCheck.jl/blob/c00aa873953d10edb33ac9e5846983d9516dbcab/README.md).

## Mechanism inspected

shrinkTowards moves a numeric failure toward a target and stops on duplicate, nonfinite or exhausted floating-point candidates. [Implementation](https://github.com/Seelengrab/PropCheck.jl/blob/c00aa873953d10edb33ac9e5846983d9516dbcab/src/shrinkers.jl#L268-L303).

## Limitation that matters

A shrinker improves diagnosis after a failing case; it does not establish that the property or generator models exchange behavior. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

When a race or accounting property fails, minimize its event sequence while preserving the failure and original seed.

## Why this score

shrinkTowards moves a numeric failure toward a target and stops on duplicate, nonfinite or exhausted floating-point candidates. A shrinker improves diagnosis after a failing case; it does not establish that the property or generator models exchange behavior.

## Source trail

[README](https://github.com/Seelengrab/PropCheck.jl/blob/c00aa873953d10edb33ac9e5846983d9516dbcab/README.md) · [Implementation](https://github.com/Seelengrab/PropCheck.jl/blob/c00aa873953d10edb33ac9e5846983d9516dbcab/src/shrinkers.jl#L268-L303) · [License](https://github.com/Seelengrab/PropCheck.jl/blob/c00aa873953d10edb33ac9e5846983d9516dbcab/LICENSE.md).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
