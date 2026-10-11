# Pointblank: count failures before assigning severity

**Decision question:** When does a data-validation failure become blocking?

| Field | Review |
| --- | --- |
| Upstream | [Pointblank](https://github.com/posit-dev/pointblank) |
| Primary area | Data Quality & Lineage |
| Source commit | [8f19f424a990f62e92a6ac98438dcfd2816ec77f](https://github.com/posit-dev/pointblank/commit/8f19f424a990f62e92a6ac98438dcfd2816ec77f) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/posit-dev/pointblank/blob/8f19f424a990f62e92a6ac98438dcfd2816ec77f/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Defines warning, error, and critical thresholds as failing-row counts or fractions, with per-step overrides and actions. This makes the acceptance policy inspectable, but a threshold cannot decide whether one missing fill or timestamp is harmless. |

## Mechanism worth inspecting

The [validation workflow](https://github.com/posit-dev/pointblank/blob/8f19f424a990f62e92a6ac98438dcfd2816ec77f/README.md#L162-L180) chains checks into a report. The [threshold contract](https://github.com/posit-dev/pointblank/blob/8f19f424a990f62e92a6ac98438dcfd2816ec77f/pointblank/thresholds.py#L9-L39) defines warning, error, and critical levels as absolute counts or fractions, while the [normalization code](https://github.com/posit-dev/pointblank/blob/8f19f424a990f62e92a6ac98438dcfd2816ec77f/pointblank/thresholds.py#L95-L122) distinguishes fractional from count limits. Its [action example](https://github.com/posit-dev/pointblank/blob/8f19f424a990f62e92a6ac98438dcfd2816ec77f/pointblank/thresholds.py#L539-L577) runs an alert after validation. This is a concrete separation between measurement and response policy.

## Important limit

The framework cannot infer that a single duplicate fill, reversed timestamp, or missing symbol is a hard stop. Those require explicit checks and thresholds. Its generated reports do not by themselves prove that a feed was complete at the time of a decision.

## Questions to take into your own design

- Which failures are zero-tolerance regardless of dataset size?
- Can a reviewer see both failed rows and the policy that permitted or blocked them?

## Why this score for a trading system

Explicit counts, fractions, and actions help make data gates reviewable; domain-specific invariants still need zero-tolerance rules.

**Scope of this review:** We read the pinned README and threshold/action implementation. We did not run a validation plan.
