# AlphaPy: inspect where preprocessing learns its parameters

**Decision question:** Can a declared train/test split still leak through feature preprocessing?

| Field | Review |
| --- | --- |
| Upstream | [AlphaPy](https://github.com/ScottfreeLLC/AlphaPy) |
| Primary area | Signals & Models |
| Source commit | [f7a14b6da031e1f05693578907f82189559419dc](https://github.com/ScottfreeLLC/AlphaPy/commit/f7a14b6da031e1f05693578907f82189559419dc) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/ScottfreeLLC/AlphaPy/blob/f7a14b6da031e1f05693578907f82189559419dc/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Provides configurable market-model feature pipelines. The inspected code fits categorical encoders on training data, but its combined-data feature path also fits scalers across all rows, illustrating why preprocessing boundaries need their own review. |

## Project overview

A legacy machine-learning framework includes MarketFlow examples for financial prediction. [Project documentation](https://github.com/ScottfreeLLC/AlphaPy/blob/f7a14b6da031e1f05693578907f82189559419dc/README.rst#L6-L27).

## Mechanism worth inspecting

[Categorical encoding](https://github.com/ScottfreeLLC/AlphaPy/blob/f7a14b6da031e1f05693578907f82189559419dc/alphapy/features.py#L564-L590) fits training rows and transforms test rows separately. In contrast, [create_features](https://github.com/ScottfreeLLC/AlphaPy/blob/f7a14b6da031e1f05693578907f82189559419dc/alphapy/features.py#L967-L979) accepts combined data, builds numerical/text features from it, and [fits a scaler](https://github.com/ScottfreeLLC/AlphaPy/blob/f7a14b6da031e1f05693578907f82189559419dc/alphapy/features.py#L1038-L1076) on the resulting combined matrix. The [market tutorial](https://github.com/ScottfreeLLC/AlphaPy/blob/f7a14b6da031e1f05693578907f82189559419dc/docs/tutorials/market.rst#L52-L80) shows how these features enter a market model.

## Important limit

Combined-data fit operations can reveal test-distribution information to training. The [README](https://github.com/ScottfreeLLC/AlphaPy/blob/f7a14b6da031e1f05693578907f82189559419dc/README.rst#L11-L27) identifies this repository as legacy and points to a separate successor, which was not evaluated here.

## Questions to take into your own design

- Is every learned preprocessing parameter fitted only within the current training window?
- Can a test fixture detect changes to training outputs when future rows change?

## Why this score for a trading system

2/5: useful as a specific preprocessing-leakage example; the inspected legacy path should not serve as a causal evaluation template.

**Scope of this review:** README, market tutorial, feature creation and factor-encoding source; successor not reviewed.
