# Superior Trade — Static guards are a first sieve

**Decision question:** Can a generated trading strategy be screened before it reaches a backtest?

| Field | Review |
| --- | --- |
| Upstream | [Superior-Trade/trading-terminal](https://github.com/Superior-Trade/trading-terminal) |
| Primary area | Execution & Exchange Integration |
| Source commit | [f0a2081c51f509e761e4176323ff2bf20c3f9961](https://github.com/Superior-Trade/trading-terminal/commit/f0a2081c51f509e761e4176323ff2bf20c3f9961) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/Superior-Trade/trading-terminal/blob/f0a2081c51f509e761e4176323ff2bf20c3f9961/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The guard rejects known code patterns and configuration mistakes, including invalid TA-Lib multi-output access and selected lookahead hazards. Regex and static checks can miss equivalent bad code; passing this sieve does not prove causal data timing or safe live execution. |

## What this project does

A Hyperliquid-oriented trading terminal that generates and checks Freqtrade strategies. [Project README](https://github.com/Superior-Trade/trading-terminal/blob/f0a2081c51f509e761e4176323ff2bf20c3f9961/README.md#L102).

## Mechanism inspected

The guard rejects known code patterns and configuration mistakes, including invalid TA-Lib multi-output access and selected lookahead hazards. [Implementation](https://github.com/Superior-Trade/trading-terminal/blob/f0a2081c51f509e761e4176323ff2bf20c3f9961/lib/freqtrade-guard.ts#L122). [Related source 1](https://github.com/Superior-Trade/trading-terminal/blob/f0a2081c51f509e761e4176323ff2bf20c3f9961/docs/strategy-pipeline.md#L40).

## Limitation that matters

Regex and static checks can miss equivalent bad code; passing this sieve does not prove causal data timing or safe live execution. This is a source review, not a runtime or security test.

## Practical check for a trading system

Use static guards to fail obvious cases, then require causal tests and event-based replay before approval.

## Why this score

A concrete defensive layer for generated strategies, with an explicit need for deeper dynamic validation.

## Source trail

[README](https://github.com/Superior-Trade/trading-terminal/blob/f0a2081c51f509e761e4176323ff2bf20c3f9961/README.md#L102); [Implementation](https://github.com/Superior-Trade/trading-terminal/blob/f0a2081c51f509e761e4176323ff2bf20c3f9961/lib/freqtrade-guard.ts#L122); [Related source 1](https://github.com/Superior-Trade/trading-terminal/blob/f0a2081c51f509e761e4176323ff2bf20c3f9961/docs/strategy-pipeline.md#L40) - [License](https://github.com/Superior-Trade/trading-terminal/blob/f0a2081c51f509e761e4176323ff2bf20c3f9961/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
