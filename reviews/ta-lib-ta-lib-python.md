# TA-Lib Python — Can a forming-bar preview change the committed state of an indicator

**Decision question:** Can a forming-bar preview change the committed state of an indicator?

| Field | Review |
| --- | --- |
| Upstream | [TA-Lib Python](https://github.com/TA-Lib/ta-lib-python) |
| Primary area | Signals & Models |
| Source commit | [8f5cadcd83091ffbbfd30a117fdd92b87fa7fc2f](https://github.com/TA-Lib/ta-lib-python/commit/8f5cadcd83091ffbbfd30a117fdd92b87fa7fc2f) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-2-Clause](https://github.com/TA-Lib/ta-lib-python/blob/8f5cadcd83091ffbbfd30a117fdd92b87fa7fc2f/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Separates committed closed-bar updates from forming-bar previews and independent copies. Useful for feature pipelines that must inspect provisional prices without contaminating the next closed-bar value. |

## Project overview

A Cython wrapper for TA-Lib, with a handle-based streaming API described in its current documentation. [Project documentation](https://github.com/TA-Lib/ta-lib-python/blob/8f5cadcd83091ffbbfd30a117fdd92b87fa7fc2f/README.md#L11-L20).

## Mechanism worth inspecting

The SMA stream wrapper exposes update, peek, value and copy as separate operations, delegating to the corresponding C API calls. Initialization also checks history and lookback before opening a handle. The README states that peek evaluates a forming value without committing it. [Stream implementation](https://github.com/TA-Lib/ta-lib-python/blob/8f5cadcd83091ffbbfd30a117fdd92b87fa7fc2f/talib/_stream.pxi#L19455-L19529); [documented preview contract](https://github.com/TA-Lib/ta-lib-python/blob/8f5cadcd83091ffbbfd30a117fdd92b87fa7fc2f/README.md#L535-L557).

## Important limit

This review inspected the wrapper, not the C implementations of Peek or Clone. Their behavioral guarantees were not independently verified. A handle is not by itself a durable checkpoint for process restart.

## Questions to take into your own design

- Can previewing a forming bar leave the next closed-bar result unchanged?
- Does restoring an indicator reproduce its exact initialization and committed history?

## Why this score for a trading system

3/5: a concrete direct interface for provisional-versus-committed features, with delegated behavior and restart handling outside this review.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
