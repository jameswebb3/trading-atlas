# openapi-cop — Validate the exchange response as well as the request

**Decision question:** Can an accepted HTTP call still violate its response contract?

| Field | Review |
| --- | --- |
| Upstream | [openapi-cop](https://github.com/EXXETA/openapi-cop) |
| Primary area | Data Quality & Lineage |
| Source commit | [72a2d4457e1a22841e36ccd49abb4213e98a653f](https://github.com/EXXETA/openapi-cop/commit/72a2d4457e1a22841e36ccd49abb4213e98a653f) |
| Reviewed | 2026-10-06 |
| Declared license | [Custom or not identified](https://github.com/EXXETA/openapi-cop/blob/72a2d4457e1a22841e36ccd49abb4213e98a653f/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The validator separately checks request, response status/content and response headers, then flags any invalid part. A schema match cannot settle asynchronous ACK, duplicate fills or missing venue events; an external proxy is unnecessary for a small HL adapter. |

## What this project does

An OpenAPI proxy that validates request bodies, response bodies and response headers against a schema. [README](https://github.com/EXXETA/openapi-cop/blob/72a2d4457e1a22841e36ccd49abb4213e98a653f/README.md).

## Mechanism inspected

The validator separately checks request, response status/content and response headers, then flags any invalid part. [Implementation](https://github.com/EXXETA/openapi-cop/blob/72a2d4457e1a22841e36ccd49abb4213e98a653f/src/validation.ts#L81-L153).

## Limitation that matters

A schema match cannot settle asynchronous ACK, duplicate fills or missing venue events; an external proxy is unnecessary for a small HL adapter. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Add offline fixtures for malformed HL response envelopes and header/status mismatches at the adapter boundary.

## Why this score

Transferable engineering pattern: The validator separately checks request, response status/content and response headers, then flags any invalid part. A schema match cannot settle asynchronous ACK, duplicate fills or missing venue events; an external proxy is unnecessary for a small HL adapter.

## Source trail

[README](https://github.com/EXXETA/openapi-cop/blob/72a2d4457e1a22841e36ccd49abb4213e98a653f/README.md) · [Implementation](https://github.com/EXXETA/openapi-cop/blob/72a2d4457e1a22841e36ccd49abb4213e98a653f/src/validation.ts#L81-L153).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
