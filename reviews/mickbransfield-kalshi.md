# Kalshi Data Scripts: Does a paginated market export prove a complete and valid historical dataset?

**Decision question:** Does a paginated market export prove a complete and valid historical dataset?

| Field | Review |
| --- | --- |
| Upstream | [mickbransfield/kalshi](https://github.com/mickbransfield/kalshi) |
| Primary area | Market Data & Ingestion |
| Source commit | [0bef695791309f8c6a84fef81bcf209723e36e46](https://github.com/mickbransfield/kalshi/commit/0bef695791309f8c6a84fef81bcf209723e36e46) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/mickbransfield/kalshi/blob/0bef695791309f8c6a84fef81bcf209723e36e46/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The v2 script requests pages until cursor equals an empty string, appending markets, trades, history or events. It writes CSV using the first row as a field template and names a current export with a local timestamp. The script is from an older Kalshi API era and no runtime behavior or current endpoint contract was verified. It lacks checks for HTTP status, duplicates, empty pages and completeness; open markets are a snapshot, not history. |

## What this project does

Loops through cursor pages and exports Kalshi markets and trades, but has no response-status or page-integrity checks; empty results are indexed and a missing cursor can repeat the request. Useful as a collector failure case, not a backfill reference.

## Mechanism inspected

The v2 script requests pages until cursor equals an empty string, appending markets, trades, history or events. It writes CSV using the first row as a field template and names a current export with a local timestamp.

## Limitation that matters

The script is from an older Kalshi API era and no runtime behavior or current endpoint contract was verified. It lacks checks for HTTP status, duplicates, empty pages and completeness; open markets are a snapshot, not history.

## Practical check for a trading system

For any Kalshi backfill, persist request window, cursor chain, page count and failures; never infer a complete history from a successful CSV write alone.

## Why this score

2/5 direct: it illustrates collector traps on a relevant venue, but it is old, unverified and missing the controls needed for trustworthy historical data.

## Source trail

[README.md](https://github.com/mickbransfield/kalshi/blob/0bef695791309f8c6a84fef81bcf209723e36e46/README.md#L1); [Kalshi_Public_API_v2.py](https://github.com/mickbransfield/kalshi/blob/0bef695791309f8c6a84fef81bcf209723e36e46/Kalshi_Public_API_v2.py#L30); [Kalshi_Public_API_v2.py](https://github.com/mickbransfield/kalshi/blob/0bef695791309f8c6a84fef81bcf209723e36e46/Kalshi_Public_API_v2.py#L52); [Kalshi_Public_API_v2.py](https://github.com/mickbransfield/kalshi/blob/0bef695791309f8c6a84fef81bcf209723e36e46/Kalshi_Public_API_v2.py#L65)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
