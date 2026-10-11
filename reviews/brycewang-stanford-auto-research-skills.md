# Auto Research Skills — Check generated catalog counts offline

**Decision question:** How can a public research directory catch stale counts before release?

| Field | Review |
| --- | --- |
| Upstream | [brycewang-stanford/Auto-Research-Skills](https://github.com/brycewang-stanford/Auto-Research-Skills) |
| Primary area | Agents & Decision Systems |
| Source commit | [bebc638377754dd8988abe497eca2f146784c4a9](https://github.com/brycewang-stanford/Auto-Research-Skills/commit/bebc638377754dd8988abe497eca2f146784c4a9) |
| Reviewed | 2026-10-10 |
| Declared license | CC0-1.0 ([source](https://github.com/brycewang-stanford/Auto-Research-Skills/blob/bebc638377754dd8988abe497eca2f146784c4a9/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its offline repository checker compares Git submodules, tracked references, generated catalog freshness, headline counts, and star-table totals. Consistent counts do not establish that an individual project was read or deserves its rating; freshness checks need an evidence gate too. |

## What this project does

A directory of auto-research skills and related projects. [Project README](https://github.com/brycewang-stanford/Auto-Research-Skills/blob/bebc638377754dd8988abe497eca2f146784c4a9/README.md#L1).

## Mechanism inspected

Its offline repository checker compares Git submodules, tracked references, generated catalog freshness, headline counts, and star-table totals. [Implementation](https://github.com/brycewang-stanford/Auto-Research-Skills/blob/bebc638377754dd8988abe497eca2f146784c4a9/scripts/check-repo.py#L1).

## Limitation that matters

Consistent counts do not establish that an individual project was read or deserves its rating; freshness checks need an evidence gate too. This is a source review, not a runtime or security test.

## Practical check for a trading system

Run structural checks and review-evidence checks as separate release requirements for a curated catalog.

## Why this score

Useful for catalog integrity, but it is a maintenance pattern rather than trading research content.

## Source trail

[README](https://github.com/brycewang-stanford/Auto-Research-Skills/blob/bebc638377754dd8988abe497eca2f146784c4a9/README.md#L1); [Implementation](https://github.com/brycewang-stanford/Auto-Research-Skills/blob/bebc638377754dd8988abe497eca2f146784c4a9/scripts/check-repo.py#L1) - [License](https://github.com/brycewang-stanford/Auto-Research-Skills/blob/bebc638377754dd8988abe497eca2f146784c4a9/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
