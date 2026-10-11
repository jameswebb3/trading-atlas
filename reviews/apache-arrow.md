# Apache Arrow — structural validity is one validation layer

**Decision question:** Which checks does a successful table validation actually certify?

| Field | Review |
| --- | --- |
| Upstream | [Apache Arrow](https://github.com/apache/arrow) |
| Primary area | Data Quality & Lineage |
| Source commit | [51955ecd2c0bb94b55c2130171386f8568fc2dbe](https://github.com/apache/arrow/commit/51955ecd2c0bb94b55c2130171386f8568fc2dbe) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/apache/arrow/blob/51955ecd2c0bb94b55c2130171386f8568fc2dbe/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Makes validation depth and cost explicit. Full structural validation is useful at data boundaries, but coverage, sequence continuity and point-in-time usability need separate market-data checks. |

## Project overview

Apache Arrow defines a columnar data format and tools for efficient interchange and analytics across languages. [Project documentation](https://github.com/apache/arrow/blob/51955ecd2c0bb94b55c2130171386f8568fc2dbe/README.md#L26-L38).

## Mechanism worth inspecting

`Table.validate` distinguishes cheap default validation from potentially O(n) full validation. The Python wrapper dispatches to `Validate` or `ValidateFull`, making the cost and checked depth explicit. [API and dispatch](https://github.com/apache/arrow/blob/51955ecd2c0bb94b55c2130171386f8568fc2dbe/python/pyarrow/table.pxi#L4220-L4242).

## Important limit

Even full structural validation is not a market-data contract: it does not certify timestamp availability, expected rows, monotonic sequences or economic units. A parser-valid table can therefore remain unusable for a trading decision. Make structural and domain validity separate recorded results.

## Questions to take into your own design

- Which boundaries require full structural checks, and what is their measured cost?
- Does the data manifest separately report coverage, ordering, units and usable-time checks?

## Why this score for a trading system

3/5: a useful layered-validation and cost-budget reference, with trading-domain semantics deliberately outside the columnar-format check.

**Scope of this review:** Table validation wrapper and documented depth/cost; native validation rules were not exhaustively audited.
