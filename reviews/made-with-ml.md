# Made With ML: report performance by slice with its sample count

**Decision question:** Can an overall model score hide weak performance in a relevant slice?

| Field | Review |
| --- | --- |
| Upstream | [Made With ML](https://github.com/GokuMohandas/Made-With-ML) |
| Primary area | Research & Reproducibility |
| Source commit | [3361aeb8ddfc2affdba9f545c978c38c85cee764](https://github.com/GokuMohandas/Made-With-ML/commit/3361aeb8ddfc2affdba9f545c978c38c85cee764) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/GokuMohandas/Made-With-ML/blob/3361aeb8ddfc2affdba9f545c978c38c85cee764/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Provides an inspectable evaluation report with overall, per-class, and slice metrics tied to a model run. Sample counts accompany the scores, exposing how much evidence supports each result rather than presenting one aggregate number. |

## Project overview

A practical ML engineering course includes training, deployment, and evaluation examples. [Project documentation](https://github.com/GokuMohandas/Made-With-ML/blob/3361aeb8ddfc2affdba9f545c978c38c85cee764/README.md#L46-L82).

## Mechanism worth inspecting

[Metric helpers](https://github.com/GokuMohandas/Made-With-ML/blob/3361aeb8ddfc2affdba9f545c978c38c85cee764/madewithml/evaluate.py#L23-L64) report sample counts alongside scores. [Slice evaluation](https://github.com/GokuMohandas/Made-With-ML/blob/3361aeb8ddfc2affdba9f545c978c38c85cee764/madewithml/evaluate.py#L67-L105) applies named masks, and [report assembly](https://github.com/GokuMohandas/Made-With-ML/blob/3361aeb8ddfc2affdba9f545c978c38c85cee764/madewithml/evaluate.py#L109-L150) attaches timestamp and run ID while reusing the saved preprocessor.

## Important limit

[Empty masks are skipped](https://github.com/GokuMohandas/Made-With-ML/blob/3361aeb8ddfc2affdba9f545c978c38c85cee764/madewithml/evaluate.py#L90-L105). The example evaluates text classification, uses no minimum slice size, and does not address trading dependence, repeated comparisons, or publication-time leakage.

## Questions to take into your own design

- Are evaluation slices declared before seeing their outcomes?
- Do reports show missing slices and effective evidence size as well as point estimates?

## Why this score for a trading system

3/5: a clear evaluation-report pattern with visible denominators; trading-specific validity checks still need to be built separately.

**Scope of this review:** README, generated evaluation API documentation, evaluation source; no model execution.
