# HyperTrade - Can an order retry avoid doubling exposure after an ambiguous response?

**Decision question:** Can an order retry avoid doubling exposure after an ambiguous response?

| Field | Review |
| --- | --- |
| Upstream | [davassi/hypertrade](https://github.com/davassi/hypertrade) |
| Primary area | Execution & Exchange Integration |
| Source commit | [86ca5db5b2fe1ae1d35ec9e2ad3a83294ace7186](https://github.com/davassi/hypertrade/commit/86ca5db5b2fe1ae1d35ec9e2ad3a83294ace7186) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Queries a deterministic Hyperliquid client order ID before retrying an uncertain send. A timeout reclaim is safe only with a reliable venue lookup and later fill reconciliation. |

## What this project does

A Hyperliquid webhook execution service with persistent request reservations and deterministic client order IDs.

## Mechanism inspected

The webhook derives a stable cloid from the request nonce. On retry it queries the venue for that cloid; an inconclusive query raises instead of resubmitting. A SQLite reservation records in-progress and completed requests.

## Limitation that matters

Its in-progress reservation can be reclaimed after a timeout, so correctness still depends on the venue lookup and the stability of the nonce across senders. A returned order ID is not a completed-fill certificate. No root license file was verified.

## Practical check for a trading system

Keep an intent ID stable through request, retry and restart; require account-side order and fill checks before treating an ambiguous send as resolved.

## Why this score

4/5. This code directly addresses duplicate live orders under uncertain HTTP responses.

## Source trail

[README](https://github.com/davassi/hypertrade/blob/86ca5db5b2fe1ae1d35ec9e2ad3a83294ace7186/README.md#L19); [hypertrade/idempotency.py](https://github.com/davassi/hypertrade/blob/86ca5db5b2fe1ae1d35ec9e2ad3a83294ace7186/hypertrade/idempotency.py#L103); [hypertrade/routes/webhooks.py](https://github.com/davassi/hypertrade/blob/86ca5db5b2fe1ae1d35ec9e2ad3a83294ace7186/hypertrade/routes/webhooks.py#L45); [hypertrade/routes/webhooks.py](https://github.com/davassi/hypertrade/blob/86ca5db5b2fe1ae1d35ec9e2ad3a83294ace7186/hypertrade/routes/webhooks.py#L95).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
