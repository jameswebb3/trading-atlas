# Dukascopy Node: validate deltas before reconstructing ticks

**Decision question:** Can a tick decoder turn a malformed column into plausible prices?

| Field | Review |
| --- | --- |
| Upstream | [Dukascopy Node](https://github.com/Leo4815162342/dukascopy-node) |
| Primary area | Market Data & Ingestion |
| Source commit | [519a79017b49431c21049944934cce525f708ba5](https://github.com/Leo4815162342/dukascopy-node/commit/519a79017b49431c21049944934cce525f708ba5) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/Leo4815162342/dukascopy-node/blob/519a79017b49431c21049944934cce525f708ba5/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Reconstructs timestamps and bid/ask prices from deltas only after checking column lengths, finite values, nonnegative time increments, and a valid price multiplier. The pattern transfers to market-feed decoders; the data source and instruments are not Hyperliquid perpetuals. |

## Mechanism worth inspecting

The [tick-data example](https://github.com/Leo4815162342/dukascopy-node/blob/519a79017b49431c21049944934cce525f708ba5/examples/with-tick-data/README.md#L1-L6) distinguishes tick quotes from candles and shows a timestamped bid/ask output. The [normalizer](https://github.com/Leo4815162342/dukascopy-node/blob/519a79017b49431c21049944934cce525f708ba5/src/data-normaliser/index.ts#L5-L42) rejects inconsistent array lengths, non-finite values, invalid multiplier, and negative time deltas. It then [accumulates time and price deltas](https://github.com/Leo4815162342/dukascopy-node/blob/519a79017b49431c21049944934cce525f708ba5/src/data-normaliser/index.ts#L48-L80) into individual quotes. This is more precise than accepting a decoded array merely because its shape looks plausible.

## Important limit

These checks operate within a returned chunk. They do not prove no chunks were omitted, that the source timestamp is exchange-authoritative, or that quotes were available before a trading decision. The upstream example uses Dukascopy EURUSD, not a crypto venue.

## Questions to take into your own design

- Are compressed columns checked before cumulative reconstruction?
- Is continuity between chunks checked separately from validity within each chunk?

## Why this score for a trading system

The decoder provides a concrete transferable integrity check for compressed tick feeds, with limited direct applicability to Hyperliquid data.

**Scope of this review:** We read the pinned README, tick example, and normalizer source. We did not download or decode market data.
