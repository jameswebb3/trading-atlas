# mm-lab - Can a fast market-making kernel be checked against an independent fill specification?

**Decision question:** Can a fast market-making kernel be checked against an independent fill specification?

| Field | Review |
| --- | --- |
| Upstream | [batuhanboztepe0/mm-lab](https://github.com/batuhanboztepe0/mm-lab) |
| Primary area | Backtesting & Simulation |
| Source commit | [c2ea2f7bd88cf08afd03da3b19d175822af389cc](https://github.com/batuhanboztepe0/mm-lab/commit/c2ea2f7bd88cf08afd03da3b19d175822af389cc) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Defines a readable fill oracle for a fast kernel, fingerprints cached research cells, and checks fill-log accounting against engine state. Queue cancellation placement remains a bounded assumption; legacy cache entries lack independent final counters. |

## What this project does

A preregistered market-making research lab with multiple fill assumptions, a readable reference engine, a faster Numba kernel and fill-log accounting.

## Mechanism inspected

The pure-Python reference freezes event order, action latency, post-only clipping, inventory cap and queue cancellation bounds. The Numba kernel states it must match that fill log bit for bit. The runner fingerprints strategy tables and behavior parameters for cache reuse and independently reconciles engine final counters against the fill log.

## Limitation that matters

The README reports negative and positive findings, but source reading does not replicate them. The F1 queue position is estimated from L1 displayed size under cancellation bounds, not an observed exchange queue. Older cached runs without stored engine counters are reconciled from the same fill log, so that legacy path is a weaker cross-check.

## Practical check for a trading system

Keep a slow semantic oracle separate from the fast backtest engine, compare complete fill logs, and bind cached outcomes to every behavior-changing parameter.

## Why this score

4/5 because Direct trading mechanics, preregistration and a two-path accounting guard are visible; queue estimates and unreplicated results keep the review below 5/5.

## Source trail

[README fill-model scope](https://github.com/batuhanboztepe0/mm-lab/blob/c2ea2f7bd88cf08afd03da3b19d175822af389cc/README.md#L26); [Reference semantics](https://github.com/batuhanboztepe0/mm-lab/blob/c2ea2f7bd88cf08afd03da3b19d175822af389cc/src/mmlab/reference.py#L1); [Fast-kernel contract](https://github.com/batuhanboztepe0/mm-lab/blob/c2ea2f7bd88cf08afd03da3b19d175822af389cc/src/mmlab/kernel.py#L1); [Cache fingerprint and accounting](https://github.com/batuhanboztepe0/mm-lab/blob/c2ea2f7bd88cf08afd03da3b19d175822af389cc/scripts/run_backtest.py#L101); [License](https://github.com/batuhanboztepe0/mm-lab/blob/c2ea2f7bd88cf08afd03da3b19d175822af389cc/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
