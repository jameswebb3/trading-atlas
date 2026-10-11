# Clarabel — Can a solver's recovered result have weaker convergence guarantees than a normal solution

**Decision question:** Can a solver's recovered result have weaker convergence guarantees than a normal solution?

| Field | Review |
| --- | --- |
| Upstream | [Clarabel](https://github.com/oxfordcontrol/Clarabel.rs) |
| Primary area | Portfolio & Risk |
| Source commit | [b6aa0421ec818a31c7f26ada8f6cef2558c768bf](https://github.com/oxfordcontrol/Clarabel.rs/commit/b6aa0421ec818a31c7f26ada8f6cef2558c768bf) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/oxfordcontrol/Clarabel.rs/blob/b6aa0421ec818a31c7f26ada8f6cef2558c768bf/LICENSE.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Labels reduced-tolerance convergence separately from full convergence. Useful for keeping fallback numerical outcomes visible instead of flattening every returned vector into an accepted portfolio. |

## Project overview

An interior-point conic optimisation solver implemented in Rust, with a Python interface. [Project documentation](https://github.com/oxfordcontrol/Clarabel.rs/blob/b6aa0421ec818a31c7f26ada8f6cef2558c768bf/README.md#L8-L8).

## Mechanism worth inspecting

The information implementation has separate full and reduced convergence tolerances. Reduced convergence assigns AlmostSolved or approximate infeasibility states instead of the corresponding full states. [Full and reduced checks](https://github.com/oxfordcontrol/Clarabel.rs/blob/b6aa0421ec818a31c7f26ada8f6cef2558c768bf/src/solver/implementations/default/info.rs#L277-L337).

## Important limit

AlmostSolved is a distinct numerical acceptance level, not a promise that each portfolio constraint is within an application-specific budget. A caller must retain the status and check returned allocations against original units.

## Questions to take into your own design

- Can a reduced-tolerance result be distinguished throughout the downstream report?
- Which constraint tolerances are acceptable in currency, exposure and contract units?

## Why this score for a trading system

3/5: a clear transferable result-quality distinction, with portfolio policy outside the solver.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
