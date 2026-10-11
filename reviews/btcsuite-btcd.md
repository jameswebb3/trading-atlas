# btcd — a reorg is a sequence of reversals and applications

**Decision question:** Can a derived on-chain dataset undo observations before applying a replacement branch?

| Field | Review |
| --- | --- |
| Upstream | [btcd](https://github.com/btcsuite/btcd) |
| Primary area | Market Data & Ingestion |
| Source commit | [b48125d0a3565b1441522ee10422f7815db03216](https://github.com/btcsuite/btcd/commit/b48125d0a3565b1441522ee10422f7815db03216) |
| Reviewed | 2026-09-27 |
| Declared license | [ISC](https://github.com/btcsuite/btcd/blob/b48125d0a3565b1441522ee10422f7815db03216/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Its reorg path provides a concrete undo-then-apply model. Downstream aggregates need reversible block identities and durable recovery because notifications do not atomically replace the consumer's own state. |

## Project overview

btcd is a Bitcoin full-node implementation in Go that validates and serves the blockchain. [Project documentation](https://github.com/btcsuite/btcd/blob/b48125d0a3565b1441522ee10422f7815db03216/README.md#L9-L14).

## Mechanism worth inspecting

The reorganization path verifies the proposed change, disconnects the old branch and then connects the replacement blocks. Connection and disconnection produce distinct notifications after releasing the chain lock around notification delivery. [Reorganization](https://github.com/btcsuite/btcd/blob/b48125d0a3565b1441522ee10422f7815db03216/blockchain/chain.go#L877-L961); [connected notification](https://github.com/btcsuite/btcd/blob/b48125d0a3565b1441522ee10422f7815db03216/blockchain/chain.go#L710-L714); [disconnected notification](https://github.com/btcsuite/btcd/blob/b48125d0a3565b1441522ee10422f7815db03216/blockchain/chain.go#L844-L848).

## Important limit

A consumer sees branch-transition events, not an automatically atomic replacement of its own derived tables. It must handle undo order, repeated delivery, crashes and reconciliation to the node's canonical tip. A block height alone cannot distinguish competing observations.

## Questions to take into your own design

- Are aggregates reversible by block hash before replacement events are applied?
- Can interruption after a disconnect recover from durable state without double-applying either branch?

## Why this score for a trading system

3/5: a clear canonical-state transition reference, while operating a second node or adapting consumers has substantial cost beyond the inspected pattern.

**Scope of this review:** Reorganization sequencing and notification boundary; no node execution or full consensus review.
