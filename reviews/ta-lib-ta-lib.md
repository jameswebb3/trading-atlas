# TA-Lib Core — Can evaluating only a late slice change an EMA value at the same bar

**Decision question:** Can evaluating only a late slice change an EMA value at the same bar?

| Field | Review |
| --- | --- |
| Upstream | [TA-Lib Core](https://github.com/TA-Lib/ta-lib) |
| Primary area | Signals & Models |
| Source commit | [5c85f0ddd3862f1748bc4d10ca8c702780f828f7](https://github.com/TA-Lib/ta-lib/commit/5c85f0ddd3862f1748bc4d10ca8c702780f828f7) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/TA-Lib/ta-lib/blob/5c85f0ddd3862f1748bc4d10ca8c702780f828f7/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Exposes how EMA warm-up and the requested start range determine the recursion seed. Useful for checking that batch, rolling-window and replay features use the same historical initialization. |

## Project overview

The core C implementation of TA-Lib's technical-analysis functions. [Project documentation](https://github.com/TA-Lib/ta-lib/blob/5c85f0ddd3862f1748bc4d10ca8c702780f828f7/README.md#L5-L8).

## Mechanism worth inspecting

The EMA implementation moves the start index past the lookback, initializes the recursion from a mean of the preceding period and then advances to the requested output. Its seeding study explicitly discusses start-dependent reseeding and unstable-period settings. [Lookback and initialization](https://github.com/TA-Lib/ta-lib/blob/5c85f0ddd3862f1748bc4d10ca8c702780f828f7/src/ta_func/ta_EMA.c#L105-L164); [seeding study](https://github.com/TA-Lib/ta-lib/blob/5c85f0ddd3862f1748bc4d10ca8c702780f828f7/docs/studies/ema-seeding/README.md#L22-L39).

## Important limit

A shared formula name does not establish identical initialization history. The study's runtime findings are upstream reports, not independently replicated here; the inspected source supports the need to record initialization and compare equal histories.

## Questions to take into your own design

- Do batch and incremental calculations share the same initialization history?
- Are lookback and unstable-period settings recorded with the feature version?

## Why this score for a trading system

3/5: a direct feature-equivalence contract; indicator availability does not supply evidence of a profitable signal.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
