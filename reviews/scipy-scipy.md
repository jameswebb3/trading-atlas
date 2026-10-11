# SciPy — pair comparisons before resampling

**Decision question:** Does the bootstrap preserve the pairing and dependence in a strategy comparison?

| Field | Review |
| --- | --- |
| Upstream | [SciPy](https://github.com/scipy/scipy) |
| Primary area | Research & Reproducibility |
| Source commit | [b8e6bfd47e1d5d60a06aa847dd45b67a53c4076b](https://github.com/scipy/scipy/commit/b8e6bfd47e1d5d60a06aa847dd45b67a53c4076b) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/scipy/scipy/blob/b8e6bfd47e1d5d60a06aa847dd45b67a53c4076b/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A precise reference for paired bootstrap comparisons. Shared resample indices preserve the relationship between alternatives; trading-day or other dependence blocks still require a separate sampling design. |

## Project overview

SciPy supplies scientific algorithms, including confidence intervals from resampling. [Project documentation](https://github.com/scipy/scipy/blob/b8e6bfd47e1d5d60a06aa847dd45b67a53c4076b/scipy/stats/_resampling.py#L297-L368).

## Mechanism worth inspecting

With `paired=True`, bootstrap input validation requires equal sample lengths and turns the paired inputs into shared observation indices. This keeps two strategy results aligned inside each resample, rather than independently shuffling their outcomes. [Paired input handling](https://github.com/scipy/scipy/blob/b8e6bfd47e1d5d60a06aa847dd45b67a53c4076b/scipy/stats/_resampling.py#L213-L231).

## Important limit

The low-level sampler draws individual indices with replacement; it does not automatically create trading-day or serial-dependence blocks. Pairing and time dependence are separate requirements. BCa intervals can also be degenerate. A trading comparison needs an explicitly chosen sampling unit. [Index sampler](https://github.com/scipy/scipy/blob/b8e6bfd47e1d5d60a06aa847dd45b67a53c4076b/scipy/stats/_resampling.py#L76-L84); [degenerate intervals](https://github.com/scipy/scipy/blob/b8e6bfd47e1d5d60a06aa847dd45b67a53c4076b/scipy/stats/_resampling.py#L418-L420).

## Questions to take into your own design

- Are both alternatives evaluated on the same dates and resampled with the same block indices?
- Does the interval report the block definition and excluded dates alongside the estimate?

## Why this score for a trading system

3/5: a useful paired-comparison reference, but the temporal sampling design and valid trading population must come from the researcher.

**Scope of this review:** Bootstrap pairing, index sampling and interval limitations; not a review of all SciPy statistics.
