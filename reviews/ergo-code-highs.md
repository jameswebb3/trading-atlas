# HiGHS — Can a returned solution vector exist while its validity has been invalidated

**Decision question:** Can a returned solution vector exist while its validity has been invalidated?

| Field | Review |
| --- | --- |
| Upstream | [HiGHS](https://github.com/ERGO-Code/HiGHS) |
| Primary area | Portfolio & Risk |
| Source commit | [73cac48c5340d775a477087198611862559be250](https://github.com/ERGO-Code/HiGHS/commit/73cac48c5340d775a477087198611862559be250) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT; optional components carry additional notices](https://github.com/ERGO-Code/HiGHS/blob/73cac48c5340d775a477087198611862559be250/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Retains solution validity separately from the numeric arrays and invalidates old evidence as model dimensions change. Useful for preventing stale allocations from surviving a model update. |

## Project overview

A numerical optimisation suite for linear, mixed-integer and quadratic models. [Project documentation](https://github.com/ERGO-Code/HiGHS/blob/73cac48c5340d775a477087198611862559be250/README.md#L47-L57).

## Mechanism worth inspecting

The implementation clears primal and dual solution-status evidence when invalidating a solution. When model dimensions grow, it resizes vectors but marks previously undersized values and duals invalid. The guide separately exposes model status, scalar information and solution data. [Invalidation](https://github.com/ERGO-Code/HiGHS/blob/73cac48c5340d775a477087198611862559be250/highs/lp_data/Highs.cpp#L3949-L3959); [resize and validity](https://github.com/ERGO-Code/HiGHS/blob/73cac48c5340d775a477087198611862559be250/highs/lp_data/Highs.cpp#L4703-L4737); [result interface](https://github.com/ERGO-Code/HiGHS/blob/73cac48c5340d775a477087198611862559be250/docs/src/guide/basic.md#L94-L104).

## Important limit

A populated or correctly sized array does not establish feasibility or optimality. A portfolio wrapper must preserve model identity, solution validity and termination status instead of treating vector shape as acceptance.

## Questions to take into your own design

- Does changing the model invalidate its previous allocation and acceptance evidence?
- Are model status, solution validity and objective data kept as separate fields?

## Why this score for a trading system

3/5: an inspectable transferable stale-result boundary; application risk constraints require an additional check.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
