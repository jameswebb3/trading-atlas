# OpenLIT - Does an offline-labelled evaluation still depend on a service?

**Decision question:** Does an offline-labelled evaluation still depend on a service?

| Field | Review |
| --- | --- |
| Upstream | [openlit/openlit](https://github.com/openlit/openlit) |
| Primary area | Operations & Observability |
| Source commit | [066e2c582c7e0365437f1eeda65ece4c4360ff58](https://github.com/openlit/openlit/commit/066e2c582c7e0365437f1eeda65ece4c4360ff58) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The offline evaluation helper builds a request with run ID, metadata and threshold, then posts it to an API. This path needs a service URL and key despite the offline name; it does not provide standalone evidence retention. |

## What this project does

An LLM observability system with evaluation submission.

## Mechanism inspected

The offline evaluation helper builds a request with run ID, metadata and threshold, then posts it to an API.

## Limitation that matters

This path needs a service URL and key despite the offline name; it does not provide standalone evidence retention.

## Practical check for a trading system

Keep local evaluation inputs and outputs before optional observability upload.

## Why this score

2/5. The run metadata is useful, while the service dependency limits direct adoption.

## Source trail

[README](https://github.com/openlit/openlit/blob/066e2c582c7e0365437f1eeda65ece4c4360ff58/README.md#L1); [sdk/python/src/openlit/evals/offline.py](https://github.com/openlit/openlit/blob/066e2c582c7e0365437f1eeda65ece4c4360ff58/sdk/python/src/openlit/evals/offline.py#L130); [sdk/python/src/openlit/evals/offline.py](https://github.com/openlit/openlit/blob/066e2c582c7e0365437f1eeda65ece4c4360ff58/sdk/python/src/openlit/evals/offline.py#L214).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
