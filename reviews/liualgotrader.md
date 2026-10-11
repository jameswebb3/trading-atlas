# LiuAlgoTrader: define whether fill quantities are deltas or totals

**Decision question:** Do streaming fills and polled order snapshots use the same quantity semantics?

| Field | Review |
| --- | --- |
| Upstream | [LiuAlgoTrader](https://github.com/amor71/LiuAlgoTrader) |
| Primary area | Execution & Exchange Integration |
| Source commit | [3df70067cf7a419115259956c64b50c5c07931db](https://github.com/amor71/LiuAlgoTrader/commit/3df70067cf7a419115259956c64b50c5c07931db) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/amor71/LiuAlgoTrader/blob/3df70067cf7a419115259956c64b50c5c07931db/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Routes broker events through a multiprocess trading framework. Its consumer adds fill quantities to positions, while the Alpaca adapter exposes both event quantities and filled-order totals, making delta-versus-cumulative semantics a concrete integration boundary to audit. |

## Project overview

A multiprocess trading platform supports equity and crypto strategies with broker and data adapters. [Project documentation](https://github.com/amor71/LiuAlgoTrader/blob/3df70067cf7a419115259956c64b50c5c07931db/README.md#L14-L24).

## Mechanism worth inspecting

The [architecture documentation](https://github.com/amor71/LiuAlgoTrader/blob/3df70067cf7a419115259956c64b50c5c07931db/docs/source/Concepts.rst#L65-L93) separates producers and consumers. The [consumer](https://github.com/amor71/LiuAlgoTrader/blob/3df70067cf7a419115259956c64b50c5c07931db/liualgotrader/consumer.py#L248-L311) adds filled_qty to positions and persists it. The [Alpaca order-status path](https://github.com/amor71/LiuAlgoTrader/blob/3df70067cf7a419115259956c64b50c5c07931db/liualgotrader/trading/alpaca.py#L94-L99) returns filled_qty, while its [event conversion](https://github.com/amor71/LiuAlgoTrader/blob/3df70067cf7a419115259956c64b50c5c07931db/liualgotrader/trading/alpaca.py#L570-L575) selects the event's qty.

## Important limit

[Terminal fill processing](https://github.com/amor71/LiuAlgoTrader/blob/3df70067cf7a419115259956c64b50c5c07931db/liualgotrader/consumer.py#L303-L314) reuses the additive partial-fill routine. Correctness therefore depends on callers supplying incremental quantities exactly once; the inspected functions do not establish persistent deduplication or normalization across every adapter.

## Questions to take into your own design

- Are event deltas and cumulative order quantities distinct fields?
- Does replaying the same execution leave positions and fees unchanged?

## Why this score for a trading system

3/5: directly useful source for inspecting broker quantity semantics, with unproven duplicate and polling/stream reconciliation guarantees.

**Scope of this review:** README, architecture documentation, consumer fill source, Alpaca quantity conversion.
