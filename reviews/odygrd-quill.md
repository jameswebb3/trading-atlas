# Quill - An asynchronous log buffer has explicit growth and loss behavior

**Decision question:** What happens when a logging consumer falls behind a trading process?

| Field | Review |
| --- | --- |
| Upstream | [odygrd/quill](https://github.com/odygrd/quill) |
| Primary area | Operations & Observability |
| Source commit | [78c0696c5be589488d882c280796dfa06bdcd492](https://github.com/odygrd/quill/commit/78c0696c5be589488d882c280796dfa06bdcd492) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its backend transit buffer grows when full and shrinks only after draining, while other queue modes explicitly choose dropping or blocking. A log queue can allocate, block or drop; none of these semantics alone provide durable order-event evidence. |

## What this project does

A C++ asynchronous logging library with configurable queue modes. The reviewed backend transit buffer grows when full and can shrink after it becomes empty.

## Mechanism inspected

The transit buffer doubles capacity on a full write, preserves circular order while moving stored events and defers shrinking until it is empty. Source tests read in this review exercise shrink and regrow behavior. The README separately documents bounded dropping and blocking queue modes with drop monitoring.

## Limitation that matters

A growing transit buffer can allocate and throw under pressure; a bounded dropping queue loses messages. Neither path is a durable event journal. The reviewed buffer is an internal logging mechanism, not evidence that order or fill events were persisted before acting. This is a source review, not a runtime or security test.

## Practical check for a trading system

Separate low-latency diagnostic logs from the durable order and fill ledger. For logs, choose and expose queue overflow behavior; for money-moving events, require acknowledged durable capture and replayable sequence numbers.

## Why this score

2/5 because queue pressure behavior is transferable to trading operations, but the inspected path is generic logging rather than a trading event ledger.

## Source trail

[README](https://github.com/odygrd/quill/blob/78c0696c5be589488d882c280796dfa06bdcd492/README.md#L266); [Buffer growth](https://github.com/odygrd/quill/blob/78c0696c5be589488d882c280796dfa06bdcd492/include/quill/backend/TransitEventBuffer.h#L82); [Shrink boundary](https://github.com/odygrd/quill/blob/78c0696c5be589488d882c280796dfa06bdcd492/include/quill/backend/TransitEventBuffer.h#L109); [Buffer test](https://github.com/odygrd/quill/blob/78c0696c5be589488d882c280796dfa06bdcd492/test/unit_tests/TransitEventBufferTest.cpp#L250); [License](https://github.com/odygrd/quill/blob/78c0696c5be589488d882c280796dfa06bdcd492/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
