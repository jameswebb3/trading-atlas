# pydantic-jsonschema - Reject unresolved schema references before validation

**Decision question:** Does an imported data contract fail when a reference cannot be resolved?

| Field | Review |
| --- | --- |
| Upstream | [Danipulok/pydantic-jsonschema](https://github.com/Danipulok/pydantic-jsonschema) |
| Primary area | Data Quality & Lineage |
| Source commit | [00b196fafec5f2b2cf670853e783ab0a87841c53](https://github.com/Danipulok/pydantic-jsonschema/commit/00b196fafec5f2b2cf670853e783ab0a87841c53) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/Danipulok/pydantic-jsonschema/blob/00b196fafec5f2b2cf670853e783ab0a87841c53/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The reference resolver follows local $defs aliases and rejects external targets, circular chains and missing names with distinct SchemaReferenceError paths. The failure occurs during contract construction, before a consumer can treat a partial model as valid. It intentionally does not resolve external references. A valid JSON Schema shape still says nothing about exchange sequence, source publication time or whether a historical feature was available at decision time. |

## What this project does

This project converts JSON Schema definitions into Pydantic models, including local definitions and aliases. [README](https://github.com/Danipulok/pydantic-jsonschema/blob/00b196fafec5f2b2cf670853e783ab0a87841c53/README.md).

## Mechanism inspected

The reference resolver follows local $defs aliases and rejects external targets, circular chains and missing names with distinct SchemaReferenceError paths. The failure occurs during contract construction, before a consumer can treat a partial model as valid. [Implementation](https://github.com/Danipulok/pydantic-jsonschema/blob/00b196fafec5f2b2cf670853e783ab0a87841c53/pydantic_jsonschema/converters/_refs.py#L51-L110). [Related path](https://github.com/Danipulok/pydantic-jsonschema/blob/00b196fafec5f2b2cf670853e783ab0a87841c53/pydantic_jsonschema/converters/_converter.py#L96-L128).

## Limitation that matters

It intentionally does not resolve external references. A valid JSON Schema shape still says nothing about exchange sequence, source publication time or whether a historical feature was available at decision time. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

For a market-event contract, construct models with missing and cyclic references and require a hard failure; test event-time, receipt-time and sequence invariants separately.

## Why this score

A clear fail-closed boundary for schema composition is useful, but it is only one layer of a market-data contract.

## Source trail

[README](https://github.com/Danipulok/pydantic-jsonschema/blob/00b196fafec5f2b2cf670853e783ab0a87841c53/README.md) - [Implementation](https://github.com/Danipulok/pydantic-jsonschema/blob/00b196fafec5f2b2cf670853e783ab0a87841c53/pydantic_jsonschema/converters/_refs.py#L51-L110) - [Related path](https://github.com/Danipulok/pydantic-jsonschema/blob/00b196fafec5f2b2cf670853e783ab0a87841c53/pydantic_jsonschema/converters/_converter.py#L96-L128) - [License](https://github.com/Danipulok/pydantic-jsonschema/blob/00b196fafec5f2b2cf670853e783ab0a87841c53/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
