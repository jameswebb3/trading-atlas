# logfire — Scrubbing records redaction while keeping a sensitive-key bypass list

**Decision question:** Can a trace prove what it redacted?

| Field | Review |
| --- | --- |
| Upstream | [pydantic/logfire](https://github.com/pydantic/logfire) |
| Primary area | Operations & Observability |
| Source commit | [e00fed0f6eef1bd6e5b0271b91bdcf9d0a31968c](https://github.com/pydantic/logfire/commit/e00fed0f6eef1bd6e5b0271b91bdcf9d0a31968c) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/pydantic/logfire/blob/e00fed0f6eef1bd6e5b0271b91bdcf9d0a31968c/LICENSE)) |
| Review depth | 3/3: documentation and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The scrubber applies patterns to span values and stores notes identifying scrubbed paths in an attribute. It skips selected instrumentation scopes and has safe-key exemptions; neither the notes nor regexes prove every secret was removed. |

## What this project does

Observability client with structured traces and sensitive-data scrubbing. [README](https://github.com/pydantic/logfire/blob/e00fed0f6eef1bd6e5b0271b91bdcf9d0a31968c/README.md).

## Mechanism inspected

The scrubber applies patterns to span values and stores notes identifying scrubbed paths in an attribute. [Implementation](https://github.com/pydantic/logfire/blob/e00fed0f6eef1bd6e5b0271b91bdcf9d0a31968c/logfire-sdk/logfire/_internal/scrubbing.py#L208-L243). [Test source](https://github.com/pydantic/logfire/blob/e00fed0f6eef1bd6e5b0271b91bdcf9d0a31968c/tests/test_secret_scrubbing.py#L41-L62).

## Limitation that matters

It skips selected instrumentation scopes and has safe-key exemptions; neither the notes nor regexes prove every secret was removed. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Test private order and credential fixtures against log export, recording redaction coverage and explicit exemptions.

## Why this score

The scrubber applies patterns to span values and stores notes identifying scrubbed paths in an attribute. It skips selected instrumentation scopes and has safe-key exemptions; neither the notes nor regexes prove every secret was removed.

## Source trail

[README](https://github.com/pydantic/logfire/blob/e00fed0f6eef1bd6e5b0271b91bdcf9d0a31968c/README.md) · [Implementation](https://github.com/pydantic/logfire/blob/e00fed0f6eef1bd6e5b0271b91bdcf9d0a31968c/logfire-sdk/logfire/_internal/scrubbing.py#L208-L243) · [Test source](https://github.com/pydantic/logfire/blob/e00fed0f6eef1bd6e5b0271b91bdcf9d0a31968c/tests/test_secret_scrubbing.py#L41-L62) · [License](https://github.com/pydantic/logfire/blob/e00fed0f6eef1bd6e5b0271b91bdcf9d0a31968c/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
