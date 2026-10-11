# MLOps Python Package — Newest version is not an approval criterion

**Decision question:** Does model promotion perform an evidence gate?

| Field | Review |
| --- | --- |
| Upstream | [MLOps Python Package](https://github.com/fmind/mlops-python-package) |
| Primary area | Research & Reproducibility |
| Source commit | [a8a6ab1a4a479c72f8eb989b4390cae42995f751](https://github.com/fmind/mlops-python-package/commit/a8a6ab1a4a479c72f8eb989b4390cae42995f751) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/fmind/mlops-python-package/blob/a8a6ab1a4a479c72f8eb989b4390cae42995f751/LICENSE.txt) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | PromotionJob selects the highest model version when no version is provided, assigns an alias and reads the alias back before sending a completion notification. The inspected promotion job does not check statistical evidence, risk constraints or data identity. |

## Project overview

Python MLOps example package covering training, registry, jobs and service boundaries. [Documentation](https://github.com/fmind/mlops-python-package/blob/a8a6ab1a4a479c72f8eb989b4390cae42995f751/README.md).

## Mechanism worth inspecting

PromotionJob selects the highest model version when no version is provided, assigns an alias and reads the alias back before sending a completion notification. [Source](https://github.com/fmind/mlops-python-package/blob/a8a6ab1a4a479c72f8eb989b4390cae42995f751/src/bikes/jobs/promotion.py#L12-L57).

## Important limit

The inspected promotion job does not check statistical evidence, risk constraints or data identity. A separate upstream admission process would have to establish those conditions. [Evidence 1](https://github.com/fmind/mlops-python-package/blob/a8a6ab1a4a479c72f8eb989b4390cae42995f751/src/bikes/jobs/promotion.py#L12-L57).

## Questions to take into your own design

- Is promotion bound to an explicitly approved immutable version?
- Can an unspecified version promote an unreviewed latest artifact?

## Why this score for a trading system

A clear lifecycle example with a visible admission gap in the reviewed job, but a generic registry stack offers limited incremental trading value.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
