# Prediction Markets MCP: Can market-movement evidence expose missing sources and publication times?

**Decision question:** Can market-movement evidence expose missing sources and publication times?

| Field | Review |
| --- | --- |
| Upstream | [JamesANZ/prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp) |
| Primary area | Research & Reproducibility |
| Source commit | [13f118b90902e06c8863d5445b75758e84ac1a95](https://github.com/JamesANZ/prediction-market-mcp/commit/13f118b90902e06c8863d5445b75758e84ac1a95) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/JamesANZ/prediction-market-mcp/blob/13f118b90902e06c8863d5445b75758e84ac1a95/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The envelope validates market movement evidence and represents each source as ok, empty, unavailable, auth required, rate limited, or error. Each evidence item carries publication and retrieval timestamps plus stale and truncated flags. Invalid envelopes are replaced with an empty partial result. The code explicitly disclaims causal explanation. A nullable publication time is honest but does not by itself prove when a trading system could have received the information. |

## What this project does

Returns a typed evidence envelope with source status, publication and retrieval times, and explicit partial or ambiguous outcomes. Useful as a model for provenance in research agents; it does not establish causality or data availability at a past trading decision.

## Mechanism inspected

The envelope validates market movement evidence and represents each source as ok, empty, unavailable, auth required, rate limited, or error. Each evidence item carries publication and retrieval timestamps plus stale and truncated flags. Invalid envelopes are replaced with an empty partial result.

## Limitation that matters

The code explicitly disclaims causal explanation. A nullable publication time is honest but does not by itself prove when a trading system could have received the information.

## Practical check for a trading system

For a historical claim, require a source status and publication timestamp, then compare the source's actual availability with the decision clock. Keep partial results distinct from a negative finding.

## Why this score

3/5 transferable: explicit failure and timing states would make research-agent evidence more auditable, but prediction-market movement search is not a Hyperliquid signal or a historical availability test.

## Source trail

[README.md](https://github.com/JamesANZ/prediction-market-mcp/blob/13f118b90902e06c8863d5445b75758e84ac1a95/README.md#L1); [src/evidence/envelope.ts](https://github.com/JamesANZ/prediction-market-mcp/blob/13f118b90902e06c8863d5445b75758e84ac1a95/src/evidence/envelope.ts#L37); [src/evidence/normalize.ts](https://github.com/JamesANZ/prediction-market-mcp/blob/13f118b90902e06c8863d5445b75758e84ac1a95/src/evidence/normalize.ts#L14)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
