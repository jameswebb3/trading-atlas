# TokenCost - Can agent experiment costs be estimated reproducibly?

**Decision question:** Can agent experiment costs be estimated reproducibly?

| Field | Review |
| --- | --- |
| Upstream | [AgentOps-AI/tokencost](https://github.com/AgentOps-AI/tokencost) |
| Primary area | Operations & Observability |
| Source commit | [e7f7c1928084af55bb4955102327982401ed8649](https://github.com/AgentOps-AI/tokencost/commit/e7f7c1928084af55bb4955102327982401ed8649) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It normalizes model names and computes cost from token counts with Decimal arithmetic. Price tables and fallback tokenization can diverge from billed usage over time. |

## What this project does

A token-cost calculator for language-model sessions.

## Mechanism inspected

It normalizes model names and computes cost from token counts with Decimal arithmetic.

## Limitation that matters

Price tables and fallback tokenization can diverge from billed usage over time.

## Practical check for a trading system

Store model, token counts, price-table version and billed cost separately.

## Why this score

2/5. Decimal calculations help budget experiments, but estimates need versioned rates.

## Source trail

[README](https://github.com/AgentOps-AI/tokencost/blob/e7f7c1928084af55bb4955102327982401ed8649/README.md#L1); [tokencost/costs.py](https://github.com/AgentOps-AI/tokencost/blob/e7f7c1928084af55bb4955102327982401ed8649/tokencost/costs.py#L101); [tokencost/costs.py](https://github.com/AgentOps-AI/tokencost/blob/e7f7c1928084af55bb4955102327982401ed8649/tokencost/costs.py#L340); [tokencost/costs.py](https://github.com/AgentOps-AI/tokencost/blob/e7f7c1928084af55bb4955102327982401ed8649/tokencost/costs.py#L308); [tokencost/costs.py](https://github.com/AgentOps-AI/tokencost/blob/e7f7c1928084af55bb4955102327982401ed8649/tokencost/costs.py#L320).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
