# MobyDQ — Job accepted is not check passed

**Decision question:** Does an API success response mean the data-quality job finished successfully?

| Field | Review |
| --- | --- |
| Upstream | [ubisoft/mobydq](https://github.com/ubisoft/mobydq) |
| Primary area | Data Quality & Lineage |
| Source commit | [7d0b76145cdd2d819278f21396e2ced78f7c69a3](https://github.com/ubisoft/mobydq/commit/7d0b76145cdd2d819278f21396e2ced78f7c69a3) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/ubisoft/mobydq/blob/7d0b76145cdd2d819278f21396e2ced78f7c69a3/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its resolver starts a Docker container for a batch and returns the database result immediately; the container callback does nothing. The GraphQL success response confirms dispatch, not completion or validation success. |

## What this project does

A container-based data-quality platform that launches indicators and exposes results through GraphQL. [Project README](https://github.com/ubisoft/mobydq/blob/7d0b76145cdd2d819278f21396e2ced78f7c69a3/README.md#L8).

## Mechanism inspected

Its resolver starts a Docker container for a batch and returns the database result immediately; the container callback does nothing. [Implementation](https://github.com/ubisoft/mobydq/blob/7d0b76145cdd2d819278f21396e2ced78f7c69a3/graphql/init/mobydq-plugin/index.js#L38). [Related source 1](https://github.com/ubisoft/mobydq/blob/7d0b76145cdd2d819278f21396e2ced78f7c69a3/docs/HOWTO.md#L1).

## Limitation that matters

The GraphQL success response confirms dispatch, not completion or validation success. A Docker socket in the API process also broadens operational risk. This is a source review, not a runtime or security test.

## Practical check for a trading system

Track accepted, running, completed, failed, and result-published as separate states for asynchronous data checks.

## Why this score

The asynchronous ACK distinction is transferable, but the platform and runtime exposure are excessive for a small trading pipeline.

## Source trail

[README](https://github.com/ubisoft/mobydq/blob/7d0b76145cdd2d819278f21396e2ced78f7c69a3/README.md#L8); [Implementation](https://github.com/ubisoft/mobydq/blob/7d0b76145cdd2d819278f21396e2ced78f7c69a3/graphql/init/mobydq-plugin/index.js#L38); [Related source 1](https://github.com/ubisoft/mobydq/blob/7d0b76145cdd2d819278f21396e2ced78f7c69a3/docs/HOWTO.md#L1) - [License](https://github.com/ubisoft/mobydq/blob/7d0b76145cdd2d819278f21396e2ced78f7c69a3/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
