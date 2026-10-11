# streamlens - Keep missing stream nodes visible

**Decision question:** Can a topology map show references to topics absent from broker metadata?

| Field | Review |
| --- | --- |
| Upstream | [muralibasani/streamlens](https://github.com/muralibasani/streamlens) |
| Primary area | Data Quality & Lineage |
| Source commit | [8b1cdd19ac120d9b0f81e80e7510ea05c13e4e64](https://github.com/muralibasani/streamlens/commit/8b1cdd19ac120d9b0f81e80e7510ea05c13e4e64) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/muralibasani/streamlens/blob/8b1cdd19ac120d9b0f81e80e7510ea05c13e4e64/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | It adds placeholder topic nodes for names referenced by producers or consumers but missing from the topic list, preserving a visible unresolved edge. Its top-level builder also turns a state-fetch exception into an empty state, so consumers must distinguish unreachable cluster from truly empty cluster. |

## What this project does

StreamLens builds a Kafka topology from topics, producers, consumers, stream processors, connectors, ACLs and schemas. [README](https://github.com/muralibasani/streamlens/blob/8b1cdd19ac120d9b0f81e80e7510ea05c13e4e64/README.md).

## Mechanism inspected

It adds placeholder topic nodes for names referenced by producers or consumers but missing from the topic list, preserving a visible unresolved edge. [Implementation](https://github.com/muralibasani/streamlens/blob/8b1cdd19ac120d9b0f81e80e7510ea05c13e4e64/server/src/topology.py#L65-L85).

## Limitation that matters

Its top-level builder also turns a state-fetch exception into an empty state, so consumers must distinguish unreachable cluster from truly empty cluster. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

In a data-flow map, show an unresolved producer/consumer reference and a separate fetch-health flag instead of silently dropping it.

## Why this score

It adds placeholder topic nodes for names referenced by producers or consumers but missing from the topic list, preserving a visible unresolved edge. Its top-level builder also turns a state-fetch exception into an empty state, so consumers must distinguish unreachable cluster from truly empty cluster.

## Source trail

[README](https://github.com/muralibasani/streamlens/blob/8b1cdd19ac120d9b0f81e80e7510ea05c13e4e64/README.md) - [Implementation](https://github.com/muralibasani/streamlens/blob/8b1cdd19ac120d9b0f81e80e7510ea05c13e4e64/server/src/topology.py#L65-L85) - [License](https://github.com/muralibasani/streamlens/blob/8b1cdd19ac120d9b0f81e80e7510ea05c13e4e64/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
