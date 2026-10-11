# Expecto — Ignored tests are an explicit result

**Decision question:** Can a green summary conceal tests that were never run?

| Field | Review |
| --- | --- |
| Upstream | [Expecto](https://github.com/haf/expecto) |
| Primary area | Testing & Verification |
| Source commit | [cec2c63c8d77c6c21bf7e35d903020f74ddc1cea](https://github.com/haf/expecto/commit/cec2c63c8d77c6c21bf7e35d903020f74ddc1cea) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/haf/expecto/blob/cec2c63c8d77c6c21bf7e35d903020f74ddc1cea/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The implementation models Passed, Ignored, Failed and Error separately and reports their counts. Ignore/focus policy still determines coverage. |

## Project overview

F#/.NET test framework supporting asynchronous, parallel, stress and property tests. [Documentation](https://github.com/haf/expecto/blob/cec2c63c8d77c6c21bf7e35d903020f74ddc1cea/README.md).

## Mechanism worth inspecting

The implementation models Passed, Ignored, Failed and Error separately and reports their counts. The public configuration can fail a run when focused tests are present. [Source](https://github.com/haf/expecto/blob/cec2c63c8d77c6c21bf7e35d903020f74ddc1cea/Expecto/Expecto.Impl.fs#L38-L69).

## Important limit

Ignore/focus policy still determines coverage. A successful exit should not be used as proof that the required suite ran unless the caller also checks the expected test set and ignored count. [Evidence 1](https://github.com/haf/expecto/blob/cec2c63c8d77c6c21bf7e35d903020f74ddc1cea/Expecto/Expecto.Impl.fs#L38-L69). [Evidence 2](https://github.com/haf/expecto/blob/cec2c63c8d77c6c21bf7e35d903020f74ddc1cea/Expecto/Expecto.Impl.fs#L116-L156). [Evidence 3](https://github.com/haf/expecto/blob/cec2c63c8d77c6c21bf7e35d903020f74ddc1cea/Expecto/Expecto.fs#L418-L419).

## Questions to take into your own design

- Does the admission gate reject missing required tests and unexpected ignores?
- Is an accidentally focused suite a failed verification?

## Why this score for a trading system

A useful test-receipt distinction already widely available, with little reason to add a CLR testing framework.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
