# Optuna — Does a feasible best trial represent all the research that was tried

**Decision question:** Does a feasible best trial represent all the research that was tried?

| Field | Review |
| --- | --- |
| Upstream | [Optuna](https://github.com/optuna/optuna) |
| Primary area | Research & Reproducibility |
| Source commit | [0d05a967362d22414d759b3e3f382f2d883d948b](https://github.com/optuna/optuna/commit/0d05a967362d22414d759b3e3f382f2d883d948b) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/optuna/optuna/blob/0d05a967362d22414d759b3e3f382f2d883d948b/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful experiment-management reference for trial states and constrained selection. Preserve every attempted configuration and explicit constraint version; a feasible winner does not establish an unbiased trading result. |

## Project overview

Optuna manages parameter-search studies as collections of trials, with sampling, pruning and recorded trial states. [Project documentation](https://github.com/optuna/optuna/blob/0d05a967362d22414d759b3e3f382f2d883d948b/README.md#L37-L63).

## Mechanism worth inspecting

The feasible-trial helper filters recorded constraints by nonpositive values. The study's best-trial path uses completed feasible trials when the nominal winner violates constraints. [Constraint filter](https://github.com/optuna/optuna/blob/0d05a967362d22414d759b3e3f382f2d883d948b/optuna/study/_constrained_optimization.py#L23-L35), [selection](https://github.com/optuna/optuna/blob/0d05a967362d22414d759b3e3f382f2d883d948b/optuna/study/study.py#L314-L353).

## Important limit

Recorded constraints define eligibility; an absent constraint set does not validate a trading rule. Ranking successful trials also does not account for the campaign's statistical search burden. The FAQ warns that parallel runs are not reproduced by a seed alone. [Reproducibility](https://github.com/optuna/optuna/blob/0d05a967362d22414d759b3e3f382f2d883d948b/docs/source/faq.rst#L194-L215).

## Questions to take into your own design

- Does a feasible best trial represent all the research that was tried?
- Where are failed and pruned attempts counted in the campaign's selection budget?

## Why this score for a trading system

3/5: concrete research bookkeeping and feasibility selection, but validation, multiplicity and trading objectives remain outside the optimizer.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
