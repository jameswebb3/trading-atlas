# PyBroker: walk-forward boundaries depend on label lookahead

**Decision question:** Does a walk-forward split hold out the target horizon?

| Field | Review |
| --- | --- |
| Upstream | [PyBroker](https://github.com/edtechre/pybroker) |
| Primary area | Backtesting & Simulation |
| Source commit | [95e00fecb1006490601aca7e2e8de609f032e12d](https://github.com/edtechre/pybroker/commit/95e00fecb1006490601aca7e2e8de609f032e12d) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0 with Commons Clause](https://github.com/edtechre/pybroker/blob/95e00fecb1006490601aca7e2e8de609f032e12d/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Requires a positive lookahead in its walk-forward splitter and describes holding out that many bars before the test boundary, including model-specific intervals. This helps avoid a common label leak, but row counts still need event-time and publication-time checks. |

## Mechanism worth inspecting

The [README](https://github.com/edtechre/pybroker/blob/95e00fecb1006490601aca7e2e8de609f032e12d/README.md#L22-L30) describes walk-forward model training and backtesting. The [split contract](https://github.com/edtechre/pybroker/blob/95e00fecb1006490601aca7e2e8de609f032e12d/src/pybroker/strategy.py#L1563-L1604) requires a lookahead measured in the model's own interval and says no test bar fits that window's model. The [input validation](https://github.com/edtechre/pybroker/blob/95e00fecb1006490601aca7e2e8de609f032e12d/src/pybroker/strategy.py#L1606-L1616) rejects zero lookahead and empty data. This is a more concrete guard than a generic train/test date split.

## Important limit

The [license carries a Commons Clause](https://github.com/edtechre/pybroker/blob/95e00fecb1006490601aca7e2e8de609f032e12d/LICENSE#L1-L11), so it is source-available with commercial-use restrictions. A fixed bar count does not handle labels with varying event ends, revised features, or exchange-specific available-at time.

## Questions to take into your own design

- Is lookahead expressed in the same interval as each model's target?
- Do variable label horizons and feature publication delays require additional purging?

## Why this score for a trading system

Its explicit model-interval lookahead boundary is directly useful for backtest validation, with licensing and variable-horizon limits.

**Scope of this review:** We read the pinned README, license, and walk-forward splitter. We did not run a backtest or test every model path.
