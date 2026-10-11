# flow-crew - Bind exceptions to the artifact inspected

**Decision question:** Can a test exception survive after a producer replaces the file it was based on?

| Field | Review |
| --- | --- |
| Upstream | [cuibuaa/flow-crew](https://github.com/cuibuaa/flow-crew) |
| Primary area | Testing & Verification |
| Source commit | [6ec82704b9f2a3f7ede2b1712253133ea4b5c695](https://github.com/cuibuaa/flow-crew/commit/6ec82704b9f2a3f7ede2b1712253133ea4b5c695) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/cuibuaa/flow-crew/blob/6ec82704b9f2a3f7ede2b1712253133ea4b5c695/LICENSE)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | A variance check rejects degenerate numeric arrays and a narrow schema exception is admitted only when its stored SHA-256 still matches the inspected artifact Variance cannot detect wrong but variable numbers. The schema exception demotes a failed check only for a narrow static pattern; a trading quality gate should require explicit owner approval for such exceptions |

## What this project does

An agent workflow engine with explicit reality checks [README](https://github.com/cuibuaa/flow-crew/blob/6ec82704b9f2a3f7ede2b1712253133ea4b5c695/README.md).

## Mechanism inspected

A variance check rejects degenerate numeric arrays and a narrow schema exception is admitted only when its stored SHA-256 still matches the inspected artifact [Implementation](https://github.com/cuibuaa/flow-crew/blob/6ec82704b9f2a3f7ede2b1712253133ea4b5c695/src/reality-gate/checks/variance-floor.ts#L10-L29). [Related path](https://github.com/cuibuaa/flow-crew/blob/6ec82704b9f2a3f7ede2b1712253133ea4b5c695/src/reality-gate/versioned-json-admission.ts#L74-L115).

## Limitation that matters

Variance cannot detect wrong but variable numbers. The schema exception demotes a failed check only for a narrow static pattern; a trading quality gate should require explicit owner approval for such exceptions This review covers the pinned source paths, not independent runtime behavior.

## Practical check for a trading system

Bind any waived battery failure to exact input hash and test version. Recheck after the producer writes, and record the original failed result

## Why this score

The source shows a defensible exact-byte binding and a failure-mode example, with a narrow domain-specific exception

## Source trail

[README](https://github.com/cuibuaa/flow-crew/blob/6ec82704b9f2a3f7ede2b1712253133ea4b5c695/README.md) - [Implementation](https://github.com/cuibuaa/flow-crew/blob/6ec82704b9f2a3f7ede2b1712253133ea4b5c695/src/reality-gate/checks/variance-floor.ts#L10-L29) - [Related path](https://github.com/cuibuaa/flow-crew/blob/6ec82704b9f2a3f7ede2b1712253133ea4b5c695/src/reality-gate/versioned-json-admission.ts#L74-L115) - [License](https://github.com/cuibuaa/flow-crew/blob/6ec82704b9f2a3f7ede2b1712253133ea4b5c695/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
