# ECOS — Can a solver return a best iterate after numerical failure without a valid solution

**Decision question:** Can a solver return a best iterate after numerical failure without a valid solution?

| Field | Review |
| --- | --- |
| Upstream | [ECOS](https://github.com/embotech/ecos) |
| Primary area | Portfolio & Risk |
| Source commit | [5d3aa62ef437e41c0314b4a16427d5d06a90b7e6](https://github.com/embotech/ecos/commit/5d3aa62ef437e41c0314b4a16427d5d06a90b7e6) |
| Reviewed | 2026-09-27 |
| Declared license | [GPL-3.0](https://github.com/embotech/ecos/blob/5d3aa62ef437e41c0314b4a16427d5d06a90b7e6/COPYING) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Restores a best numerical iterate while still reporting failed or reduced-accuracy convergence. Useful as a caution against accepting any returned vector, with limited additional value beyond other solver-status references. |

## Project overview

An embedded numerical solver for convex second-order and exponential cone problems. [Project documentation](https://github.com/embotech/ecos/blob/5d3aa62ef437e41c0314b4a16427d5d06a90b7e6/README.md#L8-L20).

## Mechanism worth inspecting

On a numerical safeguard, the solver restores its best iterate and tests reduced-accuracy exit conditions. If those conditions still fail, it returns a numerical-problem status rather than silently declaring success. [Safeguard recovery](https://github.com/embotech/ecos/blob/5d3aa62ef437e41c0314b4a16427d5d06a90b7e6/src/ecos.c#L1140-L1159); [reduced tolerances](https://github.com/embotech/ecos/blob/5d3aa62ef437e41c0314b4a16427d5d06a90b7e6/src/ecos.c#L168-L195).

## Important limit

The restored vector remains data to evaluate under its exit status, not an authorised allocation. Core licensing is GPL-3.0, with alternative licensing mentioned in the README; this review proposes the acceptance pattern rather than source adoption. [License statement](https://github.com/embotech/ecos/blob/5d3aa62ef437e41c0314b4a16427d5d06a90b7e6/README.md#L60-L63).

## Questions to take into your own design

- Can an allocation be rejected even when the solver returns finite numbers?
- Does reduced convergence retain its status and original constraint violations?

## Why this score for a trading system

2/5: a narrow numerical recovery caution, overlapping other solvers and carrying stronger source-adoption constraints.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
