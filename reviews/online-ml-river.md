# River — evaluate when labels arrive, not when rows arrive

**Decision question:** When may an online experiment learn from a future-return label?

| Field | Review |
| --- | --- |
| Upstream | [River](https://github.com/online-ml/river) |
| Primary area | Research & Reproducibility |
| Source commit | [129fc74ceb5b20a903ee57962dcb888d32b379c9](https://github.com/online-ml/river/commit/129fc74ceb5b20a903ee57962dcb888d32b379c9) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/online-ml/river/blob/129fc74ceb5b20a903ee57962dcb888d32b379c9/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its evaluator separates predictions from delayed answers and learns only when feedback arrives. A useful design reference for online research where future-return labels mature after the trading decision. |

## Project overview

River supports incremental learning on data streams and progressive evaluation in production-like event order. [Project documentation](https://github.com/online-ml/river/blob/129fc74ceb5b20a903ee57962dcb888d32b379c9/docs/introduction/basic-concepts.md#L49-L59).

## Mechanism worth inspecting

Progressive validation accepts a label delay. When features arrive without a label, it stores the prediction; when the answer arrives, it retrieves that prediction, updates the metric and only then learns. Prediction time and feedback time are distinct events. [Delay API](https://github.com/online-ml/river/blob/129fc74ceb5b20a903ee57962dcb888d32b379c9/river/evaluate/progressive_validation.py#L169-L178); [prediction/answer path](https://github.com/online-ml/river/blob/129fc74ceb5b20a903ee57962dcb888d32b379c9/river/evaluate/progressive_validation.py#L133-L155).

## Important limit

The supplied moment and delay define what the evaluator believes was available. A chronological row stream with immediate future-return labels still gives the model premature feedback. Overlapping horizons, revised labels, fees and executed-return targets need additional definitions.

## Questions to take into your own design

- Is label availability the end of the horizon plus any settlement or ingestion delay?
- Does replay retain the original prediction when a label arrives out of order?

## Why this score for a trading system

3/5: a strong transferable feedback-clock pattern, but trading targets, costs and label provenance remain outside this generic evaluator.

**Scope of this review:** Delayed progressive-validation events, not the profitability or stability of River models.
