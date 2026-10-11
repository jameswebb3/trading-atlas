# Quantmod — Does adjusted history preserve what was known at the time

**Decision question:** Does adjusted history preserve what was known at the time?

| Field | Review |
| --- | --- |
| Upstream | [Quantmod](https://github.com/joshuaulrich/quantmod) |
| Primary area | Market Data & Ingestion |
| Source commit | [96eb06be53094d1ec89d798ca0fc65ebc46a0d57](https://github.com/joshuaulrich/quantmod/commit/96eb06be53094d1ec89d798ca0fc65ebc46a0d57) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-3.0](https://github.com/joshuaulrich/quantmod/blob/96eb06be53094d1ec89d798ca0fc65ebc46a0d57/DESCRIPTION) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A financial-data reference that makes OHLC adjustment mechanics visible. Keep raw prices, corporate-action records and adjustment versions separate when research needs the history available at a past decision time. |

## Project overview

Quantmod supports financial-data retrieval and model prototyping in R, including adjustment of OHLC prices for corporate actions. [Project documentation](https://github.com/joshuaulrich/quantmod/blob/96eb06be53094d1ec89d798ca0fc65ebc46a0d57/README.md#L1-L7).

## Mechanism worth inspecting

adjustOHLC retrieves split and dividend records or consumes an adjustment ratio, then transforms all four price columns while preserving volume. [Adjustment path](https://github.com/joshuaulrich/quantmod/blob/96eb06be53094d1ec89d798ca0fc65ebc46a0d57/R/adjustOHLC.R#L7-L40), [documented methods](https://github.com/joshuaulrich/quantmod/blob/96eb06be53094d1ec89d798ca0fc65ebc46a0d57/man/adjustOHLC.Rd#L26-L59).

## Important limit

The inspected adjustment API has no historical knowledge cutoff. A newly fetched corrected price series is not automatically a point-in-time dataset; price adjustment and contemporaneous tradability are separate questions.

## Questions to take into your own design

- Does adjusted history preserve what was known at the time?
- Can the raw prices and corporate-action vintage behind an adjusted series be recovered?

## Why this score for a trading system

3/5: direct data provenance and transformation semantics; equity corporate actions are relevant to data rigor, not a perpetual-trading signal.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
