# OSQP — How accurate is a solution labelled solved inaccurate

**Decision question:** How accurate is a solution labelled solved inaccurate?

| Field | Review |
| --- | --- |
| Upstream | [OSQP](https://github.com/osqp/osqp) |
| Primary area | Portfolio & Risk |
| Source commit | [1572ae068e9ce9ca723cf8223548ade1ff7acc29](https://github.com/osqp/osqp/commit/1572ae068e9ce9ca723cf8223548ade1ff7acc29) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/osqp/osqp/blob/1572ae068e9ce9ca723cf8223548ade1ff7acc29/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Separates exact-policy convergence from a result accepted with ten-times wider tolerances. Useful for portfolio wrappers that must recompute budget and exposure limits in business units before accepting weights. |

## Project overview

A numerical solver for convex quadratic objectives subject to linear lower and upper bounds. [Project documentation](https://github.com/osqp/osqp/blob/1572ae068e9ce9ca723cf8223548ade1ff7acc29/README.md#L15-L22).

## Mechanism worth inspecting

The termination check widens absolute, relative and infeasibility tolerances by a factor of ten when evaluating approximate convergence. It assigns SOLVED_INACCURATE separately from SOLVED after residual and duality-gap checks. [Termination logic](https://github.com/osqp/osqp/blob/1572ae068e9ce9ca723cf8223548ade1ff7acc29/src/auxil.c#L808-L847), [status selection](https://github.com/osqp/osqp/blob/1572ae068e9ce9ca723cf8223548ade1ff7acc29/src/auxil.c#L899-L907); [documented statuses](https://github.com/osqp/osqp/blob/1572ae068e9ce9ca723cf8223548ade1ff7acc29/docs/interfaces/status_values.rst#L11-L37).

## Important limit

Solver tolerances are expressed in the numerical model, not directly in portfolio currency or exposure units. The documentation also warns that slightly nonconvex inputs may evade its nonconvexity detection. [Convexity boundary](https://github.com/osqp/osqp/blob/1572ae068e9ce9ca723cf8223548ade1ff7acc29/docs/interfaces/status_values.rst#L40-L52).

## Questions to take into your own design

- Do returned allocations satisfy the original risk constraints in their own units?
- Is an inaccurate result explicitly marked before any rounding or fallback?

## Why this score for a trading system

3/5: a transferable numerical acceptance contract; solver success alone cannot authorise portfolio allocations.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
