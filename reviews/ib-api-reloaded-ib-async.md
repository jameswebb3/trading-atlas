# ib_async — Can an order be filled before its commission is known

**Decision question:** Can an order be filled before its commission is known?

| Field | Review |
| --- | --- |
| Upstream | [ib_async](https://github.com/ib-api-reloaded/ib_async) |
| Primary area | Execution & Exchange Integration |
| Source commit | [ab629f34c1823ea4c1542f32f07377208a86bdfd](https://github.com/ib-api-reloaded/ib_async/commit/ab629f34c1823ea4c1542f32f07377208a86bdfd) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-2-Clause](https://github.com/ib-api-reloaded/ib_async/blob/ab629f34c1823ea4c1542f32f07377208a86bdfd/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Separates order completion, individual executions and subsequent commission reports. Useful for execution accounting that must remain provisional until costs arrive; the inspected deduplication path is in memory. |

## Project overview

A Python interface to Interactive Brokers that brings order, execution and account callbacks into an asynchronous application. [Project documentation](https://github.com/ib-api-reloaded/ib_async/blob/ab629f34c1823ea4c1542f32f07377208a86bdfd/README.md#L9-L25).

## Mechanism worth inspecting

Order status changes emit a filled event independently of execution details. Executions are stored once per execution ID; a later commission callback updates the matching fill and emits a separate event. This is a useful reference for distinguishing execution completeness from cost completeness. [Status, execution and commission handlers](https://github.com/ib-api-reloaded/ib_async/blob/ab629f34c1823ea4c1542f32f07377208a86bdfd/ib_async/wrapper.py#L735-L865).

## Important limit

The fill store is an in-memory map in this inspected path. The code does not establish a durable deduplication guarantee across application restarts, and commission callbacks without a matching fill are ignored. [Matching boundary](https://github.com/ib-api-reloaded/ib_async/blob/ab629f34c1823ea4c1542f32f07377208a86bdfd/ib_async/wrapper.py#L821-L868). [In-memory reset](https://github.com/ib-api-reloaded/ib_async/blob/ab629f34c1823ea4c1542f32f07377208a86bdfd/ib_async/wrapper.py#L318-L320).

## Questions to take into your own design

- Can a fill be reported as executed while its costs remain explicitly pending?
- What durable execution key prevents replayed fills from being counted twice after restart?

## Why this score for a trading system

4/5: execution IDs and independently arriving commissions address a concrete trading accounting boundary visible in source.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
