# Prediction MCP: When does a paginated open-market response become a complete dataset?

**Decision question:** When does a paginated open-market response become a complete dataset?

| Field | Review |
| --- | --- |
| Upstream | [shaanmajid/prediction-mcp](https://github.com/shaanmajid/prediction-mcp) |
| Primary area | Market Data & Ingestion |
| Source commit | [880f8cdf2c271e97e7d2033a5fa006e8a0b9f9b4](https://github.com/shaanmajid/prediction-mcp/commit/880f8cdf2c271e97e7d2033a5fa006e8a0b9f9b4) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/shaanmajid/prediction-mcp/blob/880f8cdf2c271e97e7d2033a5fa006e8a0b9f9b4/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Kalshi client routes market, trade and event filters to the SDK and retries only rate-limit errors. Bulk methods page through cursor until empty, optionally selecting nested markets, with fixed delays between pages. No cycle detection or per-page count validation is visible in the bulk loops. Open-only event enumeration excludes closed and settled markets; pagination over a changing set is not a consistent snapshot. Cross-venue normalization does not establish comparable contract semantics. |

## What this project does

Unifies Kalshi and Polymarket queries and retries Kalshi 429 responses. Its all-events and all-markets loops collect open pages but do not guard repeated cursors, duplicate IDs or changing source membership; the output is a live snapshot, not historical completeness.

## Mechanism inspected

Kalshi client routes market, trade and event filters to the SDK and retries only rate-limit errors. Bulk methods page through cursor until empty, optionally selecting nested markets, with fixed delays between pages.

## Limitation that matters

No cycle detection or per-page count validation is visible in the bulk loops. Open-only event enumeration excludes closed and settled markets; pagination over a changing set is not a consistent snapshot. Cross-venue normalization does not establish comparable contract semantics.

## Practical check for a trading system

For a collector, retain status/window, cursor sequence, page hashes and source IDs, then reconcile totals and duplicates. A historical claim needs closed/settled coverage and source-time validation.

## Why this score

2/5 transferable: readable cursor and retry paths make a useful collector checklist, but it repeats known pagination patterns and does not establish complete market history.

## Source trail

[README.md](https://github.com/shaanmajid/prediction-mcp/blob/880f8cdf2c271e97e7d2033a5fa006e8a0b9f9b4/README.md#L1); [src/clients/kalshi.ts](https://github.com/shaanmajid/prediction-mcp/blob/880f8cdf2c271e97e7d2033a5fa006e8a0b9f9b4/src/clients/kalshi.ts#L46); [src/clients/kalshi.ts](https://github.com/shaanmajid/prediction-mcp/blob/880f8cdf2c271e97e7d2033a5fa006e8a0b9f9b4/src/clients/kalshi.ts#L104); [src/clients/kalshi.ts](https://github.com/shaanmajid/prediction-mcp/blob/880f8cdf2c271e97e7d2033a5fa006e8a0b9f9b4/src/clients/kalshi.ts#L219); [src/clients/kalshi.ts](https://github.com/shaanmajid/prediction-mcp/blob/880f8cdf2c271e97e7d2033a5fa006e8a0b9f9b4/src/clients/kalshi.ts#L262); [docs/getting-started.md](https://github.com/shaanmajid/prediction-mcp/blob/880f8cdf2c271e97e7d2033a5fa006e8a0b9f9b4/docs/getting-started.md#L1)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
