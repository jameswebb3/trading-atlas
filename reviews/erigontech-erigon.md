# Erigon — Can an incomplete node response masquerade as no on-chain activity

**Decision question:** Can an incomplete node response masquerade as no on-chain activity?

| Field | Review |
| --- | --- |
| Upstream | [Erigon](https://github.com/erigontech/erigon) |
| Primary area | Market Data & Ingestion |
| Source commit | [2427edfc96882af810e82d8d981e58d61c2e378e](https://github.com/erigontech/erigon/commit/2427edfc96882af810e82d8d981e58d61c2e378e) |
| Reviewed | 2026-09-26 |
| Declared license | [LGPL-3.0-or-later](https://github.com/erigontech/erigon/blob/2427edfc96882af810e82d8d981e58d61c2e378e/COPYING) |
| Review depth | 3/3: documentation, relevant implementation and tests read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | A strong on-chain ingestion reference for failing explicitly when evidence is missing. The inspected log path rejects unavailable headers, with a regression test that prevents an incomplete scan from looking like a valid result. |

## Project overview

Erigon is an Ethereum execution client with configurable retention of blocks and historical state. [Project documentation](https://github.com/erigontech/erigon/blob/2427edfc96882af810e82d8d981e58d61c2e378e/docs/site/versioned_docs/version-v3.4/fundamentals/prune-modes.md#L10-L26).

## Mechanism worth inspecting

The log scan rejects a missing block header instead of continuing with an incomplete result. A source test deletes a canonical header and expects getLogs to fail. [Missing-header gate](https://github.com/erigontech/erigon/blob/2427edfc96882af810e82d8d981e58d61c2e378e/rpc/jsonrpc/eth_receipts.go#L373-L380), [test read](https://github.com/erigontech/erigon/blob/2427edfc96882af810e82d8d981e58d61c2e378e/rpc/jsonrpc/eth_getlogs_missing_header_test.go#L46-L94).

## Important limit

Node retention differs by prune mode. The inspected rejection and test cover missing headers; they do not certify every RPC path or a collector's handling of errors, reorgs and retained history.

## Questions to take into your own design

- Can an incomplete node response masquerade as no on-chain activity?
- Does a missing header produce a visible failed batch rather than a zero-activity observation?

## Why this score for a trading system

4/5: direct completeness gate plus a concrete fault-injection test. Node configuration and other query paths still need separate coverage checks.

**Scope of this review:** Focused reading of the linked documentation and implementation plus cited tests (read, not executed). Other subsystems and runtime behavior were not assessed.
