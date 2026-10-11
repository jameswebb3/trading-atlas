# Qlib: Fit feature processors on an explicit training interval

**Decision question:** Can a feature transform learn from rows beyond the training window?

| Field | Review |
| --- | --- |
| Upstream | [microsoft/qlib](https://github.com/microsoft/qlib) |
| Primary area | Signals & Models |
| Source commit | [be725493eb1a6bbb42bf11b37aa7669f59610ff1](https://github.com/microsoft/qlib/commit/be725493eb1a6bbb42bf11b37aa7669f59610ff1) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/microsoft/qlib/blob/be725493eb1a6bbb42bf11b37aa7669f59610ff1/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Passes fit_start_time and fit_end_time into processors that declare those parameters. The guard only applies to processors with those constructor arguments; it does not certify every transform is causal. |

## Mechanism worth inspecting

The data configuration distinguishes the overall data period from the processor fit period. check_transform_proc asserts both fit bounds for processor classes that declare them, then injects the bounds into construction. This makes fitted feature state visibly tied to training time.

**Source trail:** [project overview](https://github.com/microsoft/qlib/blob/be725493eb1a6bbb42bf11b37aa7669f59610ff1/README.md) · [documentation](https://github.com/microsoft/qlib/blob/be725493eb1a6bbb42bf11b37aa7669f59610ff1/docs/component/data.rst#L349-L355) · [implementation](https://github.com/microsoft/qlib/blob/be725493eb1a6bbb42bf11b37aa7669f59610ff1/qlib/contrib/data/handler.py#L12-L26).

## Important limit

A processor that does not declare the fit-bound arguments bypasses this particular guard. The repository’s stock-oriented examples do not establish alpha for crypto perpetuals.

## Questions to take into your own design

- Does each fitted transform record the exact training cutoff?
- Can an unbounded transform enter the pipeline without a causal audit?

## Why this score for a trading system

Explicit processor fit windows address trading feature leakage, but only processors declaring the bounds receive this guard.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
