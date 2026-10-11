# AI Trading Agent — Third-party indicators need publication time

**Decision question:** Can an LLM trade from an indicator whose data timing is unknown?

| Field | Review |
| --- | --- |
| Upstream | [Gajesh2007/ai-trading-agent](https://github.com/Gajesh2007/ai-trading-agent) |
| Primary area | Execution & Exchange Integration |
| Source commit | [bc14127d9f4bc5f45bf2cd65ec6fd25aba944418](https://github.com/Gajesh2007/ai-trading-agent/commit/bc14127d9f4bc5f45bf2cd65ec6fd25aba944418) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Its decision maker sends a Binance symbol and interval to TAAPI when the model requests an indicator. The inspected call path does not preserve source publication time or a reproducible indicator artifact; the external service adds dependency and timing uncertainty. |

## What this project does

A Hyperliquid agent that calls an external technical-analysis API and proposes orders. [Project README](https://github.com/Gajesh2007/ai-trading-agent/blob/bc14127d9f4bc5f45bf2cd65ec6fd25aba944418/README.md#L1).

## Mechanism inspected

Its decision maker sends a Binance symbol and interval to TAAPI when the model requests an indicator. [Implementation](https://github.com/Gajesh2007/ai-trading-agent/blob/bc14127d9f4bc5f45bf2cd65ec6fd25aba944418/src/agent/decision_maker.py#L298). [Related source 1](https://github.com/Gajesh2007/ai-trading-agent/blob/bc14127d9f4bc5f45bf2cd65ec6fd25aba944418/docs/ARCHITECTURE.md#L5).

## Limitation that matters

The inspected call path does not preserve source publication time or a reproducible indicator artifact; the external service adds dependency and timing uncertainty. This is a source review, not a runtime or security test.

## Practical check for a trading system

Record the raw market observation, calculation version, and available_at for every indicator entering a trade decision.

## Why this score

Direct venue target, but data lineage and decision reproducibility are too weak for an alpha claim.

## Source trail

[README](https://github.com/Gajesh2007/ai-trading-agent/blob/bc14127d9f4bc5f45bf2cd65ec6fd25aba944418/README.md#L1); [Implementation](https://github.com/Gajesh2007/ai-trading-agent/blob/bc14127d9f4bc5f45bf2cd65ec6fd25aba944418/src/agent/decision_maker.py#L298); [Related source 1](https://github.com/Gajesh2007/ai-trading-agent/blob/bc14127d9f4bc5f45bf2cd65ec6fd25aba944418/docs/ARCHITECTURE.md#L5).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
