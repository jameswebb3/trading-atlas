# TSTL — Reduce failures without changing the failure

**Decision question:** Can a smaller replay fail for a different reason?

| Field | Review |
| --- | --- |
| Upstream | [TSTL](https://github.com/agroce/tstl) |
| Primary area | Testing & Verification |
| Source commit | [4300c8b4910d06ca2781944f9b7da2626c55e241](https://github.com/agroce/tstl/commit/4300c8b4910d06ca2781944f9b7da2626c55e241) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/agroce/tstl/blob/4300c8b4910d06ca2781944f9b7da2626c55e241/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The reducer can capture an original failure for exception matching, choose a failure predicate and reduce the trace with guard-pruning options. A trace that still raises an exception need not preserve the original defect unless the predicate demands it. |

## Project overview

Python property-based test generation, replay, reduction and coverage tooling. [Documentation](https://github.com/agroce/tstl/blob/4300c8b4910d06ca2781944f9b7da2626c55e241/README.md).

## Mechanism worth inspecting

The reducer can capture an original failure for exception matching, choose a failure predicate and reduce the trace with guard-pruning options. It also supports repeated/probabilistic predicates for unstable failures. [Source](https://github.com/agroce/tstl/blob/4300c8b4910d06ca2781944f9b7da2626c55e241/tstl/reduce.py#L228-L241).

## Important limit

A trace that still raises an exception need not preserve the original defect unless the predicate demands it. Disabled guards or changed failure identity can make a reduced example misleading. [Evidence 1](https://github.com/agroce/tstl/blob/4300c8b4910d06ca2781944f9b7da2626c55e241/tstl/reduce.py#L228-L241). [Evidence 2](https://github.com/agroce/tstl/blob/4300c8b4910d06ca2781944f9b7da2626c55e241/tstl/reduce.py#L291-L323).

## Questions to take into your own design

- Does reduction preserve the invariant and failure identity being investigated?
- Are preconditions and repeatability recorded with the reduced trace?

## Why this score for a trading system

Useful failure-reduction controls for adversarial replay, with no need to adopt a separate test DSL.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
