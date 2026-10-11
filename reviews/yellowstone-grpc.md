# Yellowstone gRPC: make the replay boundary part of the data contract

**Decision question:** Can a resumed Solana subscription prove that its requested history is still available?

| Field | Review |
| --- | --- |
| Upstream | [Yellowstone gRPC](https://github.com/rpcpool/yellowstone-grpc) |
| Primary area | Market Data & Ingestion |
| Source commit | [9fd6a582df9b5e89bc0ac7da0b4d71c1096f63ed](https://github.com/rpcpool/yellowstone-grpc/commit/9fd6a582df9b5e89bc0ac7da0b4d71c1096f63ed) |
| Reviewed | 2026-09-26 |
| Declared license | [AGPL-3.0 server; Apache-2.0 client/proto components](https://github.com/rpcpool/yellowstone-grpc/blob/9fd6a582df9b5e89bc0ac7da0b4d71c1096f63ed/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Streams Solana slots, transactions, account updates, and blocks with explicit commitment levels. Its replay path rejects requests older than retained history, while slow consumers are disconnected instead of receiving an apparently continuous stream. |

## Project overview

A Geyser-based gRPC plugin and client collection for streaming Solana data, with filters for accounts, transactions, blocks, and commitment level. [Project documentation](https://github.com/rpcpool/yellowstone-grpc/blob/9fd6a582df9b5e89bc0ac7da0b4d71c1096f63ed/README.md#L1-L11).

## Mechanism worth inspecting

The [subscription contract](https://github.com/rpcpool/yellowstone-grpc/blob/9fd6a582df9b5e89bc0ac7da0b4d71c1096f63ed/yellowstone-grpc-proto/proto/geyser.proto#L23-L51) carries commitment and an optional starting slot. The [replay handler](https://github.com/rpcpool/yellowstone-grpc/blob/9fd6a582df9b5e89bc0ac7da0b4d71c1096f63ed/yellowstone-grpc-geyser/src/grpc.rs#L1435-L1470) compares the request to the oldest replayable slot before producing retained messages. The [client path](https://github.com/rpcpool/yellowstone-grpc/blob/9fd6a582df9b5e89bc0ac7da0b4d71c1096f63ed/yellowstone-grpc-geyser/src/grpc.rs#L1585-L1616) reports unavailable history as an error, while [broadcast lag handling](https://github.com/rpcpool/yellowstone-grpc/blob/9fd6a582df9b5e89bc0ac7da0b4d71c1096f63ed/yellowstone-grpc-geyser/src/grpc.rs#L1659-L1686) terminates an overloaded stream.

## Important limit

Retention can be disabled. Replay is not an unlimited archive or proof of every slot's completeness. The [block-reconstruction documentation](https://github.com/rpcpool/yellowstone-grpc/blob/9fd6a582df9b5e89bc0ac7da0b4d71c1096f63ed/README.md#L332-L346) describes an error counter and configurable failure action. The [pre-execution stream](https://github.com/rpcpool/yellowstone-grpc/blob/9fd6a582df9b5e89bc0ac7da0b4d71c1096f63ed/README.md#L369-L376) intentionally lacks execution status, balances, and logs.

## Questions to take into your own design

- Does reconnect recovery refuse a cursor outside retained history?
- Are processed, confirmed, finalized, and pre-execution observations separate feature inputs?

## Why this score for a trading system

4/5: directly useful stream-recovery and commitment contracts, with explicit missing-history and consumer-lag failures. Validator configuration and reconstruction scope still matter.

**Scope of this review:** README streaming/reconstruction sections, subscription protobuf, replay and consumer-lag source paths; server and client licenses are distinct.
