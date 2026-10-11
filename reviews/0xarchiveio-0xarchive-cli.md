# 0xArchive CLI — Replay capability should be checked before connection

**Decision question:** Is the requested historical channel actually replayable?

| Field | Review |
| --- | --- |
| Upstream | [0xArchive CLI](https://github.com/0xArchiveIO/0xarchive-cli) |
| Primary area | Market Data & Ingestion |
| Source commit | [c36064211cb0c353858c50207e2137b0893836ab](https://github.com/0xArchiveIO/0xarchive-cli/commit/c36064211cb0c353858c50207e2137b0893836ab) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/0xArchiveIO/0xarchive-cli/blob/c36064211cb0c353858c50207e2137b0893836ab/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The replay command rejects unknown and live-only channels before opening a socket, then emits one JSON record per server message. A replay_stopped message exits with success in this path; consumers still need to distinguish natural completion from stop and verify coverage. |

## What this project does

A terminal client for the same commercial market-data API, exposing historical WebSocket replay. [README](https://github.com/0xArchiveIO/0xarchive-cli/blob/c36064211cb0c353858c50207e2137b0893836ab/README.md).

## Mechanism inspected

The replay command rejects unknown and live-only channels before opening a socket, then emits one JSON record per server message. [Implementation](https://github.com/0xArchiveIO/0xarchive-cli/blob/c36064211cb0c353858c50207e2137b0893836ab/src/commands/replay.ts#L88-L164).

## Limitation that matters

A replay_stopped message exits with success in this path; consumers still need to distinguish natural completion from stop and verify coverage. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Record replayability and completion reason in a local source contract; do not rely on a vendor command as a dataset guarantee.

## Why this score

Direct trading-system relevance: The replay command rejects unknown and live-only channels before opening a socket, then emits one JSON record per server message. A replay_stopped message exits with success in this path; consumers still need to distinguish natural completion from stop and verify coverage.

## Source trail

[README](https://github.com/0xArchiveIO/0xarchive-cli/blob/c36064211cb0c353858c50207e2137b0893836ab/README.md) · [Implementation](https://github.com/0xArchiveIO/0xarchive-cli/blob/c36064211cb0c353858c50207e2137b0893836ab/src/commands/replay.ts#L88-L164).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
