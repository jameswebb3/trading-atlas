# Supposition.jl — Shrink the choices that built the input

**Decision question:** Can a complex failing input be reduced reproducibly?

| Field | Review |
| --- | --- |
| Upstream | [Supposition.jl](https://github.com/Seelengrab/Supposition.jl) |
| Primary area | Testing & Verification |
| Source commit | [e089f3265ef3adee9ed70e29ae34e86973867fdc](https://github.com/Seelengrab/Supposition.jl/commit/e089f3265ef3adee9ed70e29ae34e86973867fdc) |
| Reviewed | 2026-09-27 |
| Declared license | [EUPL-1.2](https://github.com/Seelengrab/Supposition.jl/blob/e089f3265ef3adee9ed70e29ae34e86973867fdc/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The shrinker works over recorded generation choices, trying block removal, zeroing, element reduction, swaps and redistribution. The resulting reduction depends on the generator and acceptance predicate, not just visible input size. |

## Project overview

Julia property-based testing inspired by Hypothesis, with generated-choice shrinking. [Documentation](https://github.com/Seelengrab/Supposition.jl/blob/e089f3265ef3adee9ed70e29ae34e86973867fdc/README.md).

## Mechanism worth inspecting

The shrinker works over recorded generation choices, trying block removal, zeroing, element reduction, swaps and redistribution. Candidates are replayed through consider before being retained. [Source](https://github.com/Seelengrab/Supposition.jl/blob/e089f3265ef3adee9ed70e29ae34e86973867fdc/src/shrink.jl#L1-L88).

## Important limit

The resulting reduction depends on the generator and acceptance predicate, not just visible input size. The inspected shrink file delegates failure acceptance to another part of the framework. [Evidence 1](https://github.com/Seelengrab/Supposition.jl/blob/e089f3265ef3adee9ed70e29ae34e86973867fdc/src/shrink.jl#L1-L88).

## Questions to take into your own design

- Is the generation-choice sequence retained with the counterexample?
- Does acceptance preserve the same failure and valid preconditions?

## Why this score for a trading system

A useful reproducible-input reduction technique; Julia adoption and whole-framework failure semantics were not justified by this review.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
