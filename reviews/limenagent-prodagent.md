# prodagent - An event stream can rebuild an agent run

**Decision question:** Can an interrupted research run be reconstructed from recorded facts?

| Field | Review |
| --- | --- |
| Upstream | [limenagent/prodagent](https://github.com/limenagent/prodagent) |
| Primary area | Research & Reproducibility |
| Source commit | [adaeaf6f1c8f6ca78e264ed17b55d089e2f1bd63](https://github.com/limenagent/prodagent/commit/adaeaf6f1c8f6ca78e264ed17b55d089e2f1bd63) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Defines run events and a pure state fold so agent state can be rebuilt and compared with recorded execution, including branching paths. The default log is memory-only and nested event payloads remain mutable; durable replay needs a storage and immutability contract. |

## What this project does

A compact agent-framework kernel with plans, schedulers, interrupts, artifacts and a run event log. The inspected mechanism folds state deltas from append-only run events.

## Mechanism inspected

Each Event carries a run-local sequence, run ID, kind and payload. apply_event folds STATE_DELTA events through channel reducers; fold_events reconstructs state from the initial value and the stream. Tests read in source compare replayed state with completed runs and exercise dynamic fan-out and branch choices.

## Limitation that matters

The default EventLog implementation is an in-process list, so it does not survive a crash. Event is a frozen dataclass but its data member is a mutable dictionary; immutability of nested payloads is not enforced here. The monotonic timestamp is suited to process-local duration, not a durable cross-process clock. This is a source review, not a runtime or security test.

## Practical check for a trading system

For a trading research agent, persist immutable event payloads before acting, assign durable sequence numbers and replay to a verified terminal state. Keep any live action behind a separate authorization gate.

## Why this score

3/5 because source and replay tests show a transferable run-evidence pattern, but the inspected default store does not provide crash durability.

## Source trail

[README](https://github.com/limenagent/prodagent/blob/adaeaf6f1c8f6ca78e264ed17b55d089e2f1bd63/README.md#L29); [Event and fold](https://github.com/limenagent/prodagent/blob/adaeaf6f1c8f6ca78e264ed17b55d089e2f1bd63/src/kernel/eventlog.py#L51); [In-memory store](https://github.com/limenagent/prodagent/blob/adaeaf6f1c8f6ca78e264ed17b55d089e2f1bd63/src/kernel/eventlog.py#L91); [Event-log tests](https://github.com/limenagent/prodagent/blob/adaeaf6f1c8f6ca78e264ed17b55d089e2f1bd63/tests/test_eventlog.py#L17); [Replay tests](https://github.com/limenagent/prodagent/blob/adaeaf6f1c8f6ca78e264ed17b55d089e2f1bd63/tests/test_replay.py#L19); [License](https://github.com/limenagent/prodagent/blob/adaeaf6f1c8f6ca78e264ed17b55d089e2f1bd63/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
