# junit-quickcheck: shrink a failing case while preserving reproduction data

**Decision question:** Can a randomized failure become a small reproducible regression fixture?

| Field | Review |
| --- | --- |
| Upstream | [junit-quickcheck](https://github.com/pholser/junit-quickcheck) |
| Primary area | Testing & Verification |
| Source commit | [de9f5d75314d0cf9b703f625ae24a4ac598f56a7](https://github.com/pholser/junit-quickcheck/commit/de9f5d75314d0cf9b703f625ae24a4ac598f56a7) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/pholser/junit-quickcheck/blob/de9f5d75314d0cf9b703f625ae24a4ac598f56a7/LICENSE.txt) |
| Review depth | 3/3: documentation, shrinker, and regression fixture read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Generates property-test inputs and shrinks failing cases into smaller counterexamples. Its documentation preserves both original failure context and reproduction seeds, while the shrinker imposes attempt, depth, and time bounds. |

## Project overview

A Java library brings property-based testing to JUnit. [Project documentation](https://github.com/pholser/junit-quickcheck/blob/de9f5d75314d0cf9b703f625ae24a4ac598f56a7/README.md#L10-L28).

## Mechanism worth inspecting

[Shrinking documentation](https://github.com/pholser/junit-quickcheck/blob/de9f5d75314d0cf9b703f625ae24a4ac598f56a7/src/site/markdown/usage/shrinking.md#L46-L71) exposes original arguments, smaller cases, and seeds. The [shrinker](https://github.com/pholser/junit-quickcheck/blob/de9f5d75314d0cf9b703f625ae24a4ac598f56a7/core/src/main/java/com/pholser/junit/quickcheck/runner/Shrinker.java#L65-L108) retains failing candidates within explicit budgets. A [fixture](https://github.com/pholser/junit-quickcheck/blob/de9f5d75314d0cf9b703f625ae24a4ac598f56a7/core/src/test/java/com/pholser/junit/quickcheck/ShrinkingTest.java#L52-L69) checks a reduced counterexample.

## Important limit

Candidate generation determines which smaller cases are reachable, and [stopping conditions](https://github.com/pholser/junit-quickcheck/blob/de9f5d75314d0cf9b703f625ae24a4ac598f56a7/core/src/main/java/com/pholser/junit/quickcheck/runner/Shrinker.java#L104-L108) can stop before the smallest possible failure. [Seed documentation](https://github.com/pholser/junit-quickcheck/blob/de9f5d75314d0cf9b703f625ae24a4ac598f56a7/src/site/markdown/usage/seed.md#L17-L30) supports replay, but generators and implementation versions must also be retained.

## Questions to take into your own design

- Does a failure artifact store the original case, reduced case, seed, and generator version?
- Do reductions preserve the event-ordering constraints relevant to the failure?

## Why this score for a trading system

3/5: a concrete reusable failure-reduction mechanism with readable test evidence; generic Java tooling is not itself a trading validation suite.

**Scope of this review:** README, shrinking and seed documentation, shrinker source and shrinking regression fixture read.
