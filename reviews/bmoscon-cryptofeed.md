# Cryptofeed — How should a local book react to a missing update

**Decision question:** How should a local book react to a missing update?

| Field | Review |
| --- | --- |
| Upstream | [Cryptofeed](https://github.com/bmoscon/cryptofeed) |
| Primary area | Market Data & Ingestion |
| Source commit | [e831ea3317b74a44b6a33d9746cb02fa7fc62dd3](https://github.com/bmoscon/cryptofeed/commit/e831ea3317b74a44b6a33d9746cb02fa7fc62dd3) |
| Reviewed | 2026-09-26 |
| Declared license | [AGPL-3.0-or-later](https://github.com/bmoscon/cryptofeed/blob/e831ea3317b74a44b6a33d9746cb02fa7fc62dd3/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | A strong reference for exchange-feed normalization and book recovery. Its Binance sequence gate discards a broken local book; inspect each venue adapter before relying on the same continuity guarantee. |

## Project overview

Cryptofeed normalizes cryptocurrency trade, order-book and other feeds across exchanges, with callbacks for storage and replay. [Project documentation](https://github.com/bmoscon/cryptofeed/blob/e831ea3317b74a44b6a33d9746cb02fa7fc62dd3/README.md#L106-L136).

## Mechanism worth inspecting

The Binance adapter distinguishes obsolete deltas from updates that cover the next expected sequence. A gap drops the local book rather than extending a state it cannot justify. [Sequence gate](https://github.com/bmoscon/cryptofeed/blob/e831ea3317b74a44b6a33d9746cb02fa7fc62dd3/cryptofeed/exchanges/binance.py#L282-L301).

## Important limit

This is a venue-specific gate; it does not establish identical guarantees for every adapter. A rebuilt book also needs an explicit readiness signal before downstream decisions resume.

## Questions to take into your own design

- How should a local book react to a missing update?
- What exact snapshot and readiness event must follow a sequence gap?

## Why this score for a trading system

4/5: directly addresses a corrupt trading input with an explicit sequence gate. Adapter-specific evidence stops short of a universal feed-integrity claim.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
