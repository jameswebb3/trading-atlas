# Superalgos: keep the unfinished candle out of learning steps

**Decision question:** How does a candle-based learning loop avoid processing its latest mutable bar?

| Field | Review |
| --- | --- |
| Upstream | [Superalgos](https://github.com/Superalgos/Superalgos) |
| Primary area | Signals & Models |
| Source commit | [9f0fb59edd4bae7afa08d06c366e0bcb48103aec](https://github.com/Superalgos/Superalgos/commit/9f0fb59edd4bae7afa08d06c366e0bcb48103aec) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/Superalgos/Superalgos/blob/9f0fb59edd4bae7afa08d06c366e0bcb48103aec/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Combines a visual crypto trading platform with learning sessions. The inspected learning loop explicitly excludes the last candle and resumes from a stored candle index, offering a readable example of separating completed bars from mutable input. |

## Project overview

A broad visual platform supports data mining, strategy design, learning, and crypto trading sessions. [Project documentation](https://github.com/Superalgos/Superalgos/blob/9f0fb59edd4bae7afa08d06c366e0bcb48103aec/README.md#L34-L46).

## Mechanism worth inspecting

The [learning loop](https://github.com/Superalgos/Superalgos/blob/9f0fb59edd4bae7afa08d06c366e0bcb48103aec/Projects/Machine-Learning/TS/Bot-Modules/Learning-Bot/Low-Frequency-Learning/LearningSimulation.js#L110-L160) chooses a starting index, stops when requested data is unavailable, and iterates only to the penultimate candle. Its [daily-file handling](https://github.com/Superalgos/Superalgos/blob/9f0fb59edd4bae7afa08d06c366e0bcb48103aec/Projects/Machine-Learning/TS/Bot-Modules/Learning-Bot/Low-Frequency-Learning/LearningSimulation.js#L87-L99) removes prior-day candles before processing.

## Important limit

The [starting-index calculation](https://github.com/Superalgos/Superalgos/blob/9f0fb59edd4bae7afa08d06c366e0bcb48103aec/Projects/Machine-Learning/TS/Bot-Modules/Learning-Bot/Low-Frequency-Learning/LearningSimulation.js#L115-L121) estimates position from elapsed time and configured frame size; irregular bars need separate handling. The reviewed learning-system documentation contains placeholder content, and the broad platform's trading execution was not audited.

## Questions to take into your own design

- Is bar completion an explicit timestamp condition rather than merely list position?
- Does restart remain correct when bars are missing or inserted retroactively?

## Why this score for a trading system

2/5: a useful small learning-loop example within a large platform, with regular-grid assumptions and incomplete inspected learning documentation.

**Scope of this review:** README, candle and learning-system schema documentation, learning simulation source.
