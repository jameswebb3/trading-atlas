# preflight - A preflight pass must distinguish skipped from checked

**Decision question:** Does a fatal data check stay blocking when its input cannot be inspected?

| Field | Review |
| --- | --- |
| Upstream | [Rusheel86/preflight](https://github.com/Rusheel86/preflight) |
| Primary area | Data Quality & Lineage |
| Source commit | [93110405bde8fdd45524b2bbedbd0de2e8206af7](https://github.com/Rusheel86/preflight/commit/93110405bde8fdd45524b2bbedbd0de2e8206af7) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Samples batches for non-finite values and exposes severity-coded preflight results. Dataloader failure downgrades the fatal check to a warning; skipped checks can appear as passed, so zero fatal failures need not mean full coverage. |

## What this project does

A PyTorch preflight tool that samples data, checks NaN and Inf values, and reports severity-coded training checks before a job starts.

## Mechanism inspected

The NaN and Inf check scans a configurable number of batches and returns a fatal failure when non-finite values are observed. Its tests include clean and NaN-containing loaders, while the registry gives each result a severity and pass flag.

## Limitation that matters

If dataloader iteration raises, this formerly fatal check returns a WARN failure. Other paths mark an uninspectable or absent input as passed with skipped text. A CI gate that blocks only fatal failures can therefore proceed without proving the data check ran. This is a source review, not a runtime or security test.

## Practical check for a trading system

Use separate PASS, FAIL and UNVERIFIED states for market-data and feature preflight. A missing source, unreadable batch or absent validation split should be an explicit gate decision rather than a passing check.

## Why this score

2/5 because this transferable preflight pattern and its failure mode are visible in code and tests, but the check is for PyTorch batches rather than trading data.

## Source trail

[README](https://github.com/Rusheel86/preflight/blob/93110405bde8fdd45524b2bbedbd0de2e8206af7/README.md#L100); [NaN check](https://github.com/Rusheel86/preflight/blob/93110405bde8fdd45524b2bbedbd0de2e8206af7/preflight/checks/data.py#L10); [Exception downgrade](https://github.com/Rusheel86/preflight/blob/93110405bde8fdd45524b2bbedbd0de2e8206af7/preflight/checks/data.py#L35); [Result type](https://github.com/Rusheel86/preflight/blob/93110405bde8fdd45524b2bbedbd0de2e8206af7/preflight/registry.py#L8); [Tests](https://github.com/Rusheel86/preflight/blob/93110405bde8fdd45524b2bbedbd0de2e8206af7/tests/test_data.py#L5); [License](https://github.com/Rusheel86/preflight/blob/93110405bde8fdd45524b2bbedbd0de2e8206af7/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
