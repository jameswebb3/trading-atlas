# swagger-conformance — Generated API cases are only as strict as the declared responses

**Decision question:** What does schema-driven API testing do when success codes are underspecified?

| Field | Review |
| --- | --- |
| Upstream | [olipratt/swagger-conformance](https://github.com/olipratt/swagger-conformance) |
| Primary area | Testing & Verification |
| Source commit | [8b6fdf99fd6a1db4eb69071c1e8d8a383ebcf76f](https://github.com/olipratt/swagger-conformance/commit/8b6fdf99fd6a1db4eb69071c1e8d8a383ebcf76f) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/olipratt/swagger-conformance/blob/8b6fdf99fd6a1db4eb69071c1e8d8a383ebcf76f/LICENSE.txt)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its operation strategy generates required and optional parameters; response checking falls back to any 2xx or adds 200 when the schema omits explicit success responses. An underspecified schema can make a false success look conformant; schema validity alone does not validate trading state. |

## What this project does

Python OpenAPI conformance tool driven by Hypothesis strategies. [README](https://github.com/olipratt/swagger-conformance/blob/8b6fdf99fd6a1db4eb69071c1e8d8a383ebcf76f/readme.md).

## Mechanism inspected

Its operation strategy generates required and optional parameters; response checking falls back to any 2xx or adds 200 when the schema omits explicit success responses. [Implementation](https://github.com/olipratt/swagger-conformance/blob/8b6fdf99fd6a1db4eb69071c1e8d8a383ebcf76f/swaggerconformance/schema/_operation.py#L37-L106).

## Limitation that matters

An underspecified schema can make a false success look conformant; schema validity alone does not validate trading state. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Require explicit success and error envelopes for order and data endpoints, plus downstream state assertions.

## Why this score

Its operation strategy generates required and optional parameters; response checking falls back to any 2xx or adds 200 when the schema omits explicit success responses. An underspecified schema can make a false success look conformant; schema validity alone does not validate trading state.

## Source trail

[README](https://github.com/olipratt/swagger-conformance/blob/8b6fdf99fd6a1db4eb69071c1e8d8a383ebcf76f/readme.md) · [Implementation](https://github.com/olipratt/swagger-conformance/blob/8b6fdf99fd6a1db4eb69071c1e8d8a383ebcf76f/swaggerconformance/schema/_operation.py#L37-L106) · [License](https://github.com/olipratt/swagger-conformance/blob/8b6fdf99fd6a1db4eb69071c1e8d8a383ebcf76f/LICENSE.txt).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
