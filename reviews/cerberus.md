# Schema validation may approve a normalized message instead of the raw one

**Decision question:** What does a successful validation say about the exchange payload received?

| Field | Review |
| --- | --- |
| Upstream | [Cerberus](https://github.com/pyeve/cerberus) |
| Primary area | Data Quality & Lineage |
| Source commit | [3c7809caaeaccf8ec192598e0156a76c4827f6b2](https://github.com/pyeve/cerberus/commit/3c7809caaeaccf8ec192598e0156a76c4827f6b2) |
| Reviewed | 2026-09-26 |
| Declared license | [ISC](https://github.com/pyeve/cerberus/blob/3c7809caaeaccf8ec192598e0156a76c4827f6b2/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Cerberus normalizes documents before validation by default, and update mode skips required-field checks. That is useful for configurable ingestion contracts, but a passing result must identify the mode and transformed document. Preserve raw payloads to avoid concealing missing or unexpected exchange fields. |

## Mechanism worth inspecting

The [README](https://github.com/pyeve/cerberus/blob/3c7809caaeaccf8ec192598e0156a76c4827f6b2/README.rst#L5-L20) describes extensible validation. The [normalization guide](https://github.com/pyeve/cerberus/blob/3c7809caaeaccf8ec192598e0156a76c4827f6b2/docs/normalization-rules.rst#L43-L68) documents optional removal of unknown fields and defaults. The [validator](https://github.com/pyeve/cerberus/blob/3c7809caaeaccf8ec192598e0156a76c4827f6b2/cerberus/validator.py#L1009-L1045) normalizes by default and checks required fields only outside update mode.

## Important limit

A schema gate does not establish message chronology, uniqueness, or completeness of a stream. A normalized value is not proof the source sent the same value; record transformations and validation configuration.

## Questions to take into your own design

- Can an accepted record be traced back to the exact raw payload?
- Could update mode or defaults mask a field that is mandatory for this message type?

## Why this score for a trading system

3/5: Explicit raw-versus-normalized contracts transfer well to trading ingestion, with the validation modes and scope clearly bounded.

**Scope of this review:** We read the pinned overview, linked documentation, and the cited implementation. No upstream code was executed.
