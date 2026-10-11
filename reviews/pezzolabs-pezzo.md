# Pezzo - Does a prompt version hash identify only its content?

**Decision question:** Does a prompt version hash identify only its content?

| Field | Review |
| --- | --- |
| Upstream | [pezzolabs/pezzo](https://github.com/pezzolabs/pezzo) |
| Primary area | Research & Reproducibility |
| Source commit | [0787e3c037ad24544c2d3e6842507c3e7461a1de](https://github.com/pezzolabs/pezzo/commit/0787e3c037ad24544c2d3e6842507c3e7461a1de) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The prompt service hashes content, settings, prompt ID and Date.now into a version identifier. Identical prompt bytes can get different hashes at different times; this is not a pure content digest. |

## What this project does

An LLM prompt management platform.

## Mechanism inspected

The prompt service hashes content, settings, prompt ID and Date.now into a version identifier.

## Limitation that matters

Identical prompt bytes can get different hashes at different times; this is not a pure content digest.

## Practical check for a trading system

Store a stable content digest separately from a version or creation ID.

## Why this score

2/5. A concrete research-agent reproducibility warning.

## Source trail

[README](https://github.com/pezzolabs/pezzo/blob/0787e3c037ad24544c2d3e6842507c3e7461a1de/README.md#L1); [apps/server/src/app/prompts/prompts.service.ts](https://github.com/pezzolabs/pezzo/blob/0787e3c037ad24544c2d3e6842507c3e7461a1de/apps/server/src/app/prompts/prompts.service.ts#L55); [apps/server/src/app/prompts/prompts.service.ts](https://github.com/pezzolabs/pezzo/blob/0787e3c037ad24544c2d3e6842507c3e7461a1de/apps/server/src/app/prompts/prompts.service.ts#L60); [Root license](https://github.com/pezzolabs/pezzo/blob/0787e3c037ad24544c2d3e6842507c3e7461a1de/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
