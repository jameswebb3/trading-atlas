# Open Data Product Standard — Schema validity is a limited claim

**Decision question:** Does a schema-valid product have a usable operational contract?

| Field | Review |
| --- | --- |
| Upstream | [Open Data Product Standard](https://github.com/bitol-io/open-data-product-standard) |
| Primary area | Data Quality & Lineage |
| Source commit | [5f54a17296c3f294ea40c949a2a5ef268c20eb6b](https://github.com/bitol-io/open-data-product-standard/commit/5f54a17296c3f294ea40c949a2a5ef268c20eb6b) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/bitol-io/open-data-product-standard/blob/5f54a17296c3f294ea40c949a2a5ef268c20eb6b/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The inspected JSON schema requires apiVersion, kind and id at the top level. The documentation says its JSON schemas are companions, not authoritative definitions. |

## Project overview

Platform-neutral documentation and schema for describing data products and their ownership. [Documentation](https://github.com/bitol-io/open-data-product-standard/blob/5f54a17296c3f294ea40c949a2a5ef268c20eb6b/README.md).

## Mechanism worth inspecting

The inspected JSON schema requires apiVersion, kind and id at the top level. It describes version and status fields without making them equivalent to a complete release/admission policy. [Source](https://github.com/bitol-io/open-data-product-standard/blob/5f54a17296c3f294ea40c949a2a5ef268c20eb6b/schema/odps-json-schema-v1.1.0.json#L1-L55).

## Important limit

The documentation says its JSON schemas are companions, not authoritative definitions. Passing this schema does not prove freshness, availability, units or that a release was approved. [Evidence 1](https://github.com/bitol-io/open-data-product-standard/blob/5f54a17296c3f294ea40c949a2a5ef268c20eb6b/schema/odps-json-schema-v1.1.0.json#L1-L55). [Evidence 2](https://github.com/bitol-io/open-data-product-standard/blob/5f54a17296c3f294ea40c949a2a5ef268c20eb6b/docs/README.md#L29-L33).

## Questions to take into your own design

- Which operational fields must your own admission contract require?
- Are descriptive examples being mistaken for enforced states?

## Why this score for a trading system

Useful for identifying the boundary between documentation and enforcement; the broader standard is not necessary for a small trading-data catalog.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
