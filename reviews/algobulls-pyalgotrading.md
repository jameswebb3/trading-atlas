# pyalgotrading — API-shaped stubs are not an executor

**Decision question:** Can a published order method be a no-op?

| Field | Review |
| --- | --- |
| Upstream | [pyalgotrading](https://github.com/algobulls/pyalgotrading) |
| Primary area | Execution & Exchange Integration |
| Source commit | [422003add749eae769cd0f8330a6af36ac15b6b1](https://github.com/algobulls/pyalgotrading/commit/422003add749eae769cd0f8330a6af36ac15b6b1) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/algobulls/pyalgotrading/blob/422003add749eae769cd0f8330a6af36ac15b6b1/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | The OrderBase methods for place, status, exit and cancel are explicitly documented as dummy signatures. A strategy written against these methods says nothing about live order behavior; actual order behavior resides in a hosted platform that is not visible in this stub. |

## What this project does

A Python interface to the AlgoBulls hosted trading platform. [README](https://github.com/algobulls/pyalgotrading/blob/422003add749eae769cd0f8330a6af36ac15b6b1/README.md).

## Mechanism inspected

The OrderBase methods for place, status, exit and cancel are explicitly documented as dummy signatures. [Implementation](https://github.com/algobulls/pyalgotrading/blob/422003add749eae769cd0f8330a6af36ac15b6b1/pyalgotrading/order/order_base.py#L1-L40).

## Limitation that matters

A strategy written against these methods says nothing about live order behavior; actual order behavior resides in a hosted platform that is not visible in this stub. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Reject it as an executor reference; require implementations and exchange-response fixtures before scoring an API.

## Why this score

Indirect relevance only: The OrderBase methods for place, status, exit and cancel are explicitly documented as dummy signatures. A strategy written against these methods says nothing about live order behavior; actual order behavior resides in a hosted platform that is not visible in this stub.

## Source trail

[README](https://github.com/algobulls/pyalgotrading/blob/422003add749eae769cd0f8330a6af36ac15b6b1/README.md) · [Documentation](https://github.com/algobulls/pyalgotrading/blob/422003add749eae769cd0f8330a6af36ac15b6b1/docs/index.md) · [Implementation](https://github.com/algobulls/pyalgotrading/blob/422003add749eae769cd0f8330a6af36ac15b6b1/pyalgotrading/order/order_base.py#L1-L40).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
