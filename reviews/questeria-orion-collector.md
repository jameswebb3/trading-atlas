# orion-collector - Do the tape-integrity tests cover the format the collector writes?

**Decision question:** Do the tape-integrity tests cover the format the collector writes?

| Field | Review |
| --- | --- |
| Upstream | [Questeria/orion-collector](https://github.com/Questeria/orion-collector) |
| Primary area | Market Data & Ingestion |
| Source commit | [57498d6547f5b6ba5706faabb06be9b123d231fc](https://github.com/Questeria/orion-collector/commit/57498d6547f5b6ba5706faabb06be9b123d231fc) |
| Reviewed | 2026-10-11 |
| Declared license | No root license file found at the reviewed commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Checksums unified tape records and tracks backpressure drops, but its integrity tests use a different crc32 record format from the runtime crc tape. A passing fixture test does not prove the writer and health checker agree on actual records. |

## What this project does

A Kalshi and Coinbase WebSocket recorder with a unified JSONL tape, sequence monitoring, backpressure counters and a separate health checker.

## Mechanism inspected

The runtime writer serializes each raw message with a crc field computed on its escaped payload. The health checker reads that field and recomputes CRC over the parsed raw payload. The writer also counts dropped messages when its queue is full.

## Limitation that matters

The inspected integrity tests use a fixture with a crc32 field and hash the entire record minus that field, while the runtime tape uses crc and hashes only the raw payload. Those tests do not exercise the writer/health-check contract. CRC also detects byte corruption, not omitted messages; a dropped counter remains necessary. No root license file was found.

## Practical check for a trading system

Test the exact serialized record emitted by the collector against the production verifier, and expose queue drops separately from checksummed-record validity.

## Why this score

2/5 because The tape format and backpressure accounting are directly relevant, but the inspected test-schema mismatch weakens confidence in the claimed integrity check.

## Source trail

[README collector design](https://github.com/Questeria/orion-collector/blob/57498d6547f5b6ba5706faabb06be9b123d231fc/README.md#L85); [Runtime tape CRC](https://github.com/Questeria/orion-collector/blob/57498d6547f5b6ba5706faabb06be9b123d231fc/orion_collector.py#L1497); [Health verifier](https://github.com/Questeria/orion-collector/blob/57498d6547f5b6ba5706faabb06be9b123d231fc/health_check.py#L166); [Test fixture schema](https://github.com/Questeria/orion-collector/blob/57498d6547f5b6ba5706faabb06be9b123d231fc/tests/test_tape_integrity.py#L25); [Drop counter](https://github.com/Questeria/orion-collector/blob/57498d6547f5b6ba5706faabb06be9b123d231fc/orion_collector.py#L2212).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
