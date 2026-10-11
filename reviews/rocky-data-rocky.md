# Rocky — Does a successful compile mean every declared data type was checked

**Decision question:** Does a successful compile mean every declared data type was checked?

| Field | Review |
| --- | --- |
| Upstream | [Rocky](https://github.com/rocky-data/rocky) |
| Primary area | Data Quality & Lineage |
| Source commit | [0ca6b07c62a3c5a8fde5793e92e0ef6600bf2ca1](https://github.com/rocky-data/rocky/commit/0ca6b07c62a3c5a8fde5793e92e0ef6600bf2ca1) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/rocky-data/rocky/blob/0ca6b07c62a3c5a8fde5793e92e0ef6600bf2ca1/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Checks SQL contracts before execution and reports unresolved types explicitly. A clean compile still needs a coverage check for declarations it could not validate. |

## Project overview

SQL compiler and change-review tooling that checks supported type, schema and contract problems before execution. [Project documentation](https://github.com/rocky-data/rocky/blob/0ca6b07c62a3c5a8fde5793e92e0ef6600bf2ca1/README.md#L14-L22).

## Mechanism worth inspecting

Contract validation reports absent required columns and mismatching resolved types. For an unknown inferred type it emits an informational diagnostic stating the declaration was not checked. [Contract model](https://github.com/rocky-data/rocky/blob/0ca6b07c62a3c5a8fde5793e92e0ef6600bf2ca1/engine/crates/rocky-compiler/src/contracts.rs#L123-L145), [unknown versus mismatch](https://github.com/rocky-data/rocky/blob/0ca6b07c62a3c5a8fde5793e92e0ef6600bf2ca1/engine/crates/rocky-compiler/src/contracts.rs#L165-L207).

## Important limit

An unknown type is informational, so successful compilation is not a universal validation certificate. The consumer-snapshot documentation also requires meaningful resolved schemas. [Snapshot requirement](https://github.com/rocky-data/rocky/blob/0ca6b07c62a3c5a8fde5793e92e0ef6600bf2ca1/docs/src/content/docs/concepts/cross-team-contracts.md#L46-L58).

## Questions to take into your own design

- Does a successful compile mean every declared data type was checked?
- Does an unresolved column type remain explicitly unchecked in the final verdict?

## Why this score for a trading system

3/5: transferable contract-coverage accounting with clear use for feature pipelines, rather than a trading-specific validator.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
