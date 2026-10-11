# AI Researcher - What happens when an automated judge fails during idea ranking?

**Decision question:** What happens when an automated judge fails during idea ranking?

| Field | Review |
| --- | --- |
| Upstream | [mguozhen/ai-researcher](https://github.com/mguozhen/ai-researcher) |
| Primary area | Agents & Decision Systems |
| Source commit | [e8171bb6e1ff26f969a46e665ad2a7d18485c54e](https://github.com/mguozhen/ai-researcher/commit/e8171bb6e1ff26f969a46e665ad2a7d18485c54e) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | When a pairwise call fails, the bracket chooses a random winner and records the error in its reasoning. The final ranking can include a random advancement while still appearing complete. |

## What this project does

A research-idea tournament driven by pairwise model comparisons.

## Mechanism inspected

When a pairwise call fails, the bracket chooses a random winner and records the error in its reasoning.

## Limitation that matters

The final ranking can include a random advancement while still appearing complete.

## Practical check for a trading system

Mark failed comparisons unresolved and rerun them before ranking ideas.

## Why this score

1/5. A concrete negative example for research-agent evaluation.

## Source trail

[README](https://github.com/mguozhen/ai-researcher/blob/e8171bb6e1ff26f969a46e665ad2a7d18485c54e/README.md#L1); [scripts/tournament_ideas.py](https://github.com/mguozhen/ai-researcher/blob/e8171bb6e1ff26f969a46e665ad2a7d18485c54e/scripts/tournament_ideas.py#L95); [scripts/tournament_ideas.py](https://github.com/mguozhen/ai-researcher/blob/e8171bb6e1ff26f969a46e665ad2a7d18485c54e/scripts/tournament_ideas.py#L110); [Root license](https://github.com/mguozhen/ai-researcher/blob/e8171bb6e1ff26f969a46e665ad2a7d18485c54e/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
