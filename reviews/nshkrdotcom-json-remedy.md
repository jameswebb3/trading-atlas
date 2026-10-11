# JSON Remedy - Should a repaired market payload be treated as the original event?

**Decision question:** Should a repaired market payload be treated as the original event?

| Field | Review |
| --- | --- |
| Upstream | [nshkrdotcom/json_remedy](https://github.com/nshkrdotcom/json_remedy) |
| Primary area | Data Quality & Lineage |
| Source commit | [1bce906bb35130155379e08ddfb2d5f5e4616f58](https://github.com/nshkrdotcom/json_remedy/commit/1bce906bb35130155379e08ddfb2d5f5e4616f58) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The parser rewrites unquoted keys and returns both repaired bytes and a list of repair descriptions. The output is no longer the received payload; consumers that discard repair metadata lose evidence of a malformed upstream event. |

## What this project does

An Elixir JSON repair library.

## Mechanism inspected

The parser rewrites unquoted keys and returns both repaired bytes and a list of repair descriptions.

## Limitation that matters

The output is no longer the received payload; consumers that discard repair metadata lose evidence of a malformed upstream event.

## Practical check for a trading system

Preserve raw bytes and reject or quarantine repaired market events before canonical ingestion.

## Why this score

2/5. The repair log is inspectable, but heuristic repair is unsafe as a silent feed normalizer.

## Source trail

[README](https://github.com/nshkrdotcom/json_remedy/blob/1bce906bb35130155379e08ddfb2d5f5e4616f58/README.md#L1); [lib/json_remedy/layer3/optimized/binary_parser.ex](https://github.com/nshkrdotcom/json_remedy/blob/1bce906bb35130155379e08ddfb2d5f5e4616f58/lib/json_remedy/layer3/optimized/binary_parser.ex#L12); [lib/json_remedy/layer3/optimized/binary_parser.ex](https://github.com/nshkrdotcom/json_remedy/blob/1bce906bb35130155379e08ddfb2d5f5e4616f58/lib/json_remedy/layer3/optimized/binary_parser.ex#L22); [Root license](https://github.com/nshkrdotcom/json_remedy/blob/1bce906bb35130155379e08ddfb2d5f5e4616f58/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
