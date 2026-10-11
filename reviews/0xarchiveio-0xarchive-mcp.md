# 0xArchive MCP Server - Can a retired market-data connector make missing access unmistakable to an agent?

**Decision question:** Can a retired market-data connector make missing access unmistakable to an agent?

| Field | Review |
| --- | --- |
| Upstream | [0xArchiveIO/0xarchive-mcp](https://github.com/0xArchiveIO/0xarchive-mcp) |
| Primary area | Agents & Decision Systems |
| Source commit | [6de12211596f9589ed0efc600ff9037d543a4692](https://github.com/0xArchiveIO/0xarchive-mcp/commit/6de12211596f9589ed0efc600ff9037d543a4692) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | A shared registration helper declares tools read-only and idempotent, checks for an API client, and returns an explicit tool error if no key is present; SDK errors are converted to a tool response. The repository is retired and the useful data is supplied by an external hosted service with API-key and history-tier constraints. The wrapper is not a self-hosted market-data archive. |

## What this project does

A read-only MCP wrapper around the 0xArchive market-data SDK. The README marks this self-hosted package retired in favor of a hosted connector.

## Mechanism inspected

A shared registration helper declares tools read-only and idempotent, checks for an API client, and returns an explicit tool error if no key is present; SDK errors are converted to a tool response.

## Limitation that matters

The repository is retired and the useful data is supplied by an external hosted service with API-key and history-tier constraints. The wrapper is not a self-hosted market-data archive.

## Practical check for a trading system

For research agents, make entitlement, missing credentials and data-window limits first-class tool results; do not let a setup response masquerade as market evidence.

## Why this score

2/5. Its explicit tool-error boundary is transferable, but the retired wrapper and hosted-data dependency limit its value as a trading-system reference.

## Source trail

[README](https://github.com/0xArchiveIO/0xarchive-mcp/blob/6de12211596f9589ed0efc600ff9037d543a4692/README.md#L1); [src/index.ts](https://github.com/0xArchiveIO/0xarchive-mcp/blob/6de12211596f9589ed0efc600ff9037d543a4692/src/index.ts#L334); [src/index.ts](https://github.com/0xArchiveIO/0xarchive-mcp/blob/6de12211596f9589ed0efc600ff9037d543a4692/src/index.ts#L350); [README.md](https://github.com/0xArchiveIO/0xarchive-mcp/blob/6de12211596f9589ed0efc600ff9037d543a4692/README.md#L3); [src/index.ts](https://github.com/0xArchiveIO/0xarchive-mcp/blob/6de12211596f9589ed0efc600ff9037d543a4692/src/index.ts#L44); [Root license](https://github.com/0xArchiveIO/0xarchive-mcp/blob/6de12211596f9589ed0efc600ff9037d543a4692/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
