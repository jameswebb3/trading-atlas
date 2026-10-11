# IB-insync — How can an unchanged order status still acknowledge a modification

**Decision question:** How can an unchanged order status still acknowledge a modification?

| Field | Review |
| --- | --- |
| Upstream | [IB-insync](https://github.com/erdewit/ib_insync) |
| Primary area | Execution & Exchange Integration |
| Source commit | [ef5ea29e44e0c40bbadbc16c2281b3ac58aa4a40](https://github.com/erdewit/ib_insync/commit/ef5ea29e44e0c40bbadbc16c2281b3ac58aa4a40) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-2-Clause](https://github.com/erdewit/ib_insync/blob/ef5ea29e44e0c40bbadbc16c2281b3ac58aa4a40/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Recognizes modification acknowledgements even when the status string is unchanged, while suppressing repeated status events. A historical comparison reference; ib_async provides the same inspected pattern. |

## Project overview

An Interactive Brokers interface built around asyncio, automatic synchronization and a linear application API. [Project documentation](https://github.com/erdewit/ib_insync/blob/ef5ea29e44e0c40bbadbc16c2281b3ac58aa4a40/README.rst#L17-L28).

## Mechanism worth inspecting

The order-status handler compares all incoming status fields with the stored record. An unchanged Submitted status becomes a Modified log entry when the preceding trade log entry was Modify; unrelated repeated statuses do not emit another event. [Status comparison and modification ACK](https://github.com/erdewit/ib_insync/blob/ef5ea29e44e0c40bbadbc16c2281b3ac58aa4a40/ib_insync/wrapper.py#L463-L501).

## Important limit

This is a specific log-based interpretation of Interactive Brokers callbacks, not a universal order protocol. The maintained ib_async fork contains the same pattern, so this historical implementation adds little beyond comparison. [Equivalent branch](https://github.com/erdewit/ib_insync/blob/ef5ea29e44e0c40bbadbc16c2281b3ac58aa4a40/ib_insync/wrapper.py#L479-L489); [project notice](https://github.com/erdewit/ib_insync/blob/ef5ea29e44e0c40bbadbc16c2281b3ac58aa4a40/README.rst#L3-L12).

## Questions to take into your own design

- Does an unchanged status acknowledge a new order generation or repeat an old event?
- Is acknowledgement tied to a request identity rather than only the last log message?

## Why this score for a trading system

2/5: the mechanism is directly relevant, but duplicates the newer fork and depends on broker-specific callback semantics.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
