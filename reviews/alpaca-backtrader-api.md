# Alpaca Backtrader API: distinguish startup inventory from a new fill

**Decision question:** How does a broker adapter introduce pre-existing positions into a strategy?

| Field | Review |
| --- | --- |
| Upstream | [Alpaca Backtrader API](https://github.com/alpacahq/alpaca-backtrader-api) |
| Primary area | Execution & Exchange Integration |
| Source commit | [475bb54b8b16506092eb97df5a7cb1d05f0b86be](https://github.com/alpacahq/alpaca-backtrader-api/commit/475bb54b8b16506092eb97df5a7cb1d05f0b86be) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/alpacahq/alpaca-backtrader-api/blob/475bb54b8b16506092eb97df5a7cb1d05f0b86be/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Maps Alpaca positions and order events into Backtrader. It loads existing broker inventory at startup and emits simulated completed orders for that inventory, a useful example of why restart evidence must distinguish reconstructed positions from newly executed fills. |

## Project overview

An adapter connects Backtrader strategies with Alpaca REST and streaming interfaces. [Project documentation](https://github.com/alpacahq/alpaca-backtrader-api/blob/475bb54b8b16506092eb97df5a7cb1d05f0b86be/README.md#L8-L15).

## Mechanism worth inspecting

[Startup synchronization](https://github.com/alpacahq/alpaca-backtrader-api/blob/475bb54b8b16506092eb97df5a7cb1d05f0b86be/alpaca_backtrader_api/alpacabroker.py#L71-L103) reads existing positions. [data_started](https://github.com/alpacahq/alpaca-backtrader-api/blob/475bb54b8b16506092eb97df5a7cb1d05f0b86be/alpaca_backtrader_api/alpacabroker.py#L105-L138) emits simulated completed orders for them. Actual [fill handling](https://github.com/alpacahq/alpaca-backtrader-api/blob/475bb54b8b16506092eb97df5a7cb1d05f0b86be/alpaca_backtrader_api/alpacabroker.py#L243-L265) updates position size and distinguishes partial from complete orders.

## Important limit

The [order registry](https://github.com/alpacahq/alpaca-backtrader-api/blob/475bb54b8b16506092eb97df5a7cb1d05f0b86be/alpaca_backtrader_api/alpacabroker.py#L61-L65) is memory-resident, and the inspected fill callback does not establish persistent execution deduplication. [Paper/live documentation](https://github.com/alpacahq/alpaca-backtrader-api/blob/475bb54b8b16506092eb97df5a7cb1d05f0b86be/README.md#L89-L92) describes a live default; safe environment selection needs separate review.

## Questions to take into your own design

- Can reconstructed inventory ever be counted as a new execution in reports?
- Does restart reconcile both open orders and positions before resuming decisions?

## Why this score for a trading system

3/5: directly relevant restart and partial-fill adaptation source, with synthetic-event and persistence limits.

**Scope of this review:** README integration/paper-mode documentation, broker startup and fill source.
