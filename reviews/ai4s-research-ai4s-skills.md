# AI4S Skills — Bibliography recency is a check, not evidence

**Decision question:** Can a research writeup show whether its references cover a fast-moving field?

| Field | Review |
| --- | --- |
| Upstream | [ai4s-research/ai4s-skills](https://github.com/ai4s-research/ai4s-skills) |
| Primary area | Agents & Decision Systems |
| Source commit | [744ab2049a7b52ae726c43313468fd518b330980](https://github.com/ai4s-research/ai4s-skills/commit/744ab2049a7b52ae726c43313468fd518b330980) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/ai4s-research/ai4s-skills/blob/744ab2049a7b52ae726c43313468fd518b330980/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Executive assessment | Its bibliography checker applies an explicit recency profile with different minimum recent-year shares. A recent bibliography can still be irrelevant or wrong; dates do not establish code behavior or a trading mechanism. |

## What this project does

A collection of scientific research skills and paper templates. [Project README](https://github.com/ai4s-research/ai4s-skills/blob/744ab2049a7b52ae726c43313468fd518b330980/README.md#L1).

## Mechanism inspected

Its bibliography checker applies an explicit recency profile with different minimum recent-year shares. [Implementation](https://github.com/ai4s-research/ai4s-skills/blob/744ab2049a7b52ae726c43313468fd518b330980/skills/paper-writer/templates/paper/check_bibliography_freshness.py#L1).

## Limitation that matters

A recent bibliography can still be irrelevant or wrong; dates do not establish code behavior or a trading mechanism. This is a source review, not a runtime or security test.

## Practical check for a trading system

Use recency checks to flag stale external claims, then trace each consequential claim to primary source and code.

## Why this score

A light research hygiene pattern with limited direct trading value.

## Source trail

[README](https://github.com/ai4s-research/ai4s-skills/blob/744ab2049a7b52ae726c43313468fd518b330980/README.md#L1); [Implementation](https://github.com/ai4s-research/ai4s-skills/blob/744ab2049a7b52ae726c43313468fd518b330980/skills/paper-writer/templates/paper/check_bibliography_freshness.py#L1) - [License](https://github.com/ai4s-research/ai4s-skills/blob/744ab2049a7b52ae726c43313468fd518b330980/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
