# Bitcoin ETL: resolving spent outputs

**Decision question:** Can a Bitcoin flow dataset trace input values back to their spent outputs?

| Field | Review |
| --- | --- |
| Upstream | [Bitcoin ETL](https://github.com/blockchain-etl/bitcoin-etl) |
| Primary area | Market Data & Ingestion |
| Source commit | [9d773d9cf9b297a45e82063e16a094c5b878ec4d](https://github.com/blockchain-etl/bitcoin-etl/commit/9d773d9cf9b297a45e82063e16a094c5b878ec4d) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/blockchain-etl/bitcoin-etl/blob/9d773d9cf9b297a45e82063e16a094c5b878ec4d/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Resolves transaction inputs against prior outputs and raises when a referenced transaction or output is unavailable. Useful for auditing the basis of Bitcoin flow accounting. |

## Project overview

Python toolkit exporting Bitcoin-family blocks and transactions. Its enrichment step resolves each transaction input to the referenced prior output, supplying the value and address fields needed for flow accounting. [Project documentation](https://github.com/blockchain-etl/bitcoin-etl/blob/9d773d9cf9b297a45e82063e16a094c5b878ec4d/README.md#L250-L273).

## Mechanism worth inspecting

The [schema and command reference](https://github.com/blockchain-etl/bitcoin-etl/blob/9d773d9cf9b297a45e82063e16a094c5b878ec4d/README.md#L114-L139) identify spent transaction hash, output index, and value. [The enrichment implementation](https://github.com/blockchain-etl/bitcoin-etl/blob/9d773d9cf9b297a45e82063e16a094c5b878ec4d/bitcoinetl/jobs/enrich_transactions.py#L56-L100) fetches referenced transactions once per distinct hash, resolves the output index, and copies its value, addresses, and script metadata. Missing transactions and out-of-range output indices raise instead of silently assigning zero.

[The streaming adapter](https://github.com/blockchain-etl/bitcoin-etl/blob/9d773d9cf9b297a45e82063e16a094c5b878ec4d/bitcoinetl/streaming/btc_streamer_adapter.py#L79-L103) also checks the enriched transaction count before export. The pattern worth preserving is input-level accounting evidence, not just an aggregate flow total.

## Important limit

[The command documentation](https://github.com/blockchain-etl/bitcoin-etl/blob/9d773d9cf9b297a45e82063e16a094c5b878ec4d/README.md#L262-L267) says un-enriched inputs lack these fields and requires `txindex=1` for enrichment. [Date-range documentation](https://github.com/blockchain-etl/bitcoin-etl/blob/9d773d9cf9b297a45e82063e16a094c5b878ec4d/README.md#L277-L285) warns that block times are not monotonic, so date selection can include out-of-day blocks. The [stream loop](https://github.com/blockchain-etl/bitcoin-etl/blob/9d773d9cf9b297a45e82063e16a094c5b878ec4d/blockchainetl/streaming/streamer.py#L88-L108) stores progress by height and lag without demonstrating fork rollback. None of these operations establishes when an address acquired an entity label.

## Questions to take into your own design

- Can each flow total be traced to spent transaction hash, output index, and original integer units?
- Are canonical order, block timestamp, receipt time, and entity-label vintage separate fields?

## Why this score for a trading system

Spent-output resolution directly supports auditable Bitcoin flow features; node prerequisites, height-only progress, and label availability constrain end-to-end use.

**Scope of this review:** Transaction schema and command reference, input enrichment, streaming cardinality check, and height progress; address clustering, entity labels, and node configuration were not evaluated.
