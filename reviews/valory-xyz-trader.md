# trader - Can an agent classify a failed transaction before retrying?

**Decision question:** Can an agent classify a failed transaction before retrying?

| Field | Review |
| --- | --- |
| Upstream | [valory-xyz/trader](https://github.com/valory-xyz/trader) |
| Primary area | Agents & Decision Systems |
| Source commit | [030c55c0d6f7bb8d91a2c8467b6aa2901840e3c7](https://github.com/valory-xyz/trader/commit/030c55c0d6f7bb8d91a2c8467b6aa2901840e3c7) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The failed-transaction behaviour classifies submitter IDs and a nonce-taken exception before advancing a failure payload. The inspected branch classifies the failure; it does not prove whether an external wager settled. |

## What this project does

An autonomous prediction-market service built from coordinated agent behaviours.

## Mechanism inspected

The failed-transaction behaviour classifies submitter IDs and a nonce-taken exception before advancing a failure payload.

## Limitation that matters

The inspected branch classifies the failure; it does not prove whether an external wager settled.

## Practical check for a trading system

Tie retries to durable transaction evidence and retain an explicit unknown outcome.

## Why this score

2/5. Useful failure taxonomy, but account reconciliation remains necessary.

## Source trail

[README](https://github.com/valory-xyz/trader/blob/030c55c0d6f7bb8d91a2c8467b6aa2901840e3c7/README.md#L1); [packages/valory/skills/decision_maker_abci/behaviours/handle_failed_tx.py](https://github.com/valory-xyz/trader/blob/030c55c0d6f7bb8d91a2c8467b6aa2901840e3c7/packages/valory/skills/decision_maker_abci/behaviours/handle_failed_tx.py#L62); [Root license](https://github.com/valory-xyz/trader/blob/030c55c0d6f7bb8d91a2c8467b6aa2901840e3c7/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
