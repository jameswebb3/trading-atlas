# MarketBridge - Does replay use the same decision function and event clock?

**Decision question:** Does replay use the same decision function and event clock?

| Field | Review |
| --- | --- |
| Upstream | [tianrking/MarketBridge](https://github.com/tianrking/MarketBridge) |
| Primary area | Research & Reproducibility |
| Source commit | [b47fd6debc5c8037175661dbb8c541e441b4a45e](https://github.com/tianrking/MarketBridge/commit/b47fd6debc5c8037175661dbb8c541e441b4a45e) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Replay rejects backwards receive time, requires source time and feeds book evidence to the research scan. The route explicitly filters spot books, so the result is not a perps execution result. |

## What this project does

A cross-venue market-data journal and research scanner.

## Mechanism inspected

Replay rejects backwards receive time, requires source time and feeds book evidence to the research scan.

## Limitation that matters

The route explicitly filters spot books, so the result is not a perps execution result.

## Practical check for a trading system

Use a deterministic decision function for live and replay, with separate fill validation.

## Why this score

3/5. Concrete clock and code-path parity, spot product scope.

## Source trail

[README](https://github.com/tianrking/MarketBridge/blob/b47fd6debc5c8037175661dbb8c541e441b4a45e/README.md#L1); [docs/README.md](https://github.com/tianrking/MarketBridge/blob/b47fd6debc5c8037175661dbb8c541e441b4a45e/docs/README.md#L1); [src/journal_replay.rs](https://github.com/tianrking/MarketBridge/blob/b47fd6debc5c8037175661dbb8c541e441b4a45e/src/journal_replay.rs#L43).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
