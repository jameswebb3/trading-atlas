# vibe-astock - Check the actual inputs before an analysis runs

**Decision question:** Would an analysis still issue recommendations when its core feeds are empty?

| Field | Review |
| --- | --- |
| Upstream | [simonlin1212/vibe-astock](https://github.com/simonlin1212/vibe-astock) |
| Primary area | Signals & Models |
| Source commit | [3959826d653cfd8cb3e80bed73d7091de75e3d94](https://github.com/simonlin1212/vibe-astock/commit/3959826d653cfd8cb3e80bed73d7091de75e3d94) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/simonlin1212/vibe-astock/blob/3959826d653cfd8cb3e80bed73d7091de75e3d94/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Its preflight calls the same getters used by analysts, blocks a run before the day settles or when a core input is empty or degraded, and records missing optional inputs as warnings. Its market calendar and core feeds are specific to Chinese equities. A market open around the clock needs different finality and freshness rules. |

## What this project does

vibe-astock is an A-share research assistant with market data and an automated daily review. [README](https://github.com/simonlin1212/vibe-astock/blob/3959826d653cfd8cb3e80bed73d7091de75e3d94/README.md).

## Mechanism inspected

Its preflight calls the same getters used by analysts, blocks a run before the day settles or when a core input is empty or degraded, and records missing optional inputs as warnings. [Implementation](https://github.com/simonlin1212/vibe-astock/blob/3959826d653cfd8cb3e80bed73d7091de75e3d94/duanxian/preflight.py#L23-L95). [Related path](https://github.com/simonlin1212/vibe-astock/blob/3959826d653cfd8cb3e80bed73d7091de75e3d94/duanxian/data.py#L53-L86).

## Limitation that matters

Its market calendar and core feeds are specific to Chinese equities. A market open around the clock needs different finality and freshness rules. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Probe the precise sources a trading decision will consume, distinguish mandatory from optional inputs, and refuse a verdict when mandatory evidence is absent.

## Why this score

A concrete decision-quality gate with a recorded motivating failure, transferable after replacing its market-specific conditions.

## Source trail

[README](https://github.com/simonlin1212/vibe-astock/blob/3959826d653cfd8cb3e80bed73d7091de75e3d94/README.md) - [Implementation](https://github.com/simonlin1212/vibe-astock/blob/3959826d653cfd8cb3e80bed73d7091de75e3d94/duanxian/preflight.py#L23-L95) - [Related path](https://github.com/simonlin1212/vibe-astock/blob/3959826d653cfd8cb3e80bed73d7091de75e3d94/duanxian/data.py#L53-L86) - [License](https://github.com/simonlin1212/vibe-astock/blob/3959826d653cfd8cb3e80bed73d7091de75e3d94/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
