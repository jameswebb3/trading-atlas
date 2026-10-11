# CSVLint.io — Missing source and malformed source are different

**Decision question:** Can a validation record distinguish not found from invalid?

| Field | Review |
| --- | --- |
| Upstream | [CSVLint.io](https://github.com/Data-Liberation-Front/csvlint.io) |
| Primary area | Data Quality & Lineage |
| Source commit | [320ebdfa5d455392adbbf68534a1a24a1505f8af](https://github.com/Data-Liberation-Front/csvlint.io/commit/320ebdfa5d455392adbbf68534a1a24a1505f8af) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/Data-Liberation-Front/csvlint.io/blob/320ebdfa5d455392adbbf68534a1a24a1505f8af/LICENSE.md) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The Validation model sets invalid on errors but overrides state to not_found when the error type says the source was absent. That state is the service's own classification; parsing, schema validity and source receipt time remain separate questions. |

## What this project does

A Rails service that validates CSV against CSVW or Data Package schemas. [README](https://github.com/Data-Liberation-Front/csvlint.io/blob/320ebdfa5d455392adbbf68534a1a24a1505f8af/README.md).

## Mechanism inspected

The Validation model sets invalid on errors but overrides state to not_found when the error type says the source was absent. [Implementation](https://github.com/Data-Liberation-Front/csvlint.io/blob/320ebdfa5d455392adbbf68534a1a24a1505f8af/app/models/validation.rb#L23-L48).

## Limitation that matters

That state is the service's own classification; parsing, schema validity and source receipt time remain separate questions. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Preserve SOURCE_ABSENT versus INVALID_DATA in collector receipts and report both counts.

## Why this score

Transferable engineering pattern: The Validation model sets invalid on errors but overrides state to not_found when the error type says the source was absent. That state is the service's own classification; parsing, schema validity and source receipt time remain separate questions.

## Source trail

[README](https://github.com/Data-Liberation-Front/csvlint.io/blob/320ebdfa5d455392adbbf68534a1a24a1505f8af/README.md) · [Implementation](https://github.com/Data-Liberation-Front/csvlint.io/blob/320ebdfa5d455392adbbf68534a1a24a1505f8af/app/models/validation.rb#L23-L48).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
