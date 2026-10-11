# Price impact and fill capacity are separate backtest controls

**Decision question:** Does adding slippage also stop an order from exceeding available volume?

| Field | Review |
| --- | --- |
| Upstream | [QF-Lib](https://github.com/quarkfin/qf-lib) |
| Primary area | Backtesting & Simulation |
| Source commit | [dfbcffc6aba129c827cfe7caab85da864e70fece](https://github.com/quarkfin/qf-lib/commit/dfbcffc6aba129c827cfe7caab85da864e70fece) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/quarkfin/qf-lib/blob/dfbcffc6aba129c827cfe7caab85da864e70fece/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | QF-Lib's square-root impact model uses historical volatility and average daily volume to worsen fill prices. Volume-share checks are optional and absent when no limit is supplied. This is a useful separation: a cost model can price an oversized fill without making that fill feasible. |

## Mechanism worth inspecting

The [README](https://github.com/quarkfin/qf-lib/blob/dfbcffc6aba129c827cfe7caab85da864e70fece/README.md#L13-L23) describes an event-driven backtester. The [volume tutorial](https://github.com/quarkfin/qf-lib/blob/dfbcffc6aba129c827cfe7caab85da864e70fece/docs/source/tutorials/customize_your_backtest.rst#L302-L313) distinguishes fill limits from slippage. The [model contract](https://github.com/quarkfin/qf-lib/blob/dfbcffc6aba129c827cfe7caab85da864e70fece/qf_lib/backtesting/execution_handler/slippage/square_root_market_impact_slippage.py#L31-L54) makes volume checking optional; its [calculation](https://github.com/quarkfin/qf-lib/blob/dfbcffc6aba129c827cfe7caab85da864e70fece/qf_lib/backtesting/execution_handler/slippage/square_root_market_impact_slippage.py#L69-L91) uses data ending the previous day.

## Important limit

A daily-volume impact approximation is not order-book replay. Units, multiplier, price-impact calibration, missing/zero volume, and available execution liquidity need venue-specific checks. We did not run the model or calibrate it.

## Questions to take into your own design

- What rejects a fill that is too large even if its price penalty is calculated?
- Are the volume and volatility units appropriate for the traded contract?

## Why this score for a trading system

3/5: Separating cost and capacity is a directly useful execution-model pattern, but the daily impact approximation needs trading-specific calibration.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
