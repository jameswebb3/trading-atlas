# Stairlight: What can a lightweight SQL-lineage scanner reliably identify?

**Decision question:** What can a lightweight SQL-lineage scanner reliably identify?

| Field | Review |
| --- | --- |
| Upstream | [tosh2230/stairlight](https://github.com/tosh2230/stairlight) |
| Primary area | Data Quality & Lineage |
| Source commit | [95b2fe9c1a17e973ec57884274e98b36eaa817e0](https://github.com/tosh2230/stairlight/commit/95b2fe9c1a17e973ec57884274e98b36eaa817e0) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/tosh2230/stairlight/blob/95b2fe9c1a17e973ec57884274e98b36eaa817e0/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The query scanner strips line comments, identifies CTE aliases, extracts FROM and JOIN table tokens, and attaches a line number to each reference. It uses regex over SQL text and a substring line search; nested or dialect-specific SQL can be missed or misattributed. It does not prove column-level lineage or data availability. |

## What this project does

Extracts upstream tables from rendered SQL and maps them to the source line, but its regular expressions are a bounded heuristic. Useful for rough lineage discovery, not authoritative dependency or column provenance.

## Mechanism inspected

The query scanner strips line comments, identifies CTE aliases, extracts FROM and JOIN table tokens, and attaches a line number to each reference.

## Limitation that matters

It uses regex over SQL text and a substring line search; nested or dialect-specific SQL can be missed or misattributed. It does not prove column-level lineage or data availability.

## Practical check for a trading system

Use this style of scanner for an initial dependency inventory only. Mark unresolved SQL and require explicit lineage for trading-critical feature and report inputs.

## Why this score

2/5 adjacent: a cheap discovery technique could help map research SQL, but its heuristic coverage is too weak to certify trading data provenance.

## Source trail

[README.md](https://github.com/tosh2230/stairlight/blob/95b2fe9c1a17e973ec57884274e98b36eaa817e0/README.md#L1); [src/stairlight/query.py](https://github.com/tosh2230/stairlight/blob/95b2fe9c1a17e973ec57884274e98b36eaa817e0/src/stairlight/query.py#L35); [src/stairlight/query.py](https://github.com/tosh2230/stairlight/blob/95b2fe9c1a17e973ec57884274e98b36eaa817e0/src/stairlight/query.py#L70)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
