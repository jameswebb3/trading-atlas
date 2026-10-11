# QuickFIX/Go — Recovery survives a timeout

**Decision question:** Does a timeout preserve the unfinished recovery state?

| Field | Review |
| --- | --- |
| Upstream | [QuickFIX/Go](https://github.com/quickfixgo/quickfix) |
| Primary area | Execution & Exchange Integration |
| Source commit | [56e2b02e927d6961583c048b738261c6520db2cf](https://github.com/quickfixgo/quickfix/commit/56e2b02e927d6961583c048b738261c6520db2cf) |
| Reviewed | 2026-09-27 |
| Declared license | [QuickFIX Software License 1.0](https://github.com/quickfixgo/quickfix/blob/56e2b02e927d6961583c048b738261c6520db2cf/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation, and relevant test code read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | The resend state wraps itself in a pending-timeout state instead of discarding recovery. This is FIX session recovery, not order reconciliation for every exchange. |

## Project overview

Go implementation of the FIX protocol, with persistent session state and message validation. [Documentation](https://github.com/quickfixgo/quickfix/blob/56e2b02e927d6961583c048b738261c6520db2cf/README.md).

## Mechanism worth inspecting

The resend state wraps itself in a pending-timeout state instead of discarding recovery. Buffered messages are released only when their sequence matches the next expected value. [Source](https://github.com/quickfixgo/quickfix/blob/56e2b02e927d6961583c048b738261c6520db2cf/resend_state.go#L29-L91).

## Important limit

This is FIX session recovery, not order reconciliation for every exchange. A contiguous message sequence does not establish complete account fills. [Evidence 1](https://github.com/quickfixgo/quickfix/blob/56e2b02e927d6961583c048b738261c6520db2cf/resend_state.go#L29-L91). [Evidence 2](https://github.com/quickfixgo/quickfix/blob/56e2b02e927d6961583c048b738261c6520db2cf/resend_state_test.go#L52-L112).

## Questions to take into your own design

- After a timeout, can recovery resume without skipping the first missing message?
- Which separate account evidence confirms quantities and fills?

## Why this score for a trading system

A directly relevant execution-protocol example with explicit recovery tests; translating it to another venue still needs a venue-specific contract.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. Relevant tests were read, not executed.
