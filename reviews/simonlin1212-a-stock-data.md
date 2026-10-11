# A-Stock Data - Can shipped data-fetching code distinguish an empty result from source failure?

**Decision question:** Can shipped data-fetching code distinguish an empty result from source failure?

| Field | Review |
| --- | --- |
| Upstream | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) |
| Primary area | Data Quality & Lineage |
| Source commit | [8f6a6a53a59813bf5f010875f16f794fdc4f44f4](https://github.com/simonlin1212/a-stock-data/commit/8f6a6a53a59813bf5f010875f16f794fdc4f44f4) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The offline tests extract the exact Python blocks shipped in SKILL.md instead of testing a duplicate implementation. They verify provider and symbol validation, provenance fields, UTC fetched_at and malformed pagination totals; live network checks are opt-in. The sources are Chinese equity and futures feeds; their units, calendars and fallback hierarchy cannot be ported to crypto. These source tests do not establish the availability or accuracy of a Hyperliquid dataset. |

## What this project does

Tests execute the exact code shipped in its documentation and distinguish valid empty data from malformed source responses.

## Mechanism inspected

The offline tests extract the exact Python blocks shipped in SKILL.md instead of testing a duplicate implementation. They verify provider and symbol validation, provenance fields, UTC fetched_at and malformed pagination totals; live network checks are opt-in.

## Limitation that matters

The sources are Chinese equity and futures feeds; their units, calendars and fallback hierarchy cannot be ported to crypto. These source tests do not establish the availability or accuracy of a Hyperliquid dataset.

## Practical check for a trading system

Test the exact published collector path with fixture responses: zero rows, malformed totals, stale symbols and source errors must be distinct outcomes with provenance.

## Why this score

3/5. A concrete test pattern can prevent silent data-contract errors in trading research, although the markets and endpoints differ.

## Source trail

[README.md](https://github.com/simonlin1212/a-stock-data/blob/8f6a6a53a59813bf5f010875f16f794fdc4f44f4/README.md#L1); [SKILL.md](https://github.com/simonlin1212/a-stock-data/blob/8f6a6a53a59813bf5f010875f16f794fdc4f44f4/SKILL.md#L1); [tests/test_official_data.py](https://github.com/simonlin1212/a-stock-data/blob/8f6a6a53a59813bf5f010875f16f794fdc4f44f4/tests/test_official_data.py#L18); [tests/test_official_data.py](https://github.com/simonlin1212/a-stock-data/blob/8f6a6a53a59813bf5f010875f16f794fdc4f44f4/tests/test_official_data.py#L195); [tests/test_official_data.py](https://github.com/simonlin1212/a-stock-data/blob/8f6a6a53a59813bf5f010875f16f794fdc4f44f4/tests/test_official_data.py#L225); [LICENSE](https://github.com/simonlin1212/a-stock-data/blob/8f6a6a53a59813bf5f010875f16f794fdc4f44f4/LICENSE#L1)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
