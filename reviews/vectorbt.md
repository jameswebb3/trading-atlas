# VectorBT: fast parameter sweeps still need a trial ledger

**Decision question:** What changes when thousands of strategy variants become cheap to test?

| Field | Review |
| --- | --- |
| Upstream | [VectorBT](https://github.com/polakowo/vectorbt) |
| Primary area | Backtesting & Simulation |
| Source commit | [a3c0f40979648585b4581fc4694fd6e92b3fffca](https://github.com/polakowo/vectorbt/commit/a3c0f40979648585b4581fc4694fd6e92b3fffca) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0 with Commons Clause](https://github.com/polakowo/vectorbt/blob/a3c0f40979648585b4581fc4694fd6e92b3fffca/LICENSE.md#L1-L13) |
| Review depth | 2/3: README, portfolio design, and order-processing source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Packs parameter combinations into arrays and records order-level simulation results. Its own example evaluates 10,000 SMA pairs, which makes search breadth easy to hide unless every attempted variant is counted. The community edition explicitly leaves limit orders, leverage, and futures contract multipliers to Pro. |

## Mechanism worth inspecting

The [overview](https://github.com/polakowo/vectorbt/blob/a3c0f40979648585b4581fc4694fd6e92b3fffca/README.md#L47-L73) describes broadcasted parameter sweeps. Its [10,000-combination example](https://github.com/polakowo/vectorbt/blob/a3c0f40979648585b4581fc4694fd6e92b3fffca/README.md#L162-L179) generates many SMA pairs and plots their returns. The [portfolio design](https://github.com/polakowo/vectorbt/blob/a3c0f40979648585b4581fc4694fd6e92b3fffca/vectorbt/portfolio/base.py#L38-L62) broadcasts inputs, traverses the time and asset axes, and appends fill records. The [order path](https://github.com/polakowo/vectorbt/blob/a3c0f40979648585b4581fc4694fd6e92b3fffca/vectorbt/portfolio/nb.py#L73-L100) applies a price adjustment and cash limit. None of these mechanics by itself corrects for selecting the best of many trials.

## Important limit

The [README marks limit orders, leverage, and futures multipliers as Pro features](https://github.com/polakowo/vectorbt/blob/a3c0f40979648585b4581fc4694fd6e92b3fffca/README.md#L136-L141). The [Commons Clause](https://github.com/polakowo/vectorbt/blob/a3c0f40979648585b4581fc4694fd6e92b3fffca/LICENSE.md#L1-L13) restricts sale of the software; this should not be described as an ordinary Apache-licensed open-source dependency. The useful reference here is the research workflow and its selection-risk warning, not a ready perpetuals engine.

## Questions to take into your own design

- Is every generated parameter pair logged, including those discarded before a final chart?
- Are validation folds and the final untouched period fixed before a sweep starts?
- Does the simulator model the instrument and order types required by the decision?

## Why this score for a trading system

Its array-based sweep is directly useful for research throughput, but the visible 10,000-trial path raises selection risk and the community edition lacks stated perpetual execution features.

**Scope of this review:** We read the pinned README, license, portfolio design, and selected order-processing code. We did not run a sweep or evaluate Pro.
