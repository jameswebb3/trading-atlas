# Polymarket Sports Trading Bot - Is live match state aligned to the market quote that a model scores?

**Decision question:** Is live match state aligned to the market quote that a model scores?

| Field | Review |
| --- | --- |
| Upstream | [rustyneuron01/Polymarket-Sports-Trading-Bot](https://github.com/rustyneuron01/Polymarket-Sports-Trading-Bot) |
| Primary area | Signals & Models |
| Source commit | [8f68304257d2064ddd4e308e16083267e8fe3826](https://github.com/rustyneuron01/Polymarket-Sports-Trading-Bot/commit/8f68304257d2064ddd4e308e16083267e8fe3826) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Builds in-game price targets from sports market snapshots. An index-based game clock can attach the wrong or future score to a quote. |

## What this project does

A sports prediction-market research bot that builds in-game training rows and runs simulated trading.

## Mechanism inspected

Its dataset builder joins recorded prices and match events, creates future-window bid targets, and supplies score and period fields to a model.

## Limitation that matters

Because real game start time is unavailable, it maps row index times 60 seconds to game state. Uneven snapshots can therefore attach a future score to an earlier market quote. Future-window best bids are labels, not executable sell guarantees. No root license text was verified.

## Practical check for a trading system

Require independently timestamped score events and market quotes with publication time before using in-game features or reported returns.

## Why this score

1/5. The core as-of join is unverified and can invalidate the apparent signal, so this is a caution rather than an alpha reference.

## Source trail

[README](https://github.com/rustyneuron01/Polymarket-Sports-Trading-Bot/blob/8f68304257d2064ddd4e308e16083267e8fe3826/README.md#L11); [build_in_game_dataset.py](https://github.com/rustyneuron01/Polymarket-Sports-Trading-Bot/blob/8f68304257d2064ddd4e308e16083267e8fe3826/build_in_game_dataset.py#L155); [build_in_game_dataset.py](https://github.com/rustyneuron01/Polymarket-Sports-Trading-Bot/blob/8f68304257d2064ddd4e308e16083267e8fe3826/build_in_game_dataset.py#L181); [build_in_game_dataset.py](https://github.com/rustyneuron01/Polymarket-Sports-Trading-Bot/blob/8f68304257d2064ddd4e308e16083267e8fe3826/build_in_game_dataset.py#L202).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
