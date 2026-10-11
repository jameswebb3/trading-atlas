# Spellbook: raw trades and enrichment have different vintages

**Decision question:** Can a normalized on-chain trade table separate event evidence from later enrichment?

| Field | Review |
| --- | --- |
| Upstream | [Spellbook](https://github.com/duneanalytics/spellbook) |
| Primary area | Data Quality & Lineage |
| Source commit | [ec6589cac89872c4645ac89efdb19ebed2c4fab7](https://github.com/duneanalytics/spellbook/commit/ec6589cac89872c4645ac89efdb19ebed2c4fab7) |
| Reviewed | 2026-09-26 |
| Declared license | [BSL-1.1; additional-use restriction; scheduled GPL-3.0-or-later change](https://github.com/duneanalytics/spellbook/blob/ec6589cac89872c4645ac89efdb19ebed2c4fab7/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Separates base trade evidence from chain aggregation and metadata/price enrichment. A useful reference for event identity and versioned on-chain transformations. |

## Project overview

Dune's collection of SQL/dbt models for interpreting blockchain data. Its DEX models separate protocol-level trades, chain-level aggregation, and cross-chain enrichment, exposing how raw amounts become normalized and priced observations. [Project documentation](https://github.com/duneanalytics/spellbook/blob/ec6589cac89872c4645ac89efdb19ebed2c4fab7/README.md#L61-L76).

## Mechanism worth inspecting

[The sector design](https://github.com/duneanalytics/spellbook/blob/ec6589cac89872c4645ac89efdb19ebed2c4fab7/docs/general/sector_spell_design.md#L19-L46) keeps base evidence separate from enrichment and isolates chains before cross-chain union. [The DEX trade model](https://github.com/duneanalytics/spellbook/blob/ec6589cac89872c4645ac89efdb19ebed2c4fab7/dbt_subprojects/dex/models/trades/dex_trades.sql#L3-L48) declares a composite merge key and retains raw amounts, block time, transaction hash, event index, protocol version, and update metadata.

[The enrichment macro](https://github.com/duneanalytics/spellbook/blob/ec6589cac89872c4645ac89efdb19ebed2c4fab7/dbt_subprojects/dex/macros/models/enrich_dex_trades.sql#L29-L87) joins token metadata and prices after the base layer. This separation makes it possible to test raw event reconstruction independently of token decimals, symbols, or USD valuation. [The schema](https://github.com/duneanalytics/spellbook/blob/ec6589cac89872c4645ac89efdb19ebed2c4fab7/dbt_subprojects/dex/models/trades/_schema.yml#L25-L36) also documents the consumer identity `(blockchain, tx_hash, evt_index)`.

## Important limit

The inspected [metadata joins](https://github.com/duneanalytics/spellbook/blob/ec6589cac89872c4645ac89efdb19ebed2c4fab7/dbt_subprojects/dex/macros/models/enrich_dex_trades.sql#L55-L77) match chain and contract address without an as-of validity or publication predicate. Rebuilding a historical table can therefore apply the selected current enrichment vintage; block time alone does not establish availability. [The uniqueness check](https://github.com/duneanalytics/spellbook/blob/ec6589cac89872c4645ac89efdb19ebed2c4fab7/dbt_subprojects/dex/models/trades/_schema.yml#L25-L36) has warning severity and a recent three-day filter at this commit. [The license](https://github.com/duneanalytics/spellbook/blob/ec6589cac89872c4645ac89efdb19ebed2c4fab7/LICENSE#L8-L22) is Business Source License 1.1, restricts use for a Data or Analytics Platform, and names a future change date/license. This is a source-available design reference, not an unrestricted open-source dependency.

## Questions to take into your own design

- Are raw event amounts immutable while enriched decimals, labels, and prices are versioned separately?
- Does a consumer identity failure block publication across the whole research range?

## Why this score for a trading system

Explicit on-chain trade identity and raw/enriched separation directly support research data quality; the inspected temporal joins, limited uniqueness gate, and restrictive license cap its practical score at 3/5.

**Scope of this review:** README, sector design, DEX cross-chain model, enrichment macro, schema test declaration, and license; Dune runtime, all protocol decoders, and reported dataset completeness were not independently verified.
