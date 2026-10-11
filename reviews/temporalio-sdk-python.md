# Temporal Python SDK — Is an activity heartbeat a durable record of every processing step

**Decision question:** Is an activity heartbeat a durable record of every processing step?

| Field | Review |
| --- | --- |
| Upstream | [Temporal Python SDK](https://github.com/temporalio/sdk-python) |
| Primary area | Operations & Observability |
| Source commit | [eb642b14947bd8bcdf8816cffb6a63869803f5c6](https://github.com/temporalio/sdk-python/commit/eb642b14947bd8bcdf8816cffb6a63869803f5c6) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/temporalio/sdk-python/blob/eb642b14947bd8bcdf8816cffb6a63869803f5c6/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Coalesces heartbeat updates into the latest progress value. Useful for recovery checkpoints, while an evidence ledger must retain the intermediate events the heartbeat intentionally omits. |

## Project overview

A Python SDK for defining durable workflows and activities, with deterministic workflow replay and activity heartbeats. [Project documentation](https://github.com/temporalio/sdk-python/blob/eb642b14947bd8bcdf8816cffb6a63869803f5c6/README.md#L12-L38).

## Mechanism worth inspecting

The activity worker queues heartbeat details, drains the queue and sends only the latest available value to the bridge. A heartbeat-recording error can cancel an activity that is still running. [Heartbeat path](https://github.com/temporalio/sdk-python/blob/eb642b14947bd8bcdf8816cffb6a63869803f5c6/temporalio/worker/_activity.py#L221-L294). Workflow documentation separately requires deterministic workflow code. [Workflow rules](https://github.com/temporalio/sdk-python/blob/eb642b14947bd8bcdf8816cffb6a63869803f5c6/README.md#L729-L732).

## Important limit

A heartbeat is a progress checkpoint, not an append-only record of all intermediate events. It does not make a retried external trading action idempotent; action outcomes need their own durable identity and evidence.

## Questions to take into your own design

- Does the evidence ledger retain events omitted by heartbeat coalescing?
- Can a resumed activity repeat an external action without a new reconciliation step?

## Why this score for a trading system

3/5: a precise transferable separation between liveness/progress signals and durable decision evidence.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
