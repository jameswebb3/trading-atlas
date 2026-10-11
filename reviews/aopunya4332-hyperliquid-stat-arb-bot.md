# Hyperliquid Statistical Arbitrage Bot - Does this pairs strategy actually observe and trade both legs?

**Decision question:** Does this pairs strategy actually observe and trade both legs?

| Field | Review |
| --- | --- |
| Upstream | [aopunya4332/hyperliquid-stat-arb-bot](https://github.com/aopunya4332/hyperliquid-stat-arb-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [3295ae8ba8d503f7185158f7ee2505358a3af770](https://github.com/aopunya4332/hyperliquid-stat-arb-bot/commit/3295ae8ba8d503f7185158f7ee2505358a3af770) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | The strategy computes a z-score of one coin's mid divided by a configured pair_mid; the default pair_mid is derived from that same mid. Its order builder submits only the configured coin. The inspected code does not fetch an independent second leg, establish cointegration, hedge a pair, or persist the displayed risk state across restarts. The runner constructs a zero-size position before calling risk checks. |

## What this project does

A Hyperliquid bot presented as cointegrated pairs mean reversion. Its shared runner polls one coin's mid, book and candles and submits orders for the configured coin.

## Mechanism inspected

The strategy computes a z-score of one coin's mid divided by a configured pair_mid; the default pair_mid is derived from that same mid. Its order builder submits only the configured coin.

## Limitation that matters

The inspected code does not fetch an independent second leg, establish cointegration, hedge a pair, or persist the displayed risk state across restarts. The runner constructs a zero-size position before calling risk checks.

## Practical check for a trading system

For a pairs claim, require two timestamped leg feeds, a stated hedge ratio, two-leg order accounting, and a replay that treats incomplete fills explicitly.

## Why this score

1/5. The code is a useful counterexample for source-checking strategy claims, but it does not implement the advertised two-leg mechanism.

## Source trail

[README](https://github.com/aopunya4332/hyperliquid-stat-arb-bot/blob/3295ae8ba8d503f7185158f7ee2505358a3af770/README.md#L1); [docs/api-reference.md](https://github.com/aopunya4332/hyperliquid-stat-arb-bot/blob/3295ae8ba8d503f7185158f7ee2505358a3af770/docs/api-reference.md#L1); [src/hyperliquid_bot/strategy.py](https://github.com/aopunya4332/hyperliquid-stat-arb-bot/blob/3295ae8ba8d503f7185158f7ee2505358a3af770/src/hyperliquid_bot/strategy.py#L13); [src/hyperliquid_bot/strategy.py](https://github.com/aopunya4332/hyperliquid-stat-arb-bot/blob/3295ae8ba8d503f7185158f7ee2505358a3af770/src/hyperliquid_bot/strategy.py#L28); [src/hyperliquid_bot/runner.py](https://github.com/aopunya4332/hyperliquid-stat-arb-bot/blob/3295ae8ba8d503f7185158f7ee2505358a3af770/src/hyperliquid_bot/runner.py#L44); [Root license](https://github.com/aopunya4332/hyperliquid-stat-arb-bot/blob/3295ae8ba8d503f7185158f7ee2505358a3af770/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
