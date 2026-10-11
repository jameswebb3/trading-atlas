# pytest-xdist — a replacement worker is not a successful test

**Decision question:** How is a test that crashes its worker represented in the final evidence?

| Field | Review |
| --- | --- |
| Upstream | [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) |
| Primary area | Testing & Verification |
| Source commit | [eba6a4475eb8697fc476357ff54d7b8b948781cf](https://github.com/pytest-dev/pytest-xdist/commit/eba6a4475eb8697fc476357ff54d7b8b948781cf) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/pytest-dev/pytest-xdist/blob/eba6a4475eb8697fc476357ff54d7b8b948781cf/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Separates worker replacement from test success and reports the active crash item as failed. A useful reference for preserving failed attempts when a parallel test or research pool recovers. |

## Project overview

pytest-xdist distributes pytest tests across worker processes and manages worker failures. [Project documentation](https://github.com/pytest-dev/pytest-xdist/blob/eba6a4475eb8697fc476357ff54d7b8b948781cf/README.rst#L22-L29).

## Mechanism worth inspecting

On worker loss, the controller removes the worker from scheduling, identifies its active crash item and emits a failed test report. It separately counts crashes and decides whether to replace the worker or stop. [Worker loss](https://github.com/pytest-dev/pytest-xdist/blob/eba6a4475eb8697fc476357ff54d7b8b948781cf/src/xdist/dsession.py#L245-L274); [failed crash report](https://github.com/pytest-dev/pytest-xdist/blob/eba6a4475eb8697fc476357ff54d7b8b948781cf/src/xdist/dsession.py#L439-L459).

## Important limit

Worker replacement is operational recovery, not proof that the crashed test completed. Hooks can affect crash reporting and scheduling. Parallel research runs need attempt identities and explicit terminal evidence rather than treating an active replacement pool as a complete successful batch.

## Questions to take into your own design

- Does a recovered worker preserve the original failed attempt in the run ledger?
- Can the batch finish without a terminal result for every planned test ID?

## Why this score for a trading system

2/5: a useful worker-failure accounting reference, but ordinary parallel test execution adds limited trading-specific value beyond an existing complete-run gate.

**Scope of this review:** Controller crash handling and restart limits; scheduler variants were not exhaustively reviewed.
