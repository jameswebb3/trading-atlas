# CCXWS — What evidence can show that a reconstructed order book disagrees with its feed

**Decision question:** What evidence can show that a reconstructed order book disagrees with its feed?

| Field | Review |
| --- | --- |
| Upstream | [CCXWS](https://github.com/altangent/ccxws) |
| Primary area | Market Data & Ingestion |
| Source commit | [50ec03d4900ee9027a05678869ba05adb4d02fa3](https://github.com/altangent/ccxws/commit/50ec03d4900ee9027a05678869ba05adb4d02fa3) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/altangent/ccxws/blob/50ec03d4900ee9027a05678869ba05adb4d02fa3/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Preserves raw level strings and implements an exchange-specific checksum over the top of a reconstructed book. Useful for book-integrity diagnostics, provided mismatch detection and resnapshot policy are implemented separately. |

## Project overview

A JavaScript interface for cryptocurrency ticker, trade and order-book streams, with exchange-specific book implementations. [Project documentation](https://github.com/altangent/ccxws/blob/50ec03d4900ee9027a05678869ba05adb4d02fa3/README.md#L6-L12).

## Mechanism worth inspecting

The Kraken book preserves raw price and size strings beside numeric values, snapshots the best ten levels and derives a CRC checksum from exchange-specific decimal formatting. Existing price-level updates ignore timestamps that are not newer. [Raw representation](https://github.com/altangent/ccxws/blob/50ec03d4900ee9027a05678869ba05adb4d02fa3/src/orderbooks/KrakenOrderBook.ts#L83-L103); [update ordering](https://github.com/altangent/ccxws/blob/50ec03d4900ee9027a05678869ba05adb4d02fa3/src/orderbooks/KrakenOrderBook.ts#L124-L150); [checksum](https://github.com/altangent/ccxws/blob/50ec03d4900ee9027a05678869ba05adb4d02fa3/src/orderbooks/KrakenOrderBook.ts#L199-L206), [formatting](https://github.com/altangent/ccxws/blob/50ec03d4900ee9027a05678869ba05adb4d02fa3/src/orderbooks/KrakenOrderBook.ts#L234-L260).

## Important limit

A checksum method does not itself compare the result with the venue or trigger recovery. The class is described as a prototype; Kraken's checksum and ordering rules do not automatically apply to another exchange. [Prototype scope](https://github.com/altangent/ccxws/blob/50ec03d4900ee9027a05678869ba05adb4d02fa3/src/orderbooks/KrakenOrderBook.ts#L9-L12).

## Questions to take into your own design

- Can the reconstructed book be compared with independent feed evidence at the same update boundary?
- Does a mismatch invalidate the book until an authoritative snapshot restores it?

## Why this score for a trading system

4/5: directly inspectable book representation and checksum mechanics target a concrete market-data integrity risk.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
