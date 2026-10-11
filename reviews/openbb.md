# OpenBB: Provider adapters separate query, extraction, and normalization

**Decision question:** Where does provider-specific data become a comparable field?

| Field | Review |
| --- | --- |
| Upstream | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) |
| Primary area | Market Data & Ingestion |
| Source commit | [3e071fcc2cd9f891cac6040ae60296dba76dab46](https://github.com/OpenBB-finance/OpenBB/commit/3e071fcc2cd9f891cac6040ae60296dba76dab46) |
| Reviewed | 2026-09-25 |
| Declared license | [AGPL-3.0](https://github.com/OpenBB-finance/OpenBB/blob/3e071fcc2cd9f891cac6040ae60296dba76dab46/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Separates provider query translation, extraction, and normalization into explicit fetcher stages. The interface alone does not certify that a field was published before a decision or that two providers use identical timestamps. |

## Mechanism worth inspecting

The fetcher interface gives query translation, source extraction, and output transformation separate entry points. Its fetch path calls them in that order, so provider normalization can be reviewed without confusing it with transport. This is a useful boundary for feed adapters and provenance records.

**Source trail:** [project overview](https://github.com/OpenBB-finance/OpenBB/blob/3e071fcc2cd9f891cac6040ae60296dba76dab46/README.md) · [documentation](https://github.com/OpenBB-finance/OpenBB/blob/3e071fcc2cd9f891cac6040ae60296dba76dab46/openbb_platform/README.md#L1-L25) · [implementation](https://github.com/OpenBB-finance/OpenBB/blob/3e071fcc2cd9f891cac6040ae60296dba76dab46/openbb_platform/core/openbb_core/provider/abstract/fetcher.py#L42-L85).

## Important limit

The interface does not enforce event time, publication time, completeness, or source-specific field semantics. The repository is large and AGPL licensed; this is an architectural reference, not a lightweight component to adopt.

## Questions to take into your own design

- Can a normalized value be traced back to its provider request and raw response?
- Where is publication time checked before the value enters research?

## Why this score for a trading system

The provider adapter split is a useful data-ingestion pattern; it does not enforce decision-time availability and the AGPL license complicates reuse.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
