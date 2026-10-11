# feedhandler-core-rs: a visible gap is still an applied delta

**Decision question:** Does a counted L2 sequence gap stop downstream decisions from using the book?

| Field | Review |
| --- | --- |
| Upstream | [tfrmma/feedhandler-core-rs](https://github.com/tfrmma/feedhandler-core-rs) |
| Primary area | Market Data & Ingestion |
| Source commit | [104973e5c2380947d937fb6c7c1a100cdd5899a3](https://github.com/tfrmma/feedhandler-core-rs/commit/104973e5c2380947d937fb6c7c1a100cdd5899a3) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/tfrmma/feedhandler-core-rs/blob/104973e5c2380947d937fb6c7c1a100cdd5899a3/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Normalizes L2 ticks and records sequence anomalies, symbol mismatches, and update results alongside the book. A sequence gap increments a counter but the delta is still applied; consumers must impose their own invalidation and resync gate. |

## Mechanism worth inspecting

The [README's pipeline](https://github.com/tfrmma/feedhandler-core-rs/blob/104973e5c2380947d937fb6c7c1a100cdd5899a3/README.md#L3-L32) keeps exchange wire parsing outside the book core. A snapshot batch shares an ID; the book clears a side when the ID changes, with a nonzero sentinel to avoid confusing the first ID 0 with uninitialized state ([design note](https://github.com/tfrmma/feedhandler-core-rs/blob/104973e5c2380947d937fb6c7c1a100cdd5899a3/README.md#L91-L105), [implementation](https://github.com/tfrmma/feedhandler-core-rs/blob/104973e5c2380947d937fb6c7c1a100cdd5899a3/src/types.rs#L291-L312). The [apply path](https://github.com/tfrmma/feedhandler-core-rs/blob/104973e5c2380947d937fb6c7c1a100cdd5899a3/src/types.rs#L315-L362) rejects a tick for the wrong symbol and separately counts gaps or reorders.

## Important limit

The same apply path updates the book before tracking a sequence gap. It does not reject or invalidate that delta on a gap. The fast [batch drain](https://github.com/tfrmma/feedhandler-core-rs/blob/104973e5c2380947d937fb6c7c1a100cdd5899a3/src/book_engine.rs#L58-L67) also discards individual `DeltaResult` values, so a caller using it needs the counters and a separate validity policy. This is an observability mechanism, not a complete feed-recovery protocol.

## Questions to take into your own design

- Does a gap turn the derived book unavailable until a fresh snapshot?
- Can the consumer see symbol mismatch, gap, reorder, and ring drops separately?
- Does the fast path preserve enough evidence to explain the first bad update?

## Why this score for a trading system

L2 sequence gaps matter directly to book-driven trading, yet this implementation counts a gap while still applying the delta.

**Scope of this review:** We read the pinned README, book apply path, and engine batch loop. We did not run the crate, inspect every exchange adapter, or verify venue sequence semantics.
