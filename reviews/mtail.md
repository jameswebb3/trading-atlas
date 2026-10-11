# A log-derived metric can miss the incident it claims to count

**Decision question:** What does a live log tailer miss after a restart or truncation?

| Field | Review |
| --- | --- |
| Upstream | [mtail](https://github.com/google/mtail) |
| Primary area | Operations & Observability |
| Source commit | [4c7e0e1174ac1ead032efe28d86428bbbe0ae145](https://github.com/google/mtail/commit/4c7e0e1174ac1ead032efe28d86428bbbe0ae145) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/google/mtail/blob/4c7e0e1174ac1ead032efe28d86428bbbe0ae145/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | mtail turns log patterns into metrics, but its own stream code warns that truncation can lose unread lines and its live default starts at end of file. For trading operations, that is a useful reminder to separate real-time alert metrics from a durable order and fill record. |

## Mechanism worth inspecting

The [README](https://github.com/google/mtail/blob/4c7e0e1174ac1ead032efe28d86428bbbe0ae145/README.md#L11-L29) positions mtail as log-to-metric extraction. The [programming guide](https://github.com/google/mtail/blob/4c7e0e1174ac1ead032efe28d86428bbbe0ae145/docs/Programming-Guide.md#L135-L167) shows pattern-based matching. The [file stream implementation](https://github.com/google/mtail/blob/4c7e0e1174ac1ead032efe28d86428bbbe0ae145/internal/tailer/logstream/filestream.go#L22-L80) warns about truncation loss and begins live streams at end of file unless configured for a one-shot read.

## Important limit

A metric built from logs inherits gaps, format changes, and duplicate-line risks. It cannot replace reconciliation against exchange orders, fills, and account state.

## Questions to take into your own design

- Are pre-start log lines counted or intentionally excluded?
- How are rotation, truncation, and replay duplicates detected?

## Why this score for a trading system

2/5: The source exposes a real observability blind spot applicable to execution monitoring. The tool is a general log parser; its metrics are not a durable trading ledger and do not establish exchange truth.

**Scope of this review:** We read the README, programming guide, and file-stream source.
