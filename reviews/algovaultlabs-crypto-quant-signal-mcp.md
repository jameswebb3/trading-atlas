# crypto-quant-signal-mcp — Shared exchange budget before a request

**Decision question:** Can concurrent data consumers exhaust an exchange weight budget without a common gate?

| Field | Review |
| --- | --- |
| Upstream | [AlgoVaultLabs/crypto-quant-signal-mcp](https://github.com/AlgoVaultLabs/crypto-quant-signal-mcp) |
| Primary area | Market Data & Ingestion |
| Source commit | [0b1ea5d0288f6a69640640f0d2965163e71bd79c](https://github.com/AlgoVaultLabs/crypto-quant-signal-mcp/commit/0b1ea5d0288f6a69640640f0d2965163e71bd79c) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/AlgoVaultLabs/crypto-quant-signal-mcp/blob/0b1ea5d0288f6a69640640f0d2965163e71bd79c/LICENSE)) |
| Review depth | 3/3: README and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The adapter routes /info calls through one fetch wrapper; the wrapper acquires an estimated venue weight before network I/O, and tests exercise reserve and concurrent acquisition. The adapter cache is process-local; a shared budget only governs writers that use the same ledger. README performance claims are not independently verified. |

## What this project does

Multi-venue crypto signal server with a dedicated Hyperliquid adapter and an upstream weight-budget implementation. [README](https://github.com/AlgoVaultLabs/crypto-quant-signal-mcp/blob/0b1ea5d0288f6a69640640f0d2965163e71bd79c/README.md).

## Mechanism inspected

The adapter routes /info calls through one fetch wrapper; the wrapper acquires an estimated venue weight before network I/O, and tests exercise reserve and concurrent acquisition. [Implementation](https://github.com/AlgoVaultLabs/crypto-quant-signal-mcp/blob/0b1ea5d0288f6a69640640f0d2965163e71bd79c/src/lib/adapters/_upstream-fetch.ts#L153-L195). [Test source](https://github.com/AlgoVaultLabs/crypto-quant-signal-mcp/blob/0b1ea5d0288f6a69640640f0d2965163e71bd79c/tests/unit/upstream-weight-budget.test.ts#L117-L156).

## Limitation that matters

The adapter cache is process-local; a shared budget only governs writers that use the same ledger. README performance claims are not independently verified. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Keep a single explicit quota ledger for collector and research calls; reserve capacity for priority paths and emit a typed rate-limit outcome instead of treating 429 as empty data.

## Why this score

The adapter routes /info calls through one fetch wrapper; the wrapper acquires an estimated venue weight before network I/O, and tests exercise reserve and concurrent acquisition. The adapter cache is process-local; a shared budget only governs writers that use the same ledger. README performance claims are not independently verified.

## Source trail

[README](https://github.com/AlgoVaultLabs/crypto-quant-signal-mcp/blob/0b1ea5d0288f6a69640640f0d2965163e71bd79c/README.md) · [Implementation](https://github.com/AlgoVaultLabs/crypto-quant-signal-mcp/blob/0b1ea5d0288f6a69640640f0d2965163e71bd79c/src/lib/adapters/_upstream-fetch.ts#L153-L195) · [Test source](https://github.com/AlgoVaultLabs/crypto-quant-signal-mcp/blob/0b1ea5d0288f6a69640640f0d2965163e71bd79c/tests/unit/upstream-weight-budget.test.ts#L117-L156) · [License](https://github.com/AlgoVaultLabs/crypto-quant-signal-mcp/blob/0b1ea5d0288f6a69640640f0d2965163e71bd79c/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
