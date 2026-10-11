# TradzQAI — A fabricated bar needs a gap marker

**Decision question:** Can missing one-minute bars become plausible observations?

| Field | Review |
| --- | --- |
| Upstream | [kkuette/TradzQAI](https://github.com/kkuette/TradzQAI) |
| Primary area | Backtesting & Simulation |
| Source commit | [1f46cb2536b24cb3716250f1e9705daa76af4f60](https://github.com/kkuette/TradzQAI/commit/1f46cb2536b24cb3716250f1e9705daa76af4f60) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/kkuette/TradzQAI/blob/1f46cb2536b24cb3716250f1e9705daa76af4f60/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Its one-minute formatter creates rows for missing minutes by copying the preceding row's fields and carrying volume, then returns an ordinary dataframe without a separate synthetic-gap indicator. A flat carried-forward bar can look like observed market data. The inspected formatter provides no exchange-calendar or receipt-time proof, so it cannot establish valid intraminute execution. |

## What this project does

Reinforcement-learning trading environment with historical bar and tick loaders. [README](https://github.com/kkuette/TradzQAI/blob/1f46cb2536b24cb3716250f1e9705daa76af4f60/README.md).

## Mechanism inspected

Its one-minute formatter creates rows for missing minutes by copying the preceding row's fields and carrying volume, then returns an ordinary dataframe without a separate synthetic-gap indicator. [Implementation](https://github.com/kkuette/TradzQAI/blob/1f46cb2536b24cb3716250f1e9705daa76af4f60/TradzQAI/core/environnement/base/dataloader.py#L269-L302).

## Limitation that matters

A flat carried-forward bar can look like observed market data. The inspected formatter provides no exchange-calendar or receipt-time proof, so it cannot establish valid intraminute execution. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Keep source gaps and synthesized bars distinguishable in replay; disallow fills or causal feature claims that require observations absent from the raw feed.

## Why this score

Its one-minute formatter creates rows for missing minutes by copying the preceding row's fields and carrying volume, then returns an ordinary dataframe without a separate synthetic-gap indicator. A flat carried-forward bar can look like observed market data. The inspected formatter provides no exchange-calendar or receipt-time proof, so it cannot establish valid intraminute execution.

## Source trail

[README](https://github.com/kkuette/TradzQAI/blob/1f46cb2536b24cb3716250f1e9705daa76af4f60/README.md) · [Implementation](https://github.com/kkuette/TradzQAI/blob/1f46cb2536b24cb3716250f1e9705daa76af4f60/TradzQAI/core/environnement/base/dataloader.py#L269-L302) · [License](https://github.com/kkuette/TradzQAI/blob/1f46cb2536b24cb3716250f1e9705daa76af4f60/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
