# TraderHarness - Can an agent be blinded to calendar cues without changing the replay clock?

**Decision question:** Can an agent be blinded to calendar cues without changing the replay clock?

| Field | Review |
| --- | --- |
| Upstream | [HephaestLab/TraderHarness](https://github.com/HephaestLab/TraderHarness) |
| Primary area | Agents & Decision Systems |
| Source commit | [3e18369da5a2060f9c65b27c2a63f99edd93e167](https://github.com/HephaestLab/TraderHarness/commit/3e18369da5a2060f9c65b27c2a63f99edd93e167) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | DateMasker maps visible dates to relative offsets while the engine retains real dates internally; the loader refuses raw chunk fallback when canonical data is absent. Masking is presentation-only: it does not prove point-in-time availability or prevent a tool from exposing future data by another path. |

## What this project does

A trading-agent harness with date masking and canonical intraday data loading.

## Mechanism inspected

DateMasker maps visible dates to relative offsets while the engine retains real dates internally; the loader refuses raw chunk fallback when canonical data is absent.

## Limitation that matters

Masking is presentation-only: it does not prove point-in-time availability or prevent a tool from exposing future data by another path.

## Practical check for a trading system

Keep agent-visible blinding separate from source-time access controls and compare blinded versus unblinded evaluations.

## Why this score

3/5. The explicit presentation boundary is a useful agent-evaluation pattern.

## Source trail

[README](https://github.com/HephaestLab/TraderHarness/blob/3e18369da5a2060f9c65b27c2a63f99edd93e167/README.md#L1); [traderharness/core/masking.py](https://github.com/HephaestLab/TraderHarness/blob/3e18369da5a2060f9c65b27c2a63f99edd93e167/traderharness/core/masking.py#L1); [traderharness/core/masking.py](https://github.com/HephaestLab/TraderHarness/blob/3e18369da5a2060f9c65b27c2a63f99edd93e167/traderharness/core/masking.py#L12); [traderharness/data/market_data_manager.py](https://github.com/HephaestLab/TraderHarness/blob/3e18369da5a2060f9c65b27c2a63f99edd93e167/traderharness/data/market_data_manager.py#L143); [traderharness/data/market_data_manager.py](https://github.com/HephaestLab/TraderHarness/blob/3e18369da5a2060f9c65b27c2a63f99edd93e167/traderharness/data/market_data_manager.py#L153); [Root license](https://github.com/HephaestLab/TraderHarness/blob/3e18369da5a2060f9c65b27c2a63f99edd93e167/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
