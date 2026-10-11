# nanofuzz — Timeouts in fuzz tests have their own state

**Decision question:** Can a hung property test be distinguished from a false property?

| Field | Review |
| --- | --- |
| Upstream | [nanofuzz](https://github.com/nanofuzz/nanofuzz) |
| Primary area | Testing & Verification |
| Source commit | [e2510b6e7baec18f91833471de86a3957c8c6efd](https://github.com/nanofuzz/nanofuzz/commit/e2510b6e7baec18f91833471de86a3957c8c6efd) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/nanofuzz/nanofuzz/blob/e2510b6e7baec18f91833471de86a3957c8c6efd/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its runner wraps function calls with interruption handling and represents timeout or host errors separately from normal outputs. Killing a host does not prove the tested invariant false; a fuzz harness must record timeout and command identity. |

## What this project does

A VS Code oriented TypeScript/Python fuzzing tool. [README](https://github.com/nanofuzz/nanofuzz/blob/e2510b6e7baec18f91833471de86a3957c8c6efd/README.md).

## Mechanism inspected

Its runner wraps function calls with interruption handling and represents timeout or host errors separately from normal outputs. [Implementation](https://github.com/nanofuzz/nanofuzz/blob/e2510b6e7baec18f91833471de86a3957c8c6efd/src/fuzzer/runners/AbstractRunner.ts#L46-L86).

## Limitation that matters

Killing a host does not prove the tested invariant false; a fuzz harness must record timeout and command identity. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Add TIMEOUT as an inconclusive outcome for local state-machine fuzz fixtures.

## Why this score

Transferable engineering pattern: Its runner wraps function calls with interruption handling and represents timeout or host errors separately from normal outputs. Killing a host does not prove the tested invariant false; a fuzz harness must record timeout and command identity.

## Source trail

[README](https://github.com/nanofuzz/nanofuzz/blob/e2510b6e7baec18f91833471de86a3957c8c6efd/README.md) · [Implementation](https://github.com/nanofuzz/nanofuzz/blob/e2510b6e7baec18f91833471de86a3957c8c6efd/src/fuzzer/runners/AbstractRunner.ts#L46-L86).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
