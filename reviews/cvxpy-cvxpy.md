# CVXPY — Is solver success enough to accept portfolio weights

**Decision question:** Is solver success enough to accept portfolio weights?

| Field | Review |
| --- | --- |
| Upstream | [CVXPY](https://github.com/cvxpy/cvxpy) |
| Primary area | Portfolio & Risk |
| Source commit | [322551276e2c4316abc835f417f01ca38a813f99](https://github.com/cvxpy/cvxpy/commit/322551276e2c4316abc835f417f01ca38a813f99) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/cvxpy/cvxpy/blob/322551276e2c4316abc835f417f01ca38a813f99/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful optimization reference for separating solver status from constraint satisfaction. Portfolio acceptance should check residuals in explicit units and repeat hard limits after quantities are rounded. |

## Project overview

CVXPY models constrained optimization problems and delegates numerical solutions to selected solvers. [Project documentation](https://github.com/cvxpy/cvxpy/blob/322551276e2c4316abc835f417f01ca38a813f99/README.md).

## Mechanism worth inspecting

The solve path warns on inaccurate statuses before unpacking a result. The constraint API separately exposes violation and an explicit absolute-tolerance check. [Status handling](https://github.com/cvxpy/cvxpy/blob/322551276e2c4316abc835f417f01ca38a813f99/cvxpy/problems/problem.py#L1444-L1461), [residual gate](https://github.com/cvxpy/cvxpy/blob/322551276e2c4316abc835f417f01ca38a813f99/cvxpy/constraints/constraint.py#L209-L256).

## Important limit

Warnings do not create an application-level acceptance policy. Constraint residuals are meaningful only in declared units, and weights must be checked again after rounding, sizing and execution constraints.

## Questions to take into your own design

- Is solver success enough to accept portfolio weights?
- Which hard limits are rechecked after solver output is converted to tradable quantities?

## Why this score for a trading system

3/5: strong transferable numerical acceptance pattern, but CVXPY supplies neither a trading risk policy nor the final post-sizing checks.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
