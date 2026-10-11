# Blueshift Strategy Examples — Zero selected assets can mean all assets

**Decision question:** What happens when the selected fraction rounds down to zero?

| Field | Review |
| --- | --- |
| Upstream | [Blueshift Strategy Examples](https://github.com/QuantInsti/blueshift-demo-strategies) |
| Primary area | Signals & Models |
| Source commit | [8dfeb49f615dbd57acf092924fdfc1fb8c336f37](https://github.com/QuantInsti/blueshift-demo-strategies/commit/8dfeb49f615dbd57acf092924fdfc1fb8c336f37) |
| Reviewed | 2026-09-27 |
| Declared license | [Not established in the inspected root](https://github.com/QuantInsti/blueshift-demo-strategies/tree/8dfeb49f615dbd57acf092924fdfc1fb8c336f37) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The cross-sectional momentum example computes n as an integer fraction of the universe. For n=0, Python's [-0:] slice selects the entire index. |

## Project overview

Trading-strategy examples for the Blueshift research and backtesting platform. [Documentation](https://github.com/QuantInsti/blueshift-demo-strategies/blob/8dfeb49f615dbd57acf092924fdfc1fb8c336f37/README.md).

## Mechanism worth inspecting

The cross-sectional momentum example computes n as an integer fraction of the universe. Its n==0 branch clears the lists, but execution continues into index[-n:]. [Source](https://github.com/QuantInsti/blueshift-demo-strategies/blob/8dfeb49f615dbd57acf092924fdfc1fb8c336f37/equities/cross_sectional_momentum.py#L66-L100).

## Important limit

For n=0, Python's [-0:] slice selects the entire index. The inspected example can therefore produce a full long list where no selections were intended. No root license text was found in the pinned tree. [Evidence 1](https://github.com/QuantInsti/blueshift-demo-strategies/blob/8dfeb49f615dbd57acf092924fdfc1fb8c336f37/equities/cross_sectional_momentum.py#L66-L100).

## Questions to take into your own design

- Does a tiny universe return no trades before any ranking slice?
- Are selected long and short counts checked against the requested count?

## Why this score for a trading system

A useful, concrete ranking boundary counterexample; the strategy and its performance are not recommendations, and reuse rights were not established.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
