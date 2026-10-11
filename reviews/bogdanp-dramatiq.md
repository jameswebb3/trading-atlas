# Dramatiq — Can a permanent task failure be kept out of an automatic retry loop

**Decision question:** Can a permanent task failure be kept out of an automatic retry loop?

| Field | Review |
| --- | --- |
| Upstream | [Dramatiq](https://github.com/Bogdanp/dramatiq) |
| Primary area | Operations & Observability |
| Source commit | [e9e7c4312308a8c7c27896c64a6f437af07dce18](https://github.com/Bogdanp/dramatiq/commit/e9e7c4312308a8c7c27896c64a6f437af07dce18) |
| Reviewed | 2026-09-27 |
| Declared license | [LGPL-3.0](https://github.com/Bogdanp/dramatiq/blob/e9e7c4312308a8c7c27896c64a6f437af07dce18/COPYING.LESSER) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Distinguishes permanent exceptions from retryable work and records per-message retry evidence. Useful for bounded recovery policies that preserve failed attempts instead of hiding them behind a final success. |

## Project overview

A distributed Python task-processing library with per-actor retry policies. [Project documentation](https://github.com/Bogdanp/dramatiq/blob/e9e7c4312308a8c7c27896c64a6f437af07dce18/README.md#L10-L16).

## Mechanism worth inspecting

The retry middleware checks a throws exception class before retry bookkeeping. Other failures update retry count, traceback and requeue time; retry_when or max_retries governs exhaustion, with an optional exhaustion callback. [Retry classifier and evidence](https://github.com/Bogdanp/dramatiq/blob/e9e7c4312308a8c7c27896c64a6f437af07dce18/dramatiq/middleware/retries.py#L97-L148).

## Important limit

The guide assumes actors are idempotent, and a custom retry_when replaces the default maximum-retry decision. That predicate must impose its own bound; evidence retention cannot rely solely on a temporary dead-letter queue. [Retry contract](https://github.com/Bogdanp/dramatiq/blob/e9e7c4312308a8c7c27896c64a6f437af07dce18/docs/source/guide.rst#L154-L156), [options](https://github.com/Bogdanp/dramatiq/blob/e9e7c4312308a8c7c27896c64a6f437af07dce18/docs/source/guide.rst#L240-L268).

## Questions to take into your own design

- Which failures are permanent and which justify another attempt?
- Does a custom retry predicate have an explicit attempt or time budget?

## Why this score for a trading system

3/5: a specific transferable failure taxonomy and attempt ledger, with idempotence and custom retry bounds left to the application.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
