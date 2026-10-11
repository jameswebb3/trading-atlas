# Finance — Do signal timing and cash accounting survive a hand-calculated replay

**Decision question:** Do signal timing and cash accounting survive a hand-calculated replay?

| Field | Review |
| --- | --- |
| Upstream | [Finance](https://github.com/shashankvemuri/Finance) |
| Primary area | Backtesting & Simulation |
| Source commit | [20799035c34de202818afdefd13600d2594dbcd8](https://github.com/shashankvemuri/Finance/commit/20799035c34de202818afdefd13600d2594dbcd8) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/shashankvemuri/Finance/blob/20799035c34de202818afdefd13600d2594dbcd8/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and tests read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Makes next-open signal timing and cash reconciliation explicit, with hand-calculated tests. A useful bar-replay reference whose share-based accounting needs adaptation for derivatives. |

## Project overview

Python research toolkit covering market data, indicators, backtesting, portfolios and statistical models. [Project documentation](https://github.com/shashankvemuri/Finance/blob/20799035c34de202818afdefd13600d2594dbcd8/README.md#L3-L6).

## Mechanism worth inspecting

The backtester shifts close targets to the next open, records signal time beside fill time, and separately updates cash, shares and commission. Tests reconstruct short proceeds, costs and next-open fills by hand and compare prefix results. [Engine](https://github.com/shashankvemuri/Finance/blob/20799035c34de202818afdefd13600d2594dbcd8/src/finance/backtesting/engine.py#L112-L151), [tests](https://github.com/shashankvemuri/Finance/blob/20799035c34de202818afdefd13600d2594dbcd8/tests/test_backtesting.py#L14-L80).

## Important limit

The documented engine omits tick sequencing, impact, volume constraints and margin loans. Its share and borrow model is not perpetual-contract accounting. [Conventions](https://github.com/shashankvemuri/Finance/blob/20799035c34de202818afdefd13600d2594dbcd8/docs/methodology.md#L37-L61).

## Questions to take into your own design

- Do signal timing and cash accounting survive a hand-calculated replay?
- Can a hand-calculated fill and cash fixture verify signal-to-execution timing?

## Why this score for a trading system

4/5: direct replay and accounting mechanisms supported by relevant source tests, with explicitly simplified execution assumptions.

**Scope of this review:** Focused reading of the linked documentation and implementation plus cited tests (read, not executed). Other subsystems and runtime behavior were not assessed.
