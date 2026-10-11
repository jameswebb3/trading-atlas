# OsEngine — Reject invalid orders in an adapter test

**Decision question:** Will a connected exchange reject zero-size orders within a bounded wait?

| Field | Review |
| --- | --- |
| Upstream | [OsEngine](https://github.com/AlexWan/OsEngine) |
| Primary area | Testing & Verification |
| Source commit | [fbd8230e6adebf35d86ec4ab2ce326bccd4e68ba](https://github.com/AlexWan/OsEngine/commit/fbd8230e6adebf35d86ec4ab2ce326bccd4e68ba) |
| Reviewed | 2026-10-06 |
| Declared license | [Custom EULA](https://github.com/AlexWan/OsEngine/blob/fbd8230e6adebf35d86ec4ab2ce326bccd4e68ba/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The tester subscribes to order events, sends an intentionally zero-volume order and fails if no reject event arrives before its deadline. The test covers one rejection path; it does not prove partial fills, cancel/ACK races or Hyperliquid semantics. The inspected branch also contains a suspect null-and-count check. |

## What this project does

A large multi-venue trading platform whose server tester exercises orders and market depth. [README](https://github.com/AlexWan/OsEngine/blob/fbd8230e6adebf35d86ec4ab2ce326bccd4e68ba/README.md).

## Mechanism inspected

The tester subscribes to order events, sends an intentionally zero-volume order and fails if no reject event arrives before its deadline. [Implementation](https://github.com/AlexWan/OsEngine/blob/fbd8230e6adebf35d86ec4ab2ce326bccd4e68ba/project/OsEngine/Robots/AutoTestBots/ServerTests/Orders_1_FakeOrders.cs#L176-L209).

## Limitation that matters

The test covers one rejection path; it does not prove partial fills, cancel/ACK races or Hyperliquid semantics. The inspected branch also contains a suspect null-and-count check. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Add an offline adapter fixture for invalid size and missing rejection, keeping timeout distinct from accepted or filled.

## Why this score

Direct trading-system relevance: The tester subscribes to order events, sends an intentionally zero-volume order and fails if no reject event arrives before its deadline. The test covers one rejection path; it does not prove partial fills, cancel/ACK races or Hyperliquid semantics. The inspected branch also contains a suspect null-and-count check.

## Source trail

[README](https://github.com/AlexWan/OsEngine/blob/fbd8230e6adebf35d86ec4ab2ce326bccd4e68ba/README.md) · [Implementation](https://github.com/AlexWan/OsEngine/blob/fbd8230e6adebf35d86ec4ab2ce326bccd4e68ba/project/OsEngine/Robots/AutoTestBots/ServerTests/Orders_1_FakeOrders.cs#L176-L209).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
