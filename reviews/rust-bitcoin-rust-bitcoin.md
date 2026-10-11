# rust-bitcoin — transaction identity has more than one hash

**Decision question:** Which transaction identifier does an on-chain dataset use?

| Field | Review |
| --- | --- |
| Upstream | [rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin) |
| Primary area | Market Data & Ingestion |
| Source commit | [86e4d5da015bcd41f8b995cb1f814105d462055a](https://github.com/rust-bitcoin/rust-bitcoin/commit/86e4d5da015bcd41f8b995cb1f814105d462055a) |
| Reviewed | 2026-09-27 |
| Declared license | [CC0-1.0](https://github.com/rust-bitcoin/rust-bitcoin/blob/86e4d5da015bcd41f8b995cb1f814105d462055a/LICENSE) |
| Review depth | 3/3: documentation, hash implementation and witness identity test read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Makes txid and witness transaction identity explicit, with a concrete fixture showing they can differ. Useful for reliable Bitcoin joins and deduplication; canonical inclusion still needs separate block evidence. |

## Project overview

rust-bitcoin provides Bitcoin data structures, serialization and protocol utilities, with distinct transaction identifier types. [Project documentation](https://github.com/rust-bitcoin/rust-bitcoin/blob/86e4d5da015bcd41f8b995cb1f814105d462055a/README.md#L6-L24).

## Mechanism worth inspecting

`compute_txid` hashes the transaction without SegWit data, while `compute_wtxid` includes the SegWit serialization when present. The inspected test checks a witness transaction with different values for the two IDs. [Hash implementation](https://github.com/rust-bitcoin/rust-bitcoin/blob/86e4d5da015bcd41f8b995cb1f814105d462055a/primitives/src/transaction.rs#L223-L244); [witness fixture](https://github.com/rust-bitcoin/rust-bitcoin/blob/86e4d5da015bcd41f8b995cb1f814105d462055a/bitcoin/src/blockdata/transaction.rs#L1236-L1243).

## Important limit

Both hashes identify transaction representations; neither proves canonical inclusion or confirmation depth. Using txid, wtxid or an application-derived ID interchangeably can break joins, deduplication and provenance. Include network and block identity where the observation depends on inclusion.

## Questions to take into your own design

- Are identifiers typed and named consistently across raw transactions, inputs, joins and features?
- Does a changed witness or reorg affect identity and observation provenance in the intended way?

## Why this score for a trading system

3/5: a precise Bitcoin identity reference with relevant source tests read, but transaction parsing does not establish canonical trading-data provenance.

**Scope of this review:** Transaction hash identities and one witness fixture; tests were read, not run; no full consensus audit.
