# Ethereum ETL: progress after export

**Decision question:** What does an ETL height checkpoint establish after a blockchain export?

| Field | Review |
| --- | --- |
| Upstream | [Ethereum ETL](https://github.com/blockchain-etl/ethereum-etl) |
| Primary area | Market Data & Ingestion |
| Source commit | [909650d64176fd26a0920fda8884ffc7e8307822](https://github.com/blockchain-etl/ethereum-etl/commit/909650d64176fd26a0920fda8884ffc7e8307822) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/blockchain-etl/ethereum-etl/blob/909650d64176fd26a0920fda8884ffc7e8307822/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Exports and enriches Ethereum entities, then advances the stream checkpoint after export returns. A compact reference for range-based ingestion and explicit entity ordering. |

## Project overview

Python ETL toolkit exporting Ethereum blocks, transactions, logs, token transfers, and traces to tabular formats. Its streaming path separates extraction, enrichment, ordered output, and progress tracking. [Project documentation](https://github.com/blockchain-etl/ethereum-etl/blob/909650d64176fd26a0920fda8884ffc7e8307822/README.md#L8-L12).

## Mechanism worth inspecting

The [stream command documentation](https://github.com/blockchain-etl/ethereum-etl/blob/909650d64176fd26a0920fda8884ffc7e8307822/docs/commands.md#L222-L227) describes the saved height and configurable lag. The [stream cycle](https://github.com/blockchain-etl/ethereum-etl/blob/909650d64176fd26a0920fda8884ffc7e8307822/blockchainetl/streaming/streamer.py#L88-L109) exports the next range before writing the last-synced height. [The Ethereum adapter](https://github.com/blockchain-etl/ethereum-etl/blob/909650d64176fd26a0920fda8884ffc7e8307822/ethereumetl/streaming/eth_streamer_adapter.py#L74-L103) enriches entities, sorts transactions and logs by their indices, assigns IDs and timestamps, and then exports them.

The useful design question is exactly what the checkpoint acknowledges. For a trading dataset, it should acknowledge a durable, identified range whose expected entities and empty blocks can be checked.

## Important limit

The inspected [progress writer](https://github.com/blockchain-etl/ethereum-etl/blob/909650d64176fd26a0920fda8884ffc7e8307822/blockchainetl/streaming/streamer.py#L119-L139) stores an integer in a separate file. A crash after export but before checkpoint persistence can replay rows; a height alone cannot detect a replaced block. [The lag documentation](https://github.com/blockchain-etl/ethereum-etl/blob/909650d64176fd26a0920fda8884ffc7e8307822/docs/commands.md#L225-L226) describes a probability reduction, while the cycle itself has no parent-hash reconciliation. [Token limitations](https://github.com/blockchain-etl/ethereum-etl/blob/909650d64176fd26a0920fda8884ffc7e8307822/docs/limitations.md#L3-L8) also document proxy detection and optional metadata gaps. Missing token metadata needs an explicit state rather than a fabricated decimal count.

## Questions to take into your own design

- Is the destination idempotent for replay after export succeeds but progress persistence fails?
- Does a completed range record canonical block hashes and unresolved metadata as well as its ending height?

## Why this score for a trading system

Range export, entity ordering, and checkpoint placement are direct ingestion references; hash reconciliation, durable acknowledgment, and metadata completeness remain consumer responsibilities.

**Scope of this review:** README, stream command reference, documented token limitations, stream loop, and adapter enrichment/export; cloud sinks and historical coverage were not evaluated.
