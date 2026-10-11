# Higher-timeframe values can differ between history and the live last bar

**Decision question:** Does lookahead-off mean the same data is visible in replay and real time?

| Field | Review |
| --- | --- |
| Upstream | [PineTS](https://github.com/LuxAlgo/PineTS) |
| Primary area | Signals & Models |
| Source commit | [1f65fa2dc1d46a9b254163599030f4bc27580922](https://github.com/LuxAlgo/PineTS/commit/1f65fa2dc1d46a9b254163599030f4bc27580922) |
| Reviewed | 2026-09-26 |
| Declared license | [AGPL-3.0-only; commercial option](https://github.com/LuxAlgo/PineTS/blob/1f65fa2dc1d46a9b254163599030f4bc27580922/LICENSE) |
| Review depth | 3/3: documentation, relevant source, and focused tests read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | PineTS selects a completed higher-timeframe bar for historical lookahead-off requests, but can return the developing bar in real time. That difference matters when porting indicators to automated trading. The inspected edge-case test checks output existence and length, not numerical equivalence between modes. |

## Mechanism worth inspecting

The [README](https://github.com/LuxAlgo/PineTS/blob/1f65fa2dc1d46a9b254163599030f4bc27580922/README.md#L32-L38) describes a Pine-compatible runtime; the [architecture guide](https://github.com/LuxAlgo/PineTS/blob/1f65fa2dc1d46a9b254163599030f4bc27580922/docs/architecture/specifics/request-security.md#L13-L20) explains secondary contexts. The [index selector](https://github.com/LuxAlgo/PineTS/blob/1f65fa2dc1d46a9b254163599030f4bc27580922/src/namespaces/request/utils/findSecContextIdx.ts#L11-L30) distinguishes lookahead, historical bar completion, and real-time selection. The [test](https://github.com/LuxAlgo/PineTS/blob/1f65fa2dc1d46a9b254163599030f4bc27580922/tests/namespaces/request-edge-cases.test.ts#L78-L99) does not assert the expected numerical difference.

## Important limit

This is a source observation about the selector and one test, not a verified claim of full TradingView compatibility. Developing bars can change before closing; exact data, timezone, alignment, and restart semantics need independent comparison.

## Questions to take into your own design

- Is the live signal allowed to use a higher-timeframe bar that can still change?
- Do boundary fixtures assert expected values rather than just nonempty plots?

## Why this score for a trading system

4/5: The historical-versus-real-time selection branch directly exposes a consequential trading timing contract, while compatibility remains unverified.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
