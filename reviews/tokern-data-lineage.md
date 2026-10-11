# Tokern: reject ambiguous column provenance

**Decision question:** Can a SQL lineage extractor distinguish a resolved source from an ambiguous column?

| Field | Review |
| --- | --- |
| Upstream | [Tokern Data Lineage](https://github.com/tokern/data-lineage) |
| Primary area | Data Quality & Lineage |
| Source commit | [5945542742979fe350d313d906440c93ee3d0f36](https://github.com/tokern/data-lineage/commit/5945542742979fe350d313d906440c93ee3d0f36) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/tokern/data-lineage/blob/5945542742979fe350d313d906440c93ee3d0f36/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Extracts SQL column lineage by binding references against a catalog. The inspected binder rejects unknown and ambiguous columns instead of choosing an arbitrary match, making it a useful reference for explicit provenance failures. |

## Project overview

A SQL lineage engine supports catalog-backed column analysis and graph visualization. [Project documentation](https://github.com/tokern/data-lineage/blob/5945542742979fe350d313d906440c93ee3d0f36/README.md#L9-L25).

## Mechanism worth inspecting

The [binder](https://github.com/tokern/data-lineage/blob/5945542742979fe350d313d906440c93ee3d0f36/data_lineage/parser/binder.py#L156-L245) resolves table aliases and subqueries before binding output expressions. [Column resolution](https://github.com/tokern/data-lineage/blob/5945542742979fe350d313d906440c93ee3d0f36/data_lineage/parser/binder.py#L258-L302) raises for missing or multiple matches. The [graph representation](https://github.com/tokern/data-lineage/blob/5945542742979fe350d313d906440c93ee3d0f36/data_lineage/graph.py#L1-L32) stores directional dependencies.

## Important limit

An inspected [unqualified-star branch](https://github.com/tokern/data-lineage/blob/5945542742979fe350d313d906440c93ee3d0f36/data_lineage/parser/binder.py#L264-L269) assigns each alias's columns to the same list rather than accumulating them. The extraction needs regression fixtures for SQL constructs, and static dependencies alone do not prove runtime input versions. The README-linked external documentation was unavailable during this review.

## Questions to take into your own design

- Are ambiguous or unsupported expressions reported as unresolved lineage?
- Does each dependency also identify the immutable input version used by a run?

## Why this score for a trading system

3/5: explicit resolution failures are useful for data provenance; limited SQL coverage and the absence of runtime-version evidence constrain the score.

**Scope of this review:** README, API example documentation and catalog binding/graph source; external documentation endpoint unavailable.
