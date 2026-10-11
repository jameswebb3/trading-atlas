# AlphaSuite — Does an outer walk-forward test make inner model selection chronological

**Decision question:** Does an outer walk-forward test make inner model selection chronological?

| Field | Review |
| --- | --- |
| Upstream | [AlphaSuite](https://github.com/rsandx/AlphaSuite) |
| Primary area | Research & Reproducibility |
| Source commit | [eb6587b143c01c70c7a6851d8d9ee7b316c06521](https://github.com/rsandx/AlphaSuite/commit/eb6587b143c01c70c7a6851d8d9ee7b316c06521) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/rsandx/AlphaSuite/blob/eb6587b143c01c70c7a6851d8d9ee7b316c06521/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Provides strategy and walk-forward workflows, but inner model selection uses shuffled validation. Inspect nested split boundaries before interpreting out-of-sample results. |

## Project overview

Quantitative research dashboard built around PyBroker, scanners, model training and walk-forward workflows. [Project documentation](https://github.com/rsandx/AlphaSuite/blob/eb6587b143c01c70c7a6851d8d9ee7b316c06521/README.md#L3-L21).

## Mechanism worth inspecting

The walk-forward class records training-window dates and can tune models. Its inner tuning uses shuffled StratifiedKFold; default training also creates a random stratified validation split. [Training entry](https://github.com/rsandx/AlphaSuite/blob/eb6587b143c01c70c7a6851d8d9ee7b316c06521/prototype/tune_train_pipeline/walkforward.py#L207-L213), [validation split](https://github.com/rsandx/AlphaSuite/blob/eb6587b143c01c70c7a6851d8d9ee7b316c06521/prototype/tune_train_pipeline/walkforward.py#L269-L275), [tuning](https://github.com/rsandx/AlphaSuite/blob/eb6587b143c01c70c7a6851d8d9ee7b316c06521/prototype/tune_train_pipeline/walkforward.py#L472-L478).

## Important limit

Random folds inside an earlier training window are not necessarily a breach of the outer holdout, but they do not preserve chronological label boundaries or purging. An outer walk-forward label alone cannot settle these questions. [CV choice](https://github.com/rsandx/AlphaSuite/blob/eb6587b143c01c70c7a6851d8d9ee7b316c06521/prototype/tune_train_pipeline/walkforward.py#L475-L478), [strategy interface](https://github.com/rsandx/AlphaSuite/blob/eb6587b143c01c70c7a6851d8d9ee7b316c06521/README.md#L200-L223).

## Questions to take into your own design

- Does an outer walk-forward test make inner model selection chronological?
- Do the inner tuning folds respect label horizons and chronological boundaries?

## Why this score for a trading system

2/5: trading-specific orchestration with a concrete validation caution; source reading does not establish reliable causal model selection.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
