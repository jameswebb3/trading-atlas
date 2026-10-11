# Faust Streaming — Can processing later messages move a checkpoint past unfinished earlier work

**Decision question:** Can processing later messages move a checkpoint past unfinished earlier work?

| Field | Review |
| --- | --- |
| Upstream | [Faust Streaming](https://github.com/faust-streaming/faust) |
| Primary area | Data Quality & Lineage |
| Source commit | [61f3c556f3caf7d9816efc8fb7aaf256493b275b](https://github.com/faust-streaming/faust/commit/61f3c556f3caf7d9816efc8fb7aaf256493b275b) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/faust-streaming/faust/blob/61f3c556f3caf7d9816efc8fb7aaf256493b275b/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Advances consumer progress through contiguous acknowledgements rather than the latest completed message alone. Useful for asynchronous collectors where completion order can differ from input order. |

## Project overview

A fork of a Python stream-processing library, with stream and consumer APIs. [Project documentation](https://github.com/faust-streaming/faust/blob/61f3c556f3caf7d9816efc8fb7aaf256493b275b/README.md#L1-L12).

## Mechanism worth inspecting

The consumer tracks acknowledged offsets separately. Its new-offset calculation sorts acknowledgements, takes the first consecutive batch and commits the next offset after that batch, while returning no advance for a gap after a previously committed offset. It also incorporates tracked source-offset gaps. [Contiguous-progress calculation](https://github.com/faust-streaming/faust/blob/61f3c556f3caf7d9816efc8fb7aaf256493b275b/faust/transport/consumer.py#L1097-L1151); [acknowledgement bookkeeping](https://github.com/faust-streaming/faust/blob/61f3c556f3caf7d9816efc8fb7aaf256493b275b/faust/transport/consumer.py#L825-L850).

## Important limit

The inspected algorithm's gap bookkeeping is part of its transport contract, not a generic permission to skip missing data. External side effects and restarts still need idempotence and coverage evidence.

## Questions to take into your own design

- Can a later completed task advance progress past an unfinished earlier input?
- Which gaps are source-defined and which represent missing work?

## Why this score for a trading system

3/5: an inspectable transferable checkpoint rule for out-of-order completion, requiring adaptation to the source's sequence semantics.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
