# ArbitrageLab — a rolling spread rule needs warm-up evidence

**Decision question:** Do entry checks validate the same window used to calculate the trading statistic?

| Field | Review |
| --- | --- |
| Upstream | [ArbitrageLab](https://github.com/hudson-and-thames/arbitragelab) |
| Primary area | Signals & Models |
| Source commit | [32ccd567e8541965a35293a67944945f6d377f65](https://github.com/hudson-and-thames/arbitragelab/commit/32ccd567e8541965a35293a67944945f6d377f65) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/hudson-and-thames/arbitragelab/blob/32ccd567e8541965a35293a67944945f6d377f65/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Its spread rule exposes separate mean and variance windows. Useful edge cases include incomplete warm-up and a constant final variance window despite a nonconstant full deque; neither should become an unexplained trading signal. |

## Project overview

ArbitrageLab covers pairs-trading methods and strategy-building tools; the inspected rule uses rolling spread z-scores. [Project documentation](https://github.com/hudson-and-thames/arbitragelab/blob/32ccd567e8541965a35293a67944945f6d377f65/README.md#L15-L16).

## Mechanism worth inspecting

The Bollinger rule stores a bounded deque and computes the mean and sample standard deviation over separate trailing slices. Entry checks test whether the standard deviation of the whole stored deque is zero before calculating that score. [Window calculation](https://github.com/hudson-and-thames/arbitragelab/blob/32ccd567e8541965a35293a67944945f6d377f65/arbitragelab/trading/z_score.py#L45-L62); [entry path](https://github.com/hudson-and-thames/arbitragelab/blob/32ccd567e8541965a35293a67944945f6d377f65/arbitragelab/trading/z_score.py#L73-L95).

## Important limit

The entry path shown does not explicitly enforce a complete warm-up for both windows. Its zero-variance guard uses the full deque, which need not match the shorter standard-deviation slice. These are boundary cases to test, not evidence that the strategy produces a trading edge.

## Questions to take into your own design

- Are both rolling windows complete before a signal becomes valid?
- Can a nonconstant full deque contain a constant final standard-deviation window?

## Why this score for a trading system

2/5: a concrete rolling-window boundary reference, but the underlying spread rule offers no established incremental trading value in this review.

**Scope of this review:** One Bollinger spread rule; cointegration methods and the broader strategy library were not evaluated.
