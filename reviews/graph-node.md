# Graph Node: historical state by block

**Decision question:** Does a historical entity query return the version valid at that block?

| Field | Review |
| --- | --- |
| Upstream | [Graph Node](https://github.com/graphprotocol/graph-node) |
| Primary area | Data Quality & Lineage |
| Source commit | [6838f4e3cf3607c5bc32ef705dd05aec1eb057ab](https://github.com/graphprotocol/graph-node/commit/6838f4e3cf3607c5bc32ef705dd05aec1eb057ab) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT OR Apache-2.0](https://github.com/graphprotocol/graph-node/blob/6838f4e3cf3607c5bc32ef705dd05aec1eb057ab/LICENSE-MIT) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Stores mutable entity versions over block ranges and filters historical queries by the requested block. Useful for reconstructing chain state without substituting today's entity value. |

## Project overview

Indexing service for blockchain subgraphs. It stores entity versions over block intervals and serves historical queries, making it useful for studying how derived blockchain state changes over time. [Project documentation](https://github.com/graphprotocol/graph-node/blob/6838f4e3cf3607c5bc32ef705dd05aec1eb057ab/docs/implementation/time-travel.md#L1-L35).

## Mechanism worth inspecting

The [historical-query design](https://github.com/graphprotocol/graph-node/blob/6838f4e3cf3607c5bc32ef705dd05aec1eb057ab/docs/implementation/time-travel.md#L14-L35) gives each mutable entity version a non-overlapping, half-open block range. The [query builder](https://github.com/graphprotocol/graph-node/blob/6838f4e3cf3607c5bc32ef705dd05aec1eb057ab/store/postgres/src/block_range.rs#L253-L299) emits a range-containment predicate for mutable entities and a block threshold for immutable ones. This puts the historical-state condition in the query path rather than relying on callers to avoid current values.

The [write/revert path](https://github.com/graphprotocol/graph-node/blob/6838f4e3cf3607c5bc32ef705dd05aec1eb057ab/store/postgres/src/writable.rs#L1498-L1513) forwards the rollback target together with the Firehose cursor. A useful adaptation is to version derived balances or classifications and make every historical query declare the version boundary it needs.

## Important limit

[The design notes](https://github.com/graphprotocol/graph-node/blob/6838f4e3cf3607c5bc32ef705dd05aec1eb057ab/docs/implementation/time-travel.md#L125-L133) explicitly distinguish block height from block hash. [Pruning](https://github.com/graphprotocol/graph-node/blob/6838f4e3cf3607c5bc32ef705dd05aec1eb057ab/docs/implementation/pruning.md#L1-L30) deletes entity versions and moves an exposed earliest-queryable block. Historical queries reconstruct the retained chain state; they do not establish when an indexer finished processing that state or when a consumer could first query it. Backtests need that second time axis too.

## Questions to take into your own design

- Can a historical query name both a block hash and the earliest retained version?
- Do research snapshots record indexing completion and receipt time separately from block time?

## Why this score for a trading system

The implemented historical-version predicate directly protects on-chain feature reconstruction from current-state substitution; retention and historical availability still need explicit consumer controls.

**Scope of this review:** Entity-version intervals, query predicates, write/revert dispatch, and pruning documentation; subgraph correctness, consensus verification, and operational performance were not evaluated.
