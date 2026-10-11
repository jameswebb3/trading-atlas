# alpaca-mcp-server — Tool output can carry its own trust-boundary envelope

**Decision question:** How can an agent avoid treating broker API text as instructions?

| Field | Review |
| --- | --- |
| Upstream | [alpacahq/alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server) |
| Primary area | Agents & Decision Systems |
| Source commit | [a82ad1ccb740609abc99e10376e42d8e9c1037a1](https://github.com/alpacahq/alpaca-mcp-server/commit/a82ad1ccb740609abc99e10376e42d8e9c1037a1) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/alpacahq/alpaca-mcp-server/blob/a82ad1ccb740609abc99e10376e42d8e9c1037a1/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Middleware wraps tool results in server-authored trust metadata and a separate data field; external text receives a higher-risk label, while already wrapped responses are not wrapped twice. The envelope describes a boundary but cannot force a model to respect it; the project targets Alpaca assets, not HL perps. |

## What this project does

MCP server exposing Alpaca trading and market-data tools to assistants. [README](https://github.com/alpacahq/alpaca-mcp-server/blob/a82ad1ccb740609abc99e10376e42d8e9c1037a1/README.md).

## Mechanism inspected

Middleware wraps tool results in server-authored trust metadata and a separate data field; external text receives a higher-risk label, while already wrapped responses are not wrapped twice. [Implementation](https://github.com/alpacahq/alpaca-mcp-server/blob/a82ad1ccb740609abc99e10376e42d8e9c1037a1/src/alpaca_mcp_server/security.py#L18-L104).

## Limitation that matters

The envelope describes a boundary but cannot force a model to respect it; the project targets Alpaca assets, not HL perps. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Preserve source, risk class and raw payload separately in agent evidence; keep execution permissions outside generated text.

## Why this score

Middleware wraps tool results in server-authored trust metadata and a separate data field; external text receives a higher-risk label, while already wrapped responses are not wrapped twice. The envelope describes a boundary but cannot force a model to respect it; the project targets Alpaca assets, not HL perps.

## Source trail

[README](https://github.com/alpacahq/alpaca-mcp-server/blob/a82ad1ccb740609abc99e10376e42d8e9c1037a1/README.md) · [Implementation](https://github.com/alpacahq/alpaca-mcp-server/blob/a82ad1ccb740609abc99e10376e42d8e9c1037a1/src/alpaca_mcp_server/security.py#L18-L104) · [License](https://github.com/alpacahq/alpaca-mcp-server/blob/a82ad1ccb740609abc99e10376e42d8e9c1037a1/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
