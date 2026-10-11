# HyperView — What observed evidence determines stop-versus-target order within a candle

**Decision question:** What observed evidence determines stop-versus-target order within a candle?

| Field | Review |
| --- | --- |
| Upstream | [HyperView](https://github.com/TreborNamor/TradingView-Machine-Learning-GUI) |
| Primary area | Backtesting & Simulation |
| Source commit | [04439529bab93a2b82a6777d3d0e6d28ffc1b19c](https://github.com/TreborNamor/TradingView-Machine-Learning-GUI/commit/04439529bab93a2b82a6777d3d0e6d28ffc1b19c) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/TreborNamor/TradingView-Machine-Learning-GUI/blob/04439529bab93a2b82a6777d3d0e6d28ffc1b19c/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Offers repeatable candle backtests and optimization. Its stop/target ordering follows an assumed OHLC path, so ambiguous-bar results need stress tests or finer data. |

## Project overview

CLI toolkit for TradingView data, Python strategy backtests and parameter optimization. [Project documentation](https://github.com/TreborNamor/TradingView-Machine-Learning-GUI/blob/04439529bab93a2b82a6777d3d0e6d28ffc1b19c/README.md#L5-L34).

## Mechanism worth inspecting

The bar-exit routine chooses open→high→low→close or open→low→high→close according to the nearer extreme, then selects the first threshold along that assumed path. [Exit routine](https://github.com/TreborNamor/TradingView-Machine-Learning-GUI/blob/04439529bab93a2b82a6777d3d0e6d28ffc1b19c/hyperview/backtest/engine.py#L360-L390), [workflow](https://github.com/TreborNamor/TradingView-Machine-Learning-GUI/blob/04439529bab93a2b82a6777d3d0e6d28ffc1b19c/README.md#L238-L243).

## Important limit

The chosen path is an approximation, not a recorded trade sequence. The shown close-position calculation compounds price returns without a fees term in that function; broader execution costs require separate verification. [Return calculation](https://github.com/TreborNamor/TradingView-Machine-Learning-GUI/blob/04439529bab93a2b82a6777d3d0e6d28ffc1b19c/hyperview/backtest/engine.py#L427-L440).

## Questions to take into your own design

- What observed evidence determines stop-versus-target order within a candle?
- How does the result change under the other possible intrabar threshold ordering?

## Why this score for a trading system

2/5: direct bar-replay code with clearly inspectable simplifications, insufficient evidence for execution-sensitive claims.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
