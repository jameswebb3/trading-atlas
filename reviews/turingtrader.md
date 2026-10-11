# Bar-based order precedence is a model assumption, not a market fact

**Decision question:** How does a daily-bar simulator decide which stop or limit runs first?

| Field | Review |
| --- | --- |
| Upstream | [TuringTrader](https://github.com/fbertram/TuringTrader) |
| Primary area | Backtesting & Simulation |
| Source commit | [0a7dc60ed9df6f94920b13b6233cd0d0926f2528](https://github.com/fbertram/TuringTrader/commit/0a7dc60ed9df6f94920b13b6233cd0d0926f2528) |
| Reviewed | 2026-09-26 |
| Declared license | [AGPL-3.0](https://github.com/fbertram/TuringTrader/blob/0a7dc60ed9df6f94920b13b6233cd0d0926f2528/COPYING.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | TuringTrader orders processing by explicit type: close, next open, sell stops and limits, then buy stops and limits. It also converts pending next-open orders to last-bar close execution. Those choices make the simulation reproducible, but they cannot reconstruct the true intrabar sequence from OHLC alone. |

## Mechanism worth inspecting

The [README](https://github.com/fbertram/TuringTrader/blob/0a7dc60ed9df6f94920b13b6233cd0d0926f2528/README.md#L5-L15) identifies the backtesting engine. The [account interface](https://github.com/fbertram/TuringTrader/blob/0a7dc60ed9df6f94920b13b6233cd0d0926f2528/TuringTrader.Simulator/Simulator/v2/Core/IAccount.cs#L29-L58) defines order timing. The [processing loop](https://github.com/fbertram/TuringTrader/blob/0a7dc60ed9df6f94920b13b6233cd0d0926f2528/TuringTrader.Simulator/Simulator/v2/Core/Account_Default.cs#L116-L143) applies a fixed precedence and last-bar conversion, and notes that next-open NAV is an approximation for stops and limits.

## Important limit

Determinism is not execution realism. Daily highs and lows do not establish cross-asset simultaneity or whether a stop happened before a limit. Last-bar conversion can alter the intended order horizon.

## Questions to take into your own design

- How sensitive is the result to plausible alternative intrabar order sequences?
- Are terminal-bar fills reported as a distinct forced convention?

## Why this score for a trading system

3/5: Explicit order sequencing and terminal handling are useful direct references for auditing simulation assumptions, with unresolved OHLC ambiguity.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
