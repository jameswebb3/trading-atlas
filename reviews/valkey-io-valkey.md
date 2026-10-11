# Valkey — Does reclaiming a pending stream message guarantee its payload still exists

**Decision question:** Does reclaiming a pending stream message guarantee its payload still exists?

| Field | Review |
| --- | --- |
| Upstream | [Valkey](https://github.com/valkey-io/valkey) |
| Primary area | Operations & Observability |
| Source commit | [dca022fa11e82b336a78b8e95b85c2f1d4a4ddc0](https://github.com/valkey-io/valkey/commit/dca022fa11e82b336a78b8e95b85c2f1d4a4ddc0) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/valkey-io/valkey/blob/dca022fa11e82b336a78b8e95b85c2f1d4a4ddc0/COPYING) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Separates reclaimable messages from pending IDs whose payloads have already disappeared. Useful when setting retention around recovery, with limited reason to add another data service solely for this pattern. |

## Project overview

A data-structure server supporting key/value workloads and native structures, forked from open-source Redis. [Project documentation](https://github.com/valkey-io/valkey/blob/dca022fa11e82b336a78b8e95b85c2f1d4a4ddc0/README.md#L4-L11).

## Mechanism worth inspecting

The XAUTOCLAIM implementation checks whether each pending entry still exists in the stream. Missing entries are removed from both pending lists and their IDs are collected for the response; existing entries can transfer ownership and increment delivery attempts. [Reclaim boundary](https://github.com/valkey-io/valkey/blob/dca022fa11e82b336a78b8e95b85c2f1d4a4ddc0/src/t_stream.c#L3538-L3599).

## Important limit

Cleaning up pending metadata does not recreate a deleted payload or prove its application effect completed. Retention must cover recovery requirements, and external actions still need a durable idempotency record.

## Questions to take into your own design

- Can retention delete a payload before its processing evidence is complete?
- Is a reclaimed message distinguished from a deleted, unrecoverable entry?

## Why this score for a trading system

2/5: a concrete retention caution, but an indirect fit for trading research unless a stream queue is already required.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
