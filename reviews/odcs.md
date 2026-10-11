# ODCS: a data-quality rule must name its dimension and execution

**Decision question:** What does a data contract actually guarantee at decision time?

| Field | Review |
| --- | --- |
| Upstream | [Open Data Contract Standard](https://github.com/bitol-io/open-data-contract-standard) |
| Primary area | Data Quality & Lineage |
| Source commit | [d3e1cb3e69849e05c9a7522abed9b27fb9af50d7](https://github.com/bitol-io/open-data-contract-standard/commit/d3e1cb3e69849e05c9a7522abed9b27fb9af50d7) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/bitol-io/open-data-contract-standard/blob/d3e1cb3e69849e05c9a7522abed9b27fb9af50d7/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Defines structured quality checks with dimensions, severity, scheduling, and text, library, SQL, or custom execution forms. The JSON Schema validates the contract shape; it does not run the check or prove that a published value was available on time. |

## Mechanism worth inspecting

The [standard overview](https://github.com/bitol-io/open-data-contract-standard/blob/d3e1cb3e69849e05c9a7522abed9b27fb9af50d7/README.md#L23-L56) places schema and quality in a producer-consumer contract. The [quality guide](https://github.com/bitol-io/open-data-contract-standard/blob/d3e1cb3e69849e05c9a7522abed9b27fb9af50d7/docs/data-quality.md#L11-L43) separates human text, built-in metrics, SQL, and custom checks; its [scheduling example](https://github.com/bitol-io/open-data-contract-standard/blob/d3e1cb3e69849e05c9a7522abed9b27fb9af50d7/docs/data-quality.md#L262-L275) makes execution cadence explicit. The [v3.2 schema](https://github.com/bitol-io/open-data-contract-standard/blob/d3e1cb3e69849e05c9a7522abed9b27fb9af50d7/schema/odcs-json-schema-v3.2.0.json#L2762-L2828) constrains dimensions such as timeliness and coverage and records severity and scheduler fields.

## Important limit

The [guide explicitly describes text rules as potentially executable later](https://github.com/bitol-io/open-data-contract-standard/blob/d3e1cb3e69849e05c9a7522abed9b27fb9af50d7/docs/data-quality.md#L24-L33). A contract file cannot demonstrate actual check execution, missing-row detection, source publication time, or a passing result. The useful unit is contract plus run evidence.

## Questions to take into your own design

- Does every critical rule have an executable check and a last-run result?
- Are timeliness and coverage measured on the exact slice used for a decision?

## Why this score for a trading system

Its explicit quality dimensions and rule metadata transfer well to trading data contracts, while schema validity alone cannot certify observed data.

**Scope of this review:** We read the pinned overview, quality guide, and versioned JSON Schema. The schema is the executable specification inspected; we did not validate a contract.
