# PropCheck for Ruby — Shrink budgets belong in the failure report

**Decision question:** Was the reported counterexample fully reduced?

| Field | Review |
| --- | --- |
| Upstream | [PropCheck for Ruby](https://github.com/Qqwy/ruby-prop_check) |
| Primary area | Testing & Verification |
| Source commit | [155a3278cfae619edba244eaf0986e0771cb64f2](https://github.com/Qqwy/ruby-prop_check/commit/155a3278cfae619edba244eaf0986e0771cb64f2) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/Qqwy/ruby-prop_check/blob/155a3278cfae619edba244eaf0986e0771cb64f2/LICENSE.txt) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The shrinker explores failing child values while tracking shrink steps and retaining the latest exception. Budget exhaustion is not a guarantee of a globally minimal example. |

## Project overview

Ruby property-testing library with generators, counterexample shrinking and lifecycle hooks. [Documentation](https://github.com/Qqwy/ruby-prop_check/blob/155a3278cfae619edba244eaf0986e0771cb64f2/README.md).

## Mechanism worth inspecting

The shrinker explores failing child values while tracking shrink steps and retaining the latest exception. It reports when the configured maximum steps were exceeded. [Source](https://github.com/Qqwy/ruby-prop_check/blob/155a3278cfae619edba244eaf0986e0771cb64f2/lib/prop_check/property/shrinker.rb#L20-L79).

## Important limit

Budget exhaustion is not a guarantee of a globally minimal example. Any exception is treated as a failing candidate, so preserving a particular defect requires a stronger property contract. [Evidence 1](https://github.com/Qqwy/ruby-prop_check/blob/155a3278cfae619edba244eaf0986e0771cb64f2/lib/prop_check/property/shrinker.rb#L20-L79).

## Questions to take into your own design

- Does the receipt mark a shrink-budget limit?
- Are original input, reduced input and failure category retained together?

## Why this score for a trading system

A narrow failure-reporting lesson, overlapping existing shrinker tools and not a new testing stack recommendation.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
