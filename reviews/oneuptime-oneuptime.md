# OneUptime - What happens when probe forwarding still fails after retries?

**Decision question:** What happens when probe forwarding still fails after retries?

| Field | Review |
| --- | --- |
| Upstream | [OneUptime/oneuptime](https://github.com/OneUptime/oneuptime) |
| Primary area | Operations & Observability |
| Source commit | [4591b5f1d866832c140df6693a127a7e9727aac3](https://github.com/OneUptime/oneuptime/commit/4591b5f1d866832c140df6693a127a7e9727aac3) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 for inspected path; enterprise directory separately licensed |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The probe retries failed forwarding with bounded exponential backoff. After the retry limit it logs and returns; this path does not provide a durable receipt or replay queue for a lost probe. |

## What this project does

An open-source monitoring platform with probe ingress forwarding.

## Mechanism inspected

The probe retries failed forwarding with bounded exponential backoff.

## Limitation that matters

After the retry limit it logs and returns; this path does not provide a durable receipt or replay queue for a lost probe.

## Practical check for a trading system

Treat exhausted forwarding as an explicit gap and retain the payload until acknowledged.

## Why this score

2/5. The retry loop is concrete, but silent loss after exhaustion limits its use as an evidence channel.

## Source trail

[README](https://github.com/OneUptime/oneuptime/blob/4591b5f1d866832c140df6693a127a7e9727aac3/README.md#L1); [packages/Probe/API/IncomingRequestIngress.ts](https://github.com/OneUptime/oneuptime/blob/4591b5f1d866832c140df6693a127a7e9727aac3/packages/Probe/API/IncomingRequestIngress.ts#L77); [packages/Probe/API/IncomingRequestIngress.ts](https://github.com/OneUptime/oneuptime/blob/4591b5f1d866832c140df6693a127a7e9727aac3/packages/Probe/API/IncomingRequestIngress.ts#L104).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
