# Skyulf - Can an in-memory trial buffer stand in for a research ledger?

**Decision question:** Can an in-memory trial buffer stand in for a research ledger?

| Field | Review |
| --- | --- |
| Upstream | [flyingriverhorse/Skyulf](https://github.com/flyingriverhorse/Skyulf) |
| Primary area | Research & Reproducibility |
| Source commit | [8432a6bad06464ea72e6e69dae62f1f1d17008ae](https://github.com/flyingriverhorse/Skyulf/commit/8432a6bad06464ea72e6e69dae62f1f1d17008ae) |
| Reviewed | 2026-10-11 |
| Declared license | AGPL-3.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The buffer caps retained jobs and trials and evicts older entries with LRU behavior. Evicted trials are unavailable from this buffer, and process restart loses in-memory records. |

## What this project does

An agent research service with a real-time trial buffer.

## Mechanism inspected

The buffer caps retained jobs and trials and evicts older entries with LRU behavior.

## Limitation that matters

Evicted trials are unavailable from this buffer, and process restart loses in-memory records.

## Practical check for a trading system

Use buffers only for live display; persist every trial and rejection in a durable ledger.

## Why this score

1/5. This is mainly a negative example of why UI buffers cannot certify experiment history.

## Source trail

[README](https://github.com/flyingriverhorse/Skyulf/blob/8432a6bad06464ea72e6e69dae62f1f1d17008ae/README.md#L1); [backend/realtime/trial_buffer.py](https://github.com/flyingriverhorse/Skyulf/blob/8432a6bad06464ea72e6e69dae62f1f1d17008ae/backend/realtime/trial_buffer.py#L20); [backend/realtime/trial_buffer.py](https://github.com/flyingriverhorse/Skyulf/blob/8432a6bad06464ea72e6e69dae62f1f1d17008ae/backend/realtime/trial_buffer.py#L50).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
