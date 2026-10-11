# ruptures — a historical break is not its detection time

**Decision question:** When was an offline change point actually knowable?

| Field | Review |
| --- | --- |
| Upstream | [ruptures](https://github.com/deepcharles/ruptures) |
| Primary area | Signals & Models |
| Source commit | [ee1c8ff8a548d54c641b2bb471562165931f31c7](https://github.com/deepcharles/ruptures/commit/ee1c8ff8a548d54c641b2bb471562165931f31c7) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-2-Clause](https://github.com/deepcharles/ruptures/blob/ee1c8ff8a548d54c641b2bb471562165931f31c7/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | A useful offline segmentation reference. Its break locations describe the fitted history; treating them as live signals requires separate detection timestamps and a policy for revised historical partitions. |

## Project overview

ruptures is a toolkit for offline change-point detection and segmentation of non-stationary series. [Project documentation](https://github.com/deepcharles/ruptures/blob/ee1c8ff8a548d54c641b2bb471562165931f31c7/README.md#L15-L18).

## Mechanism worth inspecting

PELT fits a cost model to the supplied signal and stores its total sample count. Its prediction computes a penalized partition over that fitted sequence. `jump` restricts candidate breakpoints to a grid, while `min_size` limits segment lengths. [Fit/predict](https://github.com/deepcharles/ruptures/blob/ee1c8ff8a548d54c641b2bb471562165931f31c7/src/ruptures/detection/pelt.py#L99-L143); [grid documentation](https://github.com/deepcharles/ruptures/blob/ee1c8ff8a548d54c641b2bb471562165931f31c7/docs/user-guide/detection/pelt.md#L14-L17).

## Important limit

The retrospective location of a break does not establish when a live process could have detected it. Appending observations can change the optimal historical partition. An online application needs detection-time records, prefix evaluation and an explicit revision policy.

## Questions to take into your own design

- Does the output preserve both estimated break location and first detection time?
- How are historical labels revised when a longer prefix changes the partition?

## Why this score for a trading system

2/5: useful for retrospective segmentation and timing checks, but converting offline breakpoints into tradable features requires a distinct validated design.

**Scope of this review:** PELT fit, partition prediction and candidate grid; no comparative detector study.
