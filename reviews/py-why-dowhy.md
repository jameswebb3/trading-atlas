# DoWhy — a permutation placebo needs the right null

**Decision question:** Does a placebo preserve the temporal structure of the data it challenges?

| Field | Review |
| --- | --- |
| Upstream | [DoWhy](https://github.com/py-why/dowhy) |
| Primary area | Research & Reproducibility |
| Source commit | [cc23521127ba21ade40514539ae7b91db27ca54a](https://github.com/py-why/dowhy/commit/cc23521127ba21ade40514539ae7b91db27ca54a) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/py-why/dowhy/blob/cc23521127ba21ade40514539ae7b91db27ca54a/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its placebo code makes the null generator inspectable. For time-series research, row permutation can erase important structure; use a justified temporal null before interpreting a passed refutation. |

## Project overview

DoWhy organizes causal analysis and refutation; its placebo refuter can generate random treatments or permute observed treatments. [Project documentation](https://github.com/py-why/dowhy/blob/cc23521127ba21ade40514539ae7b91db27ca54a/dowhy/causal_refuters/placebo_treatment_refuter.py#L30-L61).

## Mechanism worth inspecting

The permutation path samples row indices without replacement and assigns the reordered treatment by position. With instrumental-variable estimators it also reorders the associated instruments. [Permutation implementation](https://github.com/py-why/dowhy/blob/cc23521127ba21ade40514539ae7b91db27ca54a/dowhy/causal_refuters/placebo_treatment_refuter.py#L159-L175).

## Important limit

An arbitrary row permutation can destroy serial dependence, seasonality and clustering. A passed refutation therefore tests the supplied null, not every plausible explanation for a trading relationship. Block or calendar-aware placebo construction must match the research question.

## Questions to take into your own design

- Which dependencies must the placebo retain for the financial hypothesis?
- Does the experiment record the null generator and its invalidation conditions?

## Why this score for a trading system

2/5: a useful refutation-design caution, but causal assumptions and suitable temporal nulls dominate the added value for trading.

**Scope of this review:** Placebo treatment generation; not verification of causal identification or estimator assumptions.
