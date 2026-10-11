# A cancellation request needs a separately observed terminal state

**Decision question:** Does returning from cancel_order prove an order stopped trading?

| Field | Review |
| --- | --- |
| Upstream | [pylivetrader](https://github.com/alpacahq/pylivetrader) |
| Primary area | Execution & Exchange Integration |
| Source commit | [d32334dd496d29d50bab9f934bab3778e50bd653](https://github.com/alpacahq/pylivetrader/commit/d32334dd496d29d50bab9f934bab3778e50bd653) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/alpacahq/pylivetrader/blob/d32334dd496d29d50bab9f934bab3778e50bd653/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The Alpaca backend sends a cancellation request without returning a confirmed terminal state. Stream updates later remove filled, canceled, or rejected orders from the open cache. This separation is useful to inspect, especially because the cancellation helper catches errors and returns without a structured outcome. |

## Mechanism worth inspecting

The [overview](https://github.com/alpacahq/pylivetrader/blob/d32334dd496d29d50bab9f934bab3778e50bd653/README.md#L8-L11) presents a live Zipline-style interface; the [migration guide](https://github.com/alpacahq/pylivetrader/blob/d32334dd496d29d50bab9f934bab3778e50bd653/migration.md#L39-L43) records unsupported futures APIs. The [stream handler](https://github.com/alpacahq/pylivetrader/blob/d32334dd496d29d50bab9f934bab3778e50bd653/pylivetrader/backend/alpaca.py#L135-L159) updates open-order state from events, while [cancel_order](https://github.com/alpacahq/pylivetrader/blob/d32334dd496d29d50bab9f934bab3778e50bd653/pylivetrader/backend/alpaca.py#L439-L446) submits a request and catches failures.

## Important limit

A request-level return is not cancellation evidence. We did not establish restart reconciliation, missing stream recovery, or complete fill history. This is an Alpaca equities adapter, not a Hyperliquid connector.

## Questions to take into your own design

- How does the caller distinguish failed cancellation from an accepted request?
- Are fills arriving between cancel request and terminal confirmation included?

## Why this score for a trading system

3/5: The request-versus-terminal-state boundary is directly relevant to order safety, but exception signaling and recovery need additional design.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
