# CSVLint — CSV errors need row and severity

**Decision question:** Can a malformed row be traced without discarding the file silently?

| Field | Review |
| --- | --- |
| Upstream | [CSVLint](https://github.com/BdR76/CSVLint) |
| Primary area | Data Quality & Lineage |
| Source commit | [6a84207ccf780869fc5daedbb7b341cd34464880](https://github.com/BdR76/CSVLint/commit/6a84207ccf780869fc5daedbb7b341cd34464880) |
| Reviewed | 2026-10-06 |
| Declared license | [GPL-3.0](https://github.com/BdR76/CSVLint/blob/6a84207ccf780869fc5daedbb7b341cd34464880/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its validator stores line number and severity for errors while inspecting data values against field definitions. An editor plugin is not a pipeline guard, and syntactically valid CSV cannot prove causal timestamps or source completeness. |

## What this project does

A Notepad++ plugin for CSV and fixed-width validation. [README](https://github.com/BdR76/CSVLint/blob/6a84207ccf780869fc5daedbb7b341cd34464880/readme.md).

## Mechanism inspected

Its validator stores line number and severity for errors while inspecting data values against field definitions. [Implementation](https://github.com/BdR76/CSVLint/blob/6a84207ccf780869fc5daedbb7b341cd34464880/CSVLintNppPlugin/CsvLint/CsvValidate.cs#L18-L50).

## Limitation that matters

An editor plugin is not a pipeline guard, and syntactically valid CSV cannot prove causal timestamps or source completeness. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Preserve file, row and severity in collector quarantine receipts instead of silently skipping bad input.

## Why this score

Transferable engineering pattern: Its validator stores line number and severity for errors while inspecting data values against field definitions. An editor plugin is not a pipeline guard, and syntactically valid CSV cannot prove causal timestamps or source completeness.

## Source trail

[README](https://github.com/BdR76/CSVLint/blob/6a84207ccf780869fc5daedbb7b341cd34464880/readme.md) · [Documentation](https://github.com/BdR76/CSVLint/blob/6a84207ccf780869fc5daedbb7b341cd34464880/docs/readme.md) · [Implementation](https://github.com/BdR76/CSVLint/blob/6a84207ccf780869fc5daedbb7b341cd34464880/CSVLintNppPlugin/CsvLint/CsvValidate.cs#L18-L50).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
