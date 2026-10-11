# On-chain data: from blocks to usable observations

On-chain data spans several jobs: extracting historical blocks, following the canonical chain, decoding events, and building economic metrics. These projects cover different parts of that path. A successful RPC request alone does not establish a complete, historically usable trading dataset.

## Reviewed projects by job

| Job | Project | What it offers | Main boundary |
| --- | --- | --- | --- |
| EVM application indexing | [Ponder](../reviews/ponder.md) | Event handlers, PostgreSQL tables, and a reversible database change log. | Recovery is bounded by retained history and configuration. |
| Historical entity state | [Graph Node](../reviews/graph-node.md) | Entity versions queried at a selected block. | Block validity and historical consumer availability are different time axes. |
| Blockchain ETL and archives | [Squid SDK](../reviews/squid-sdk.md) | Finalized/reversible block transactions and consecutive-height checks in a fills archive reader. | The inspected fills normalizer uses zero hashes and floating-point amounts. |
| Historical extraction | [cryo](../reviews/cryo.md) | Dataset/range partitions, columnar output, and separate work outcomes. | File-existence resume needs independent content and canonicality checks. |
| Ethereum exports | [Ethereum ETL](../reviews/ethereum-etl.md) | Blocks, transactions, logs, transfers, traces, and explicit entity ordering. | The stream's height checkpoint is separate from destination writes. |
| Bitcoin input accounting | [Bitcoin ETL](../reviews/bitcoin-etl.md) | Resolves transaction inputs against the outputs they spend. | Node indexing, fork handling, and entity-label vintages remain separate concerns. |
| Execution-detail extraction | [Firehose Ethereum](../reviews/firehose-ethereum.md) | Explicit BASE versus EXTENDED data representations. | A chain or acquisition path may not supply the detail a feature requires. |
| Reversible stream processing | [Substreams](../reviews/substreams.md) | SQL change history, transactional rollback cursors, and block-hash invalidation. | Guarantees depend on the selected sink mode and downstream handling. |
| Python RPC collection | [web3.py](../reviews/web3py.md) | Inclusive-range handling and adaptive event-scanner examples. | The example is not a durable application storage/recovery system. |
| Rust canonical log streams | [Alloy](../reviews/alloy.md) | Added/removed batches, empty-block progress, and bounded fork reconciliation. | The canonical buffer is in memory; the sink must persist and apply changes. |
| Protocol accounting | [DefiLlama TVL Adapters](../reviews/defillama-adapters.md) | Inspectable balance queries and explicit lending/exclusion rules. | Today's calculation recipe does not reproduce every historical metric vintage. |
| Normalized trade models | [Spellbook](../reviews/spellbook.md) | Raw trade evidence separated from metadata and price enrichment. | Temporal enrichment conditions and restrictive reuse terms need attention. |
| Prediction-market trade events | [Polymarket subgraph](../reviews/polymarket-polymarket-subgraph.md) | Chain-observed fills, amounts, fees and aggregate token volumes. | It does not reconstruct displayed CLOB depth or queue position; event-key uniqueness needs checking. |
| Bitcoin node notifications | [Bitcoin Core](../reviews/bitcoin-core.md) | Distinct notification sequences, transaction lifecycle messages, and gap-detection guidance. | Notifications do not provide durable replay; a consumer must reconcile gaps. |
| Mempool observations | [mempool](../reviews/mempool.md) | Snapshot synchronization, guarded arrival counting, and delayed removal of stale transactions. | Matching counts are not proof of identical transaction sets. |
| Ethereum node log feeds | [Geth](../reviews/go-ethereum.md) | Added and removed logs delivered to subscription consumers. | A downstream consumer must persist and apply reversals itself. |
| Address-index validation | [TrueBlocks Chifra](../reviews/trueblocks-chifra.md) | Explicit chunk continuity and deeper Bloom-membership checks. | A hash-string length check does not verify content integrity. |
| Solana execution streams | [Yellowstone gRPC](../reviews/yellowstone-grpc.md) | Commitment-aware streams and replay from a retained slot. | Replay retention is bounded; lag and too-old requests need explicit recovery. |
| Block explorer ingestion | [Blockscout](../reviews/blockscout.md) | Separate indexing consumers and an inspectable reorg-monitor path. | The reviewed height-only monitor misses equal-height changes; commercial reuse terms require review. |
| DeFi dimensional metrics | [DefiLlama Dimensions](../reviews/defillama-dimensions.md) | Separate flow and open-interest adapters with inspectable venue accounting conventions. | Snapshot fallback and skipped markets affect historical completeness. |
| Yield decomposition | [DefiLlama Yields](../reviews/defillama-yields.md) | Separates base and incentive yield and distinguishes receipt tokens from underlying assets. | Optional fields and fallback rules change what a displayed yield represents. |
| Ethereum RPC completeness | [Erigon](../reviews/erigontech-erigon.md) | Retention modes and a missing-header rejection with a regression test. | A node's retained range and the collector's error handling still determine usable coverage. |
| Ethereum query limits | [Nethermind](../reviews/nethermindeth-nethermind.md) | A bound on log-query work outside usable index coverage. | A rejected range is not an empty result; collectors need explicit splitting and coverage receipts. |
| Solana replay cursors | [LaserStream SDK](../reviews/helius-labs-laserstream-sdk.md) | Commitment-aware resume slots and a finite replay horizon. | Received slot progress is not a durable consumer acknowledgment. |
| AMM observation history | [Uniswap V3 Core](../reviews/uniswap-v3-core.md) | Bounded observation storage and rejection beyond usable historical coverage. | Allocated capacity, populated history and off-chain availability are distinct. |
| LP valuation units | [Curve StableSwap NG](../reviews/curvefi-stableswap-ng.md) | Explicit base-asset units and documented virtual-price dependencies. | LP oracle valuation is not an executable market quote; the root license is restrictive. |
| Lending share accounting | [Morpho Blue](../reviews/morpho-org-morpho-blue.md) | Separate upward and downward conversion rules with virtual assets and shares. | Empty-market conventions and unrealizable debt are model assumptions, not free precision. |
| RPC observation identity | [ethers.js](../reviews/ethers-io-ethers.js.md) | Inspectable sharing of identical low-level provider requests. | Repeated calls can reuse one observation; call count does not prove freshness or quorum. |
| EVM watcher checkpoints | [viem](../reviews/wevm-viem.md) | Filter fallback, range polling and an explicit in-memory block cursor. | Cursor advancement before callback delivery is not a durable consumer commit. |
| Bitcoin transaction identity | [rust-bitcoin](../reviews/rust-bitcoin-rust-bitcoin.md) | Distinct txid and witness transaction hashes, with a relevant source fixture. | Neither identifier alone proves canonical inclusion. |
| Bitcoin branch transitions | [btcd](../reviews/btcsuite-btcd.md) | Explicit old-branch disconnection followed by replacement connection. | Consumer tables and aggregates need their own reversible, durable state. |
| Bitcoin record framing | [python-bitcoinlib](../reviews/petertodd-python-bitcoinlib.md) | Default object decoding rejects unconsumed trailing bytes. | Buffer consumption is not consensus or inclusion validation. |
| ABI payload validation | [eth-abi](../reviews/ethereum-eth-abi.md) | Dynamic pointer, length and strict padding checks. | Decode success does not certify contract identity, ABI vintage or canonicality. |

Each linked review gives its inspected commit, implementation evidence, score, and scope. This is a comparison of observed designs; it is not a throughput benchmark or a recommendation to operate the whole stack.

## Six distinctions that change the dataset

### 1. Height is progress; hash is identity

A stream may reach height N while later discovering that its block at N belongs to a replaced chain. [Alloy's reconciler](../reviews/alloy.md) compares parent identity and emits removals before replacements. [Ponder](../reviews/ponder.md) uses recorded row changes to restore derived state.

A practical consumer contract names chain, block height, block hash where available, parent hash, and canonical status. When a source cannot supply identity, record that limitation explicitly instead of inventing a hash.

### 2. No events is different from no data

An empty block can be valid evidence of no matching events. An unread block is missing coverage. [Alloy's empty-batch fixture](../reviews/alloy.md) advances progress through blocks with no matching logs; [Squid SDK's archive reader](../reviews/squid-sdk.md) checks the next expected height.

For historical extracts, a coverage receipt should record requested ranges, returned ranges, successful empty blocks, failed ranges, and the source/query version. [cryo](../reviews/cryo.md) illustrates separate collection outcomes, with limits around skipped files.

### 3. Chain time is different from usable time

A block timestamp says when the chain places an event. It does not say when an archive object was published, an indexer finished its transformation, or a trading process received the result.

[Graph Node](../reviews/graph-node.md) reconstructs entity validity at a block. [Spellbook](../reviews/spellbook.md) shows that token metadata and prices can arrive through separate enrichment layers. A historical trading observation therefore needs a recorded availability policy and a retained data vintage as well as event time.

### 4. Normalization changes the evidence

Decimals, prices, contract classifications, and exclusion lists affect the final number. [Squid SDK](../reviews/squid-sdk.md) exposes decimal-to-float conversion; [DefiLlama](../reviews/defillama-adapters.md) exposes lending exclusions and price filtering; [Spellbook](../reviews/spellbook.md) separates raw amounts from enrichment.

Keep the raw observation alongside the normalized result. Version the calculation recipe and retain unresolved or unpriced components so a changing total can be explained.

### 5. Rewinding a cursor is different from restoring data

A corrected resume point does not undo an aggregate already computed from a fork. [Substreams' PostgreSQL path](../reviews/substreams.md) places rollback and cursor update in the same transaction. [Ethereum ETL](../reviews/ethereum-etl.md) illustrates the different failure boundary of export followed by a separate height-file write.

The downstream contract must describe how removals affect stored rows, aggregates, caches, and computations in flight. For external writes, explicit idempotent identities and recovery receipts are needed.


### 6. Oracle value is different from an executable quote

[Uniswap V3 Core](../reviews/uniswap-v3-core.md) exposes bounded accumulator history. [Curve's LP oracle](../reviews/curvefi-stableswap-ng.md) quotes in an underlying base asset and depends on virtual price, with explicit valuation limits. [Morpho Blue](../reviews/morpho-org-morpho-blue.md) separates asset/share conversions by rounding direction.

An observation should name its units, numeraire, source state and calculation version. Oracle, mark, accounting and executable prices may all be useful, but substituting one for another changes the claim being measured.


### 7. Settled events are not a live order book

The [Polymarket subgraph](../reviews/polymarket-polymarket-subgraph.md) maps chain-observed fill events into trade records and token aggregates. The inspected [fill mapping](https://github.com/Polymarket/polymarket-subgraph/blob/7a92ba026a9466c07381e0d245a323ba23ee8701/orderbook-subgraph/src/ExchangeMapping.ts#L24) records executed activity, not the displayed quotes or queue visible when an order would have arrived. Treat an indexed fill as settlement evidence; a backtest of executable quotes needs a separate point-in-time book feed and a coverage record.

## Practical reading order

- **Building an EVM event dataset:** Ponder → Alloy → Ethereum ETL.
- **Preparing a historical research extract:** cryo → Bitcoin ETL or Ethereum ETL → Graph Node.
- **Interpreting DeFi metrics:** DefiLlama TVL Adapters → DefiLlama Dimensions → DefiLlama Yields → Spellbook.
- **Designing a reversible sink:** Substreams → Ponder → Squid SDK.
- **Understanding available execution detail:** Firehose Ethereum → Yellowstone gRPC → LaserStream SDK.
- **Collecting Bitcoin observations:** Bitcoin Core → mempool → Bitcoin ETL → rust-bitcoin for transaction identity; btcd for branch transitions.
- **Checking an address index:** TrueBlocks Chifra.
- **Checking RPC completeness and workload bounds:** Erigon → Nethermind; ethers.js for request/observation identity.
- **Designing an EVM watcher sink:** viem → Substreams or Ponder for durable, reversible storage.
- **Separating settled prediction-market trades from executable quotes:** Polymarket subgraph → a separately captured, timestamped order-book feed.
- **Validating raw records:** python-bitcoinlib for complete buffer consumption; eth-abi for payload structure.
- **Interpreting protocol prices and monetary units:** Uniswap V3 Core → Curve StableSwap NG → Morpho Blue.

[← Back to the Atlas](../README.md) · [All Market Data & Ingestion reviews](../areas/market-data-ingestion.md) · [Data Quality & Lineage](../areas/data-quality-lineage.md)
