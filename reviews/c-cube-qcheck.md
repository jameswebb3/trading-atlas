# QCheck — Can a passing property have tested too few valid examples

**Decision question:** Can a passing property have tested too few valid examples?

| Field | Review |
| --- | --- |
| Upstream | [QCheck](https://github.com/c-cube/qcheck) |
| Primary area | Testing & Verification |
| Source commit | [77ef95f60e4c15c867e4c4fd2305fc3edfc67462](https://github.com/c-cube/qcheck/commit/77ef95f60e4c15c867e4c4fd2305fc3edfc67462) |
| Reviewed | 2026-09-26 |
| Declared license | [BSD-2-Clause](https://github.com/c-cube/qcheck/blob/77ef95f60e4c15c867e4c4fd2305fc3edfc67462/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful testing reference for an easily missed acceptance policy. Too few valid examples can produce only a warning by default; critical trading properties should require coverage thresholds that fail the run. |

## Project overview

QCheck provides property-based testing for OCaml, including generator statistics and configurable handling of failed preconditions. [Project documentation](https://github.com/c-cube/qcheck/blob/77ef95f60e4c15c867e4c4fd2305fc3edfc67462/README.adoc#L6-L29).

## Mechanism worth inspecting

The test runner compares accepted examples with the target count. Insufficient acceptance can append a warning or turn the result into a failure, depending on policy; the default policy is warning at a 5% threshold. [Default](https://github.com/c-cube/qcheck/blob/77ef95f60e4c15c867e4c4fd2305fc3edfc67462/src/core/QCheck2.ml#L1612-L1616), [coverage gate](https://github.com/c-cube/qcheck/blob/77ef95f60e4c15c867e4c4fd2305fc3edfc67462/src/core/QCheck2.ml#L1938-L1959), [API](https://github.com/c-cube/qcheck/blob/77ef95f60e4c15c867e4c4fd2305fc3edfc67462/src/core/QCheck2.mli#L1763-L1785).

## Important limit

A warning can coexist with a successful property state. Trading checks need an explicit fatal coverage policy and scenario counts; accepted random examples alone do not prove coverage of rare event races.

## Questions to take into your own design

- Can a passing property have tested too few valid examples?
- Which critical properties fail when too few generated inputs meet their preconditions?

## Why this score for a trading system

3/5: a precise transferable test-validity boundary, with no trading-specific generator or invariant supplied by the framework.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
