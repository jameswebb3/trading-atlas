# Firehose Ethereum: data detail is part of the contract

**Decision question:** Does an on-chain feed actually contain the execution detail a feature assumes?

| Field | Review |
| --- | --- |
| Upstream | [Firehose Ethereum](https://github.com/streamingfast/firehose-ethereum) |
| Primary area | Market Data & Ingestion |
| Source commit | [9f69f928e4cbd3b65136dab61ba8ed7c8e976abc](https://github.com/streamingfast/firehose-ethereum/commit/9f69f928e4cbd3b65136dab61ba8ed7c8e976abc) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/streamingfast/firehose-ethereum/blob/9f69f928e4cbd3b65136dab61ba8ed7c8e976abc/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Makes data detail explicit through BASE and EXTENDED block representations. Useful when a feature needs internal execution evidence rather than just transactions and logs. |

## Project overview

Ethereum-compatible blockchain extraction and streaming stack. Its block model distinguishes RPC-derived headers, receipts, and logs from extended execution data produced through node instrumentation. [Project documentation](https://github.com/streamingfast/firehose-ethereum/blob/9f69f928e4cbd3b65136dab61ba8ed7c8e976abc/SUPPORTED-NETWORKS.md#L1-L19).

## Mechanism worth inspecting

[The network documentation](https://github.com/streamingfast/firehose-ethereum/blob/9f69f928e4cbd3b65136dab61ba8ed7c8e976abc/SUPPORTED-NETWORKS.md#L3-L19) separates instrumented-node extraction from standard RPC polling. [The block schema](https://github.com/streamingfast/firehose-ethereum/blob/9f69f928e4cbd3b65136dab61ba8ed7c8e976abc/proto/sf/ethereum/type/v2/type.proto#L9-L50) documents which detail level can supply execution traces and how within-block ordinals order successful execution elements. [Block helpers](https://github.com/streamingfast/firehose-ethereum/blob/9f69f928e4cbd3b65136dab61ba8ed7c8e976abc/types/pb/sf/ethereum/type/v2/type.go#L34-L57) expose hash, height, time, and parent identity separately.

[The log filter](https://github.com/streamingfast/firehose-ethereum/blob/9f69f928e4cbd3b65136dab61ba8ed7c8e976abc/transform/log_filter.go#L31-L85) validates that a filter specifies an address or event signature, then checks receipt logs for both conditions. That mechanism is a transaction-selection step. A useful feed contract also records acquisition mode and supported fields so an absent trace is not mistaken for a zero flow.

## Important limit

[The supported-network table](https://github.com/streamingfast/firehose-ethereum/blob/9f69f928e4cbd3b65136dab61ba8ed7c8e976abc/SUPPORTED-NETWORKS.md#L21-L41) records chain-specific start boundaries and the RPC fallback. The [schema](https://github.com/streamingfast/firehose-ethereum/blob/9f69f928e4cbd3b65136dab61ba8ed7c8e976abc/proto/sf/ethereum/type/v2/type.proto#L44-L70) warns that ordinals on reverted execution elements are unreliable and that some gas/fee effects survive failed transactions. Event selection alone does not distinguish swaps, routing, internal movement, or failed economic intent. Operating instrumented nodes and the wider streaming stack is a substantial infrastructure commitment; this review did not evaluate that deployment.

## Questions to take into your own design

- Does each dataset declare BASE versus EXTENDED coverage and unsupported historical ranges?
- Do failed calls, persistent fee effects, and successful transfers have distinct accounting rules?

## Why this score for a trading system

Execution-detail contracts are directly useful for on-chain trading features, but chain-specific instrumentation and downstream economic decoding make this a 3/5 reference rather than a general-purpose data solution.

**Scope of this review:** README, supported-network documentation, block schema and identity helpers, poller interface, and receipt-log filter; the wider Firehose core and production deployment were not inspected end to end.
