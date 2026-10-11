# Cross-Venue Arbitrage Decision Core - Can a rejected trade remain part of the evidence?

**Decision question:** Can a rejected trade remain part of the evidence?

| Field | Review |
| --- | --- |
| Upstream | [max0514/polymarket-bot](https://github.com/max0514/polymarket-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [c845e05384843cbc30edf811975c22390938b353](https://github.com/max0514/polymarket-bot/commit/c845e05384843cbc30edf811975c22390938b353) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Uses a replayable reducer and logs rejected opportunities with fee and risk reasons. Deterministic decisions do not establish synchronized books or achievable cross-venue fills. |

## What this project does

A Kalshi/Polymarket arbitrage decision core built around a pure state-event reducer and fee-aware pair evaluation.

## Mechanism inspected

One step(State, Event) seam receives book, fill, reject and health events. Pair evaluation records both accepted and rejected candidates with price-dependent fees and risk flags, preserving the denominator of the opportunity set.

## Limitation that matters

The README says live WebSocket book adapters are still open. The reducer can be replayed deterministically, but source reading does not show a validated live path, pair settlement equivalence or capturable two-leg fills.

## Practical check for a trading system

Persist every evaluated opportunity and rejection reason, then replay the same event stream through the decision function before discussing realized edge.

## Why this score

4/5 because The code makes decision evidence and negative outcomes inspectable; the capture and execution boundary remains unfinished.

## Source trail

[README](https://github.com/max0514/polymarket-bot/blob/c845e05384843cbc30edf811975c22390938b353/README.md#L3); [README](https://github.com/max0514/polymarket-bot/blob/c845e05384843cbc30edf811975c22390938b353/README.md#L109); [arb/reducer.py](https://github.com/max0514/polymarket-bot/blob/c845e05384843cbc30edf811975c22390938b353/arb/reducer.py#L43); [arb/evaluate.py](https://github.com/max0514/polymarket-bot/blob/c845e05384843cbc30edf811975c22390938b353/arb/evaluate.py#L25); [arb/pricing.py](https://github.com/max0514/polymarket-bot/blob/c845e05384843cbc30edf811975c22390938b353/arb/pricing.py#L96).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
