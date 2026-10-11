# PineForge — Can broker-state fingerprints locate the first replay divergence

**Decision question:** Can broker-state fingerprints locate the first replay divergence?

| Field | Review |
| --- | --- |
| Upstream | [PineForge](https://github.com/pineforge-4pass/pineforge-engine) |
| Primary area | Backtesting & Simulation |
| Source commit | [0d76a099cdd6a042601abf14a8f2beb50d5c8241](https://github.com/pineforge-4pass/pineforge-engine/commit/0d76a099cdd6a042601abf14a8f2beb50d5c8241) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0 (engine; separate compiler has different terms)](https://github.com/pineforge-4pass/pineforge-engine/blob/0d76a099cdd6a042601abf14a8f2beb50d5c8241/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and tests read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Records broker-state fingerprints across batch and streaming paths, with prefix-invariance tests. Useful for finding the first execution divergence rather than comparing only final P&L. |

## Project overview

C++ backtest and forward-execution engine with a separate Pine source-adapter runtime. [Project documentation](https://github.com/pineforge-4pass/pineforge-engine/blob/0d76a099cdd6a042601abf14a8f2beb50d5c8241/README.md#L25-L35).

## Mechanism worth inspecting

The broker hash folds execution continuation, position state, opening obligations, physical lots and finalized trade digests, then includes host-owned state. Tests read in this review check prefix invariance and recording through historical warm-up into streaming. [Hash projection](https://github.com/pineforge-4pass/pineforge-engine/blob/0d76a099cdd6a042601abf14a8f2beb50d5c8241/src/engine_state_hash.cpp#L22-L115), [tests](https://github.com/pineforge-4pass/pineforge-engine/blob/0d76a099cdd6a042601abf14a8f2beb50d5c8241/tests/test_live_state_hash_recording.cpp#L47-L87).

## Important limit

Coverage depends on which durable state is folded, including host extensions. The fill-model documentation says scheduling consolidation is incomplete; advertised TradingView parity is author-reported compatibility evidence, not live execution proof. [Boundary](https://github.com/pineforge-4pass/pineforge-engine/blob/0d76a099cdd6a042601abf14a8f2beb50d5c8241/docs/pages/fill-model.md#L3-L21), [host extension](https://github.com/pineforge-4pass/pineforge-engine/blob/0d76a099cdd6a042601abf14a8f2beb50d5c8241/src/engine_state_hash.cpp#L14-L19).

## Questions to take into your own design

- Can broker-state fingerprints locate the first replay divergence?
- Which pending orders, lots and host extensions affect continuation but are omitted from the hash?

## Why this score for a trading system

4/5: direct replay-state evidence with relevant tests; hash coverage and incomplete scheduler consolidation require further review.

**Scope of this review:** Focused reading of the linked documentation and implementation plus cited tests (read, not executed). Other subsystems and runtime behavior were not assessed.
