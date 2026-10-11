# cutebacktests: preserve how a simulated fill was priced

**Decision question:** Can quote-based and bar-based simulated fills be distinguished in the results?

| Field | Review |
| --- | --- |
| Upstream | [cutebacktests](https://github.com/cutemarkets/cutebacktests) |
| Primary area | Backtesting & Simulation |
| Source commit | [4b3eb3904a8a662e5708029f03d63a3946ed6144](https://github.com/cutemarkets/cutebacktests/commit/4b3eb3904a8a662e5708029f03d63a3946ed6144) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/cutemarkets/cutebacktests/blob/4b3eb3904a8a662e5708029f03d63a3946ed6144/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Builds an options backtesting runtime around execution delays, quote-aware pricing, and historical contract reconstruction. The inspected pricing path records which quote or bar route supplied a fill, making execution evidence inspectable rather than blending different price assumptions. |

## Project overview

A DuckDB-backed runtime supports historical and intraday U.S. equity-option research. [Project documentation](https://github.com/cutemarkets/cutebacktests/blob/4b3eb3904a8a662e5708029f03d63a3946ed6144/README.md#L5-L25).

## Mechanism worth inspecting

The [realism documentation](https://github.com/cutemarkets/cutebacktests/blob/4b3eb3904a8a662e5708029f03d63a3946ed6144/docs/realism.md#L5-L36) distinguishes signal time, delayed fills, and historical chains. The [pricing path](https://github.com/cutemarkets/cutebacktests/blob/4b3eb3904a8a662e5708029f03d63a3946ed6144/src/cutebacktests/backtest/intraday_pricing.py#L258-L281) tracks fallback and source fields, [checks quote availability](https://github.com/cutemarkets/cutebacktests/blob/4b3eb3904a8a662e5708029f03d63a3946ed6144/src/cutebacktests/backtest/intraday_pricing.py#L313-L354), and [records quote pricing routes and timestamps](https://github.com/cutemarkets/cutebacktests/blob/4b3eb3904a8a662e5708029f03d63a3946ed6144/src/cutebacktests/backtest/intraday_pricing.py#L555-L596).

## Important limit

The [entry readiness check](https://github.com/cutemarkets/cutebacktests/blob/4b3eb3904a8a662e5708029f03d63a3946ed6144/src/cutebacktests/backtest/intraday_pricing.py#L339-L354) tests positive leg prices, not a full executable depth guarantee. The README identifies provider-backed default workflows, and this review does not validate historical contract coverage or replicate results.

## Questions to take into your own design

- Can every simulated fill be grouped by its pricing source and fallback reason?
- Are quote age, spread, and executable size checked before accepting a fill?

## Why this score for a trading system

3/5: directly useful execution-evidence fields, constrained by asset-specific options assumptions and unverified provider coverage.

**Scope of this review:** README, realism documentation, quote readiness and fill-source accounting code.
