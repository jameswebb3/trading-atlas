# Jesse: Gap exits need a replay invariant

**Decision question:** Do step and fast backtests agree when price opens beyond a protective order?

| Field | Review |
| --- | --- |
| Upstream | [jesse-ai/jesse](https://github.com/jesse-ai/jesse) |
| Primary area | Backtesting & Simulation |
| Source commit | [b6d89c21386f2d6db7403bb06f1cfadf08e4fea2](https://github.com/jesse-ai/jesse/commit/b6d89c21386f2d6db7403bb06f1cfadf08e4fea2) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/jesse-ai/jesse/blob/b6d89c21386f2d6db7403bb06f1cfadf08e4fea2/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Tests stop and take-profit fills across price gaps in both step and fast replay modes. Agreement between two candle modes is a regression guard, not proof of an actual venue fill price. |

## Mechanism worth inspecting

A parametrized test creates discontinuous one-minute candles and runs the same scenario in step and fast modes. It asserts trade count, fees, PnL, timestamps, and exact exit prices across a stop gap and a later take-profit gap. The value is the concrete execution invariant and detailed trade fingerprint.

**Source trail:** [project overview](https://github.com/jesse-ai/jesse/blob/b6d89c21386f2d6db7403bb06f1cfadf08e4fea2/README.md) · [documentation](https://github.com/jesse-ai/jesse/blob/b6d89c21386f2d6db7403bb06f1cfadf08e4fea2/README.md#L1-L30) · [implementation](https://github.com/jesse-ai/jesse/blob/b6d89c21386f2d6db7403bb06f1cfadf08e4fea2/tests/test_price_gap_backtest.py#L225-L270) · [additional source](https://github.com/jesse-ai/jesse/blob/b6d89c21386f2d6db7403bb06f1cfadf08e4fea2/jesse/modes/backtest_mode.py#L531-L550).

## Important limit

The test compares two implementations against chosen candle outcomes. Candle OHLC cannot reveal all intrabar ordering or queue behavior, so the asserted fills remain model assumptions.

## Questions to take into your own design

- Do fast and slow replay produce identical order and trade receipts for gap cases?
- Are chosen gap fill prices labeled as assumptions?

## Why this score for a trading system

The step-versus-fast gap fixture checks trade prices, fees, and PnL across replay modes, though candle fills remain model assumptions.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
