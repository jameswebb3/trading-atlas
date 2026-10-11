# Hyperliquid Node — Ready means current, not just running

**Decision question:** How can a node be live but unusable as a market-data source?

| Field | Review |
| --- | --- |
| Upstream | [BuckshotCapital/hyperliquid-node](https://github.com/BuckshotCapital/hyperliquid-node) |
| Primary area | Execution & Exchange Integration |
| Source commit | [8e3ab37b4e134609422f3cfa6f061d65691ecce4](https://github.com/BuckshotCapital/hyperliquid-node/commit/8e3ab37b4e134609422f3cfa6f061d65691ecce4) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Its monitor distinguishes process liveness from readiness by checking node response and clock proximity. Clock proximity does not establish complete event history, and the node plus pruning requires substantial operational resources. |

## What this project does

A deployment and bootstrap repository for a non-validator Hyperliquid node. [Project README](https://github.com/BuckshotCapital/hyperliquid-node/blob/8e3ab37b4e134609422f3cfa6f061d65691ecce4/README.md#L12).

## Mechanism inspected

Its monitor distinguishes process liveness from readiness by checking node response and clock proximity. [Implementation](https://github.com/BuckshotCapital/hyperliquid-node/blob/8e3ab37b4e134609422f3cfa6f061d65691ecce4/hl-bootstrap/src/monitor/server.rs#L22). [Related source 1](https://github.com/BuckshotCapital/hyperliquid-node/blob/8e3ab37b4e134609422f3cfa6f061d65691ecce4/README.md#L43). [Related source 2](https://github.com/BuckshotCapital/hyperliquid-node/blob/8e3ab37b4e134609422f3cfa6f061d65691ecce4/notes.md#L31).

## Limitation that matters

Clock proximity does not establish complete event history, and the node plus pruning requires substantial operational resources. This is a source review, not a runtime or security test.

## Practical check for a trading system

Gate any local feed on sync height, freshness, and missing-range recovery, not only a responsive process.

## Why this score

A direct readiness pattern, but self-hosting cost and data-completeness limits are material.

## Source trail

[README](https://github.com/BuckshotCapital/hyperliquid-node/blob/8e3ab37b4e134609422f3cfa6f061d65691ecce4/README.md#L12); [Implementation](https://github.com/BuckshotCapital/hyperliquid-node/blob/8e3ab37b4e134609422f3cfa6f061d65691ecce4/hl-bootstrap/src/monitor/server.rs#L22); [Related source 1](https://github.com/BuckshotCapital/hyperliquid-node/blob/8e3ab37b4e134609422f3cfa6f061d65691ecce4/README.md#L43); [Related source 2](https://github.com/BuckshotCapital/hyperliquid-node/blob/8e3ab37b4e134609422f3cfa6f061d65691ecce4/notes.md#L31).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
