# pytrade.org — Unknown capability is different from no

**Decision question:** How should a trading-library inventory represent unverified capabilities?

| Field | Review |
| --- | --- |
| Upstream | [PFund-Software-Ltd/pytrade.org](https://github.com/PFund-Software-Ltd/pytrade.org) |
| Primary area | Research & Reproducibility |
| Source commit | [a783f0cc1d745f79dde3b15dbfa6ff9d83d7aa6a](https://github.com/PFund-Software-Ltd/pytrade.org/commit/a783f0cc1d745f79dde3b15dbfa6ff9d83d7aa6a) |
| Reviewed | 2026-10-09 |
| Declared license | CC-BY-4.0 ([source](https://github.com/PFund-Software-Ltd/pytrade.org/blob/a783f0cc1d745f79dde3b15dbfa6ff9d83d7aa6a/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Its table renders capability cells as true, false or N/A rather than forcing all missing fields to false. This is catalog presentation logic, not source verification; an N/A cell still needs a stated evidence trail and date. |

## What this project does

Curated learning website and library inventory for Python trading. [README](https://github.com/PFund-Software-Ltd/pytrade.org/blob/a783f0cc1d745f79dde3b15dbfa6ff9d83d7aa6a/README.md).

## Mechanism inspected

Its table renders capability cells as true, false or N/A rather than forcing all missing fields to false. [Implementation](https://github.com/PFund-Software-Ltd/pytrade.org/blob/a783f0cc1d745f79dde3b15dbfa6ff9d83d7aa6a/src/pytrade/table.py#L84-L137).

## Limitation that matters

This is catalog presentation logic, not source verification; an N/A cell still needs a stated evidence trail and date. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Use an explicit unknown state in capability comparisons while linking each verified claim to source.

## Why this score

Its table renders capability cells as true, false or N/A rather than forcing all missing fields to false. This is catalog presentation logic, not source verification; an N/A cell still needs a stated evidence trail and date.

## Source trail

[README](https://github.com/PFund-Software-Ltd/pytrade.org/blob/a783f0cc1d745f79dde3b15dbfa6ff9d83d7aa6a/README.md) · [Implementation](https://github.com/PFund-Software-Ltd/pytrade.org/blob/a783f0cc1d745f79dde3b15dbfa6ff9d83d7aa6a/src/pytrade/table.py#L84-L137) · [License](https://github.com/PFund-Software-Ltd/pytrade.org/blob/a783f0cc1d745f79dde3b15dbfa6ff9d83d7aa6a/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
