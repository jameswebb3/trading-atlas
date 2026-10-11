# OR-Tools — Does a feasible discrete allocation mean it is optimal

**Decision question:** Does a feasible discrete allocation mean it is optimal?

| Field | Review |
| --- | --- |
| Upstream | [OR-Tools](https://github.com/google/or-tools) |
| Primary area | Portfolio & Risk |
| Source commit | [100f66e6242ab8bf8d32feb8f3bf086db66ae2b5](https://github.com/google/or-tools/commit/100f66e6242ab8bf8d32feb8f3bf086db66ae2b5) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/google/or-tools/blob/100f66e6242ab8bf8d32feb8f3bf086db66ae2b5/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Provides explicit states for a discrete solve, including a feasible incumbent without an optimality proof. Useful when integer allocation constraints are a real requirement; otherwise a specialised tool to keep in reserve. |

## Project overview

Google's combinatorial optimisation suite, covering constraint programming and related optimisation problems. [Project documentation](https://github.com/google/or-tools/blob/100f66e6242ab8bf8d32feb8f3bf086db66ae2b5/README.md#L13-L13).

## Mechanism worth inspecting

The CP-SAT status schema distinguishes unknown, invalid, feasible, infeasible and optimal outcomes, and documents exceptions to the ordinary interpretation of optimal for feasibility and gap-limited searches. The Python solve method returns that status from the solver response. [Status contract](https://github.com/google/or-tools/blob/100f66e6242ab8bf8d32feb8f3bf086db66ae2b5/ortools/sat/cp_model.proto#L692-L718); [Python solve path](https://github.com/google/or-tools/blob/100f66e6242ab8bf8d32feb8f3bf086db66ae2b5/ortools/sat/python/cp_model.py#L1752-L1779).

## Important limit

FEASIBLE does not prove optimality, and OPTIMAL must be interpreted with the configured gap or feasibility objective. Integer lot modelling can be useful, but that need does not justify adding a combinatorial solver to every portfolio system.

## Questions to take into your own design

- Is the accepted result feasible, proven optimal or accepted at a declared gap limit?
- Does the recorded model reproduce contract lots and risk bounds exactly?

## Why this score for a trading system

2/5: a sound transferable result contract, but discrete optimisation is an unestablished requirement for many trading stacks.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
