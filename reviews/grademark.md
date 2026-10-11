# Grademark: distinguish next-bar orders from ideal stop fills

**Decision question:** Does next-bar execution also make intrabar stops realistic?

| Field | Review |
| --- | --- |
| Upstream | [Grademark](https://github.com/Grademark/grademark) |
| Primary area | Backtesting & Simulation |
| Source commit | [dee7bb1a6fd27cf5c11e8116995ba359579d041e](https://github.com/Grademark/grademark/commit/dee7bb1a6fd27cf5c11e8116995ba359579d041e) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/Grademark/grademark/blob/dee7bb1a6fd27cf5c11e8116995ba359579d041e/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Provides a compact TypeScript backtesting state machine that defers ordinary entries and exits to the next bar. Its stop path fills exactly at the stop price when the bar crosses it, exposing a separate execution assumption that needs gap and slippage tests. |

## Project overview

A JavaScript and TypeScript toolkit supports strategy backtests and trade analysis. [Project documentation](https://github.com/Grademark/grademark/blob/dee7bb1a6fd27cf5c11e8116995ba359579d041e/README.md#L1-L11).

## Mechanism worth inspecting

[Order requests](https://github.com/Grademark/grademark/blob/dee7bb1a6fd27cf5c11e8116995ba359579d041e/src/lib/backtest.ts#L172-L186) enter pending states for the next bar. [Stop handling](https://github.com/Grademark/grademark/blob/dee7bb1a6fd27cf5c11e8116995ba359579d041e/src/lib/backtest.ts#L325-L342) tests bar extrema and closes at the configured stop, while [ordinary exits](https://github.com/Grademark/grademark/blob/dee7bb1a6fd27cf5c11e8116995ba359579d041e/src/lib/backtest.ts#L416-L419) use the next open.

## Important limit

The stop price may not be available after a gap, and OHLC bars cannot fully establish intrabar ordering. The [README](https://github.com/Grademark/grademark/blob/dee7bb1a6fd27cf5c11e8116995ba359579d041e/README.md#L74-L80) explicitly leaves fees, slippage, and sizing for later. The readable state machine is therefore an educational mechanism rather than a complete execution simulator.

## Questions to take into your own design

- What fill price applies if the market opens beyond the stop?
- Are costs and position size part of the same accounting model as the trade list?

## Why this score for a trading system

2/5: readable next-bar state transitions, with documented cost omissions and idealized stop fills.

**Scope of this review:** README usage and future-features sections, release notes, backtest state and stop source.
