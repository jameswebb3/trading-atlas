# time-machine — clock travel has a process boundary

**Decision question:** Which clocks and processes move when a timeout test travels through time?

| Field | Review |
| --- | --- |
| Upstream | [time-machine](https://github.com/adamchainz/time-machine) |
| Primary area | Testing & Verification |
| Source commit | [6f1693aaad6a4e4cc91b0ba2c9d4bf39f08fb125](https://github.com/adamchainz/time-machine/commit/6f1693aaad6a4e4cc91b0ba2c9d4bf39f08fb125) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/adamchainz/time-machine/blob/6f1693aaad6a4e4cc91b0ba2c9d4bf39f08fb125/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Provides explicit freeze, tick and backward-shift controls. Its process-wide effect and lack of cross-process propagation make clock ownership essential when testing deadlines, workers and asynchronous trading paths. |

## Project overview

time-machine moves or freezes Python wall-clock time for tests, with explicit tick and shift controls. [Project documentation](https://github.com/adamchainz/time-machine/blob/6f1693aaad6a4e4cc91b0ba2c9d4bf39f08fb125/docs/usage.rst#L9-L15).

## Mechanism worth inspecting

The traveller returns a fixed nanosecond timestamp when ticking is disabled; otherwise it advances from the destination by real elapsed time. Shift moves the destination, including backwards. [Traveller clock](https://github.com/adamchainz/time-machine/blob/6f1693aaad6a4e4cc91b0ba2c9d4bf39f08fb125/src/time_machine/__init__.py#L224-L245); [tick/shift documentation](https://github.com/adamchainz/time-machine/blob/6f1693aaad6a4e4cc91b0ba2c9d4bf39f08fb125/docs/usage.rst#L92-L95).

## Important limit

The documentation warns that mocked time is global within the process and affects concurrent threads and asynchronous work, while other processes are unaffected. A worker, exchange simulator or monotonic deadline can therefore be on a different clock. Backward wall-clock travel should not silently reset operational deadlines. [Process boundary](https://github.com/adamchainz/time-machine/blob/6f1693aaad6a4e4cc91b0ba2c9d4bf39f08fb125/docs/usage.rst#L9-L15); [negative shift](https://github.com/adamchainz/time-machine/blob/6f1693aaad6a4e4cc91b0ba2c9d4bf39f08fb125/docs/usage.rst#L286-L307).

## Questions to take into your own design

- Do civil timestamps and monotonic timeout deadlines have separate injected clocks?
- Does a multiprocess test explicitly synchronize the simulated clock rather than assuming a global patch?

## Why this score for a trading system

3/5: a valuable clock-boundary reference for deterministic timeout tests, requiring explicit process and deadline design.

**Scope of this review:** Traveller timestamp and shift behavior plus documented process boundaries; native patch internals were not fully audited.
