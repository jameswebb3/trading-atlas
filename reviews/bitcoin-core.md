# Bitcoin Core: distinguish notification loss from mempool event ordering

**Decision question:** Can a collector identify lost notifications without confusing them with mempool-state changes?

| Field | Review |
| --- | --- |
| Upstream | [Bitcoin Core](https://github.com/bitcoin/bitcoin) |
| Primary area | Market Data & Ingestion |
| Source commit | [ed7dd7cf4e1561a97edf72eba29a67b14e28c717](https://github.com/bitcoin/bitcoin/commit/ed7dd7cf4e1561a97edf72eba29a67b14e28c717) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/bitcoin/bitcoin/blob/ed7dd7cf4e1561a97edf72eba29a67b14e28c717/COPYING) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Provides canonical Bitcoin node data and read-only event notifications. Its ZeroMQ feed has separate transport and mempool sequence numbers, plus distinct block connect/disconnect and transaction add/remove events; recovery remains the collector's responsibility. |

## Project overview

Bitcoin Core provides node validation, a local chain database, RPC queries, and optional block/transaction notification feeds. [Project documentation](https://github.com/bitcoin/bitcoin/blob/ed7dd7cf4e1561a97edf72eba29a67b14e28c717/README.md#L1-L20).

## Mechanism worth inspecting

The [wire-format documentation](https://github.com/bitcoin/bitcoin/blob/ed7dd7cf4e1561a97edf72eba29a67b14e28c717/doc/zmq.md#L96-L152) separates the per-topic message counter from the mempool event sequence and identifies connect, disconnect, acceptance, and non-mining removal. The [publisher](https://github.com/bitcoin/bitcoin/blob/ed7dd7cf4e1561a97edf72eba29a67b14e28c717/src/zmq/zmqpublishnotifier.cpp#L193-L207) appends a memory-only counter to every successful send. [Event-specific encoding](https://github.com/bitcoin/bitcoin/blob/ed7dd7cf4e1561a97edf72eba29a67b14e28c717/src/zmq/zmqpublishnotifier.cpp#L254-L293) preserves the distinction between chain and mempool transitions.

## Important limit

[Raw transaction notifications](https://github.com/bitcoin/bitcoin/blob/ed7dd7cf4e1561a97edf72eba29a67b14e28c717/doc/zmq.md#L119-L131) can repeat on mempool admission and block inclusion. [Recovery notes](https://github.com/bitcoin/bitcoin/blob/ed7dd7cf4e1561a97edf72eba29a67b14e28c717/doc/zmq.md#L192-L208) explicitly assign gap recovery to the subscriber and distinguish transport counters from mempool ordering. A reconnected socket is not evidence that intervening history was received.

## Questions to take into your own design

- Is a transport-counter reset distinguishable from a missing-message gap?
- Can the collector reconcile an authoritative snapshot before resuming features after notification loss?

## Why this score for a trading system

4/5: authoritative, explicit event semantics directly support reliable Bitcoin data collection. The feed intentionally delegates replay and reconciliation to the consumer.

**Scope of this review:** README, complete relevant ZeroMQ protocol sections, event publisher, and MIT notice; no node or upstream example executed.
