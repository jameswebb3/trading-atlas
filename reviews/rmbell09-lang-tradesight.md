# TradeSight — Which historical P&L is supported by broker evidence

**Decision question:** Which historical P&L is supported by broker evidence?

| Field | Review |
| --- | --- |
| Upstream | [TradeSight](https://github.com/rmbell09-lang/tradesight) |
| Primary area | Research & Reproducibility |
| Source commit | [8b2de128b5180d05e87a51a191685298e2e888e6](https://github.com/rmbell09-lang/tradesight/commit/8b2de128b5180d05e87a51a191685298e2e888e6) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT (declared in package metadata)](https://github.com/rmbell09-lang/tradesight/blob/8b2de128b5180d05e87a51a191685298e2e888e6/pyproject.toml#L10) |
| Review depth | 3/3: documentation, relevant implementation and tests read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Separates legacy P&L from broker-supported results and preserves the evidence behind each classification. Inspect the local-price fallback before treating that classification as fully verified accounting. |

## Project overview

Self-hosted strategy research and broker-backed paper trading with explicit accounting evidence and promotion gates. [Project documentation](https://github.com/rmbell09-lang/tradesight/blob/8b2de128b5180d05e87a51a191685298e2e888e6/README.md#L3-L15).

## Mechanism worth inspecting

An idempotent accounting epoch preserves old rows but excludes them from trusted performance. Later closed trades require broker order evidence, with a separate baseline-position path. Tests explicitly check legacy exclusion and two-fill confirmation. [Policy](https://github.com/rmbell09-lang/tradesight/blob/8b2de128b5180d05e87a51a191685298e2e888e6/src/trading/accounting_truth.py#L73-L128), [reconciliation](https://github.com/rmbell09-lang/tradesight/blob/8b2de128b5180d05e87a51a191685298e2e888e6/src/trading/accounting_truth.py#L333-L386), [tests](https://github.com/rmbell09-lang/tradesight/blob/8b2de128b5180d05e87a51a191685298e2e888e6/tests/test_accounting_truth.py#L54-L103).

## Important limit

Broker-confirmed status can still use local entry or exit prices when broker prices are absent. The P&L formula shown is quantity times price difference, not a complete fees/funding ledger. Its paper-readiness gates cannot activate live trading. [Fallback](https://github.com/rmbell09-lang/tradesight/blob/8b2de128b5180d05e87a51a191685298e2e888e6/src/trading/accounting_truth.py#L344-L361), [release boundary](https://github.com/rmbell09-lang/tradesight/blob/8b2de128b5180d05e87a51a191685298e2e888e6/docs/LIVE_READINESS.md#L3-L25).

## Questions to take into your own design

- Which historical P&L is supported by broker evidence?
- Do quantity, execution price, fees and funding each have their own evidence status?

## Why this score for a trading system

4/5: directly relevant trading-accounting evidence with readable tests; local-price fallback and incomplete cost accounting prevent a stronger score.

**Scope of this review:** Focused reading of the linked documentation and implementation plus cited tests (read, not executed). Other subsystems and runtime behavior were not assessed.
