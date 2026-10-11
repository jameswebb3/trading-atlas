# Prediction Market Arbitrage - Does a cross-venue name match establish a tradable arbitrage?

**Decision question:** Does a cross-venue name match establish a tradable arbitrage?

| Field | Review |
| --- | --- |
| Upstream | [bentroutman/prediction-market-arbitrage](https://github.com/bentroutman/prediction-market-arbitrage) |
| Primary area | Signals & Models |
| Source commit | [3b245dd6e6bf54930b2af5af5539531c2d3e0ee1](https://github.com/bentroutman/prediction-market-arbitrage/commit/3b245dd6e6bf54930b2af5af5539531c2d3e0ee1) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The matching pipeline first filters Kalshi and Polymarket titles with TF-IDF cosine similarity, then applies fuzzy name similarity plus timeframe, entity, party and district checks before comparing yes/no ask prices. The timeframe checker treats two missing timeframes as compatible, and the code's name/entity tests cannot prove that venues share the same settlement rules. The threshold screen uses quote CSVs without a demonstrated common observation clock, depth or fee-adjusted fill path. |

## What this project does

Adds entity and timeframe checks to fuzzy market matching, but names and static ask prices do not prove settlement or executable arbitrage.

## Mechanism inspected

The matching pipeline first filters Kalshi and Polymarket titles with TF-IDF cosine similarity, then applies fuzzy name similarity plus timeframe, entity, party and district checks before comparing yes/no ask prices.

## Limitation that matters

The timeframe checker treats two missing timeframes as compatible, and the code's name/entity tests cannot prove that venues share the same settlement rules. The threshold screen uses quote CSVs without a demonstrated common observation clock, depth or fee-adjusted fill path.

## Practical check for a trading system

Record explicit event-rule equivalence, settlement date, quote timestamps and executable size before labeling any apparent cross-venue spread an opportunity.

## Why this score

2/5. The multi-stage matching pipeline is useful for event-market research, but the unresolved contract and execution evidence prevents a stronger score.

## Source trail

[README.md](https://github.com/bentroutman/prediction-market-arbitrage/blob/3b245dd6e6bf54930b2af5af5539531c2d3e0ee1/README.md#L1); [src/find_arbs.py](https://github.com/bentroutman/prediction-market-arbitrage/blob/3b245dd6e6bf54930b2af5af5539531c2d3e0ee1/src/find_arbs.py#L191); [src/find_arbs.py](https://github.com/bentroutman/prediction-market-arbitrage/blob/3b245dd6e6bf54930b2af5af5539531c2d3e0ee1/src/find_arbs.py#L213); [src/find_arbs.py](https://github.com/bentroutman/prediction-market-arbitrage/blob/3b245dd6e6bf54930b2af5af5539531c2d3e0ee1/src/find_arbs.py#L305); [src/find_arbs.py](https://github.com/bentroutman/prediction-market-arbitrage/blob/3b245dd6e6bf54930b2af5af5539531c2d3e0ee1/src/find_arbs.py#L319); [src/find_arbs.py](https://github.com/bentroutman/prediction-market-arbitrage/blob/3b245dd6e6bf54930b2af5af5539531c2d3e0ee1/src/find_arbs.py#L338); [src/find_arbs.py](https://github.com/bentroutman/prediction-market-arbitrage/blob/3b245dd6e6bf54930b2af5af5539531c2d3e0ee1/src/find_arbs.py#L375)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
