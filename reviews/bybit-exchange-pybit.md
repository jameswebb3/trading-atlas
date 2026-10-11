# Pybit — Is a reconstructed snapshot evidence of uninterrupted book history

**Decision question:** Is a reconstructed snapshot evidence of uninterrupted book history?

| Field | Review |
| --- | --- |
| Upstream | [Pybit](https://github.com/bybit-exchange/pybit) |
| Primary area | Market Data & Ingestion |
| Source commit | [e6a557985396757830ee0ed031d3254abe398d0a](https://github.com/bybit-exchange/pybit/commit/e6a557985396757830ee0ed031d3254abe398d0a) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/bybit-exchange/pybit/blob/e6a557985396757830ee0ed031d3254abe398d0a/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A clear Python example of snapshot-plus-delta book reconstruction. Validate sequence continuity separately: the inspected handler updates sequence fields without checking for missing deltas. |

## Project overview

Pybit is Bybit's Python connector for REST and WebSocket data, with account and public-market subscriptions. [Project documentation](https://github.com/bybit-exchange/pybit/blob/e6a557985396757830ee0ed031d3254abe398d0a/examples/websocket_example_explanatory.py#L17-L50).

## Mechanism worth inspecting

The order-book handler replaces state on snapshots and applies delta inserts, updates and zero-size deletions. It writes the incoming update and sequence IDs into local state. [Book reconstruction](https://github.com/bybit-exchange/pybit/blob/e6a557985396757830ee0ed031d3254abe398d0a/pybit/_websocket_stream.py#L446-L483).

## Important limit

The inspected handler assigns sequence identifiers without a continuity check in this function. Its callback labels reconstructed data as a snapshot; that label alone does not certify a gap-free feed. [Callback](https://github.com/bybit-exchange/pybit/blob/e6a557985396757830ee0ed031d3254abe398d0a/pybit/_websocket_stream.py#L540-L547).

## Questions to take into your own design

- Is a reconstructed snapshot evidence of uninterrupted book history?
- Where is sequence continuity checked before a reconstructed book reaches consumers?

## Why this score for a trading system

3/5: directly useful book mechanics, with a specific integrity limitation that prevents treating normalization as validation.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
