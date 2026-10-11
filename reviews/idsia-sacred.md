# Sacred — a run has states, sources and a heartbeat

**Decision question:** Can an experiment remain visibly incomplete after its worker disappears?

| Field | Review |
| --- | --- |
| Upstream | [Sacred](https://github.com/IDSIA/sacred) |
| Primary area | Research & Reproducibility |
| Source commit | [86865b03d05e83da35ca582392ca31777db88d11](https://github.com/IDSIA/sacred/commit/86865b03d05e83da35ca582392ca31777db88d11) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/IDSIA/sacred/blob/86865b03d05e83da35ca582392ca31777db88d11/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its local observer makes run lifecycle, heartbeat and source evidence explicit. A useful ledger reference, provided worker loss remains an incomplete or failed attempt and source references are immutable. |

## Project overview

Sacred configures and records experiments, including parameters, sources, run states and observer outputs. [Project documentation](https://github.com/IDSIA/sacred/blob/86865b03d05e83da35ca582392ca31777db88d11/README.rst#L16-L23).

## Mechanism worth inspecting

The file observer records queued and running states, snapshots configuration and source references, updates heartbeat time and marks completion only on the completion event. This exposes lifecycle evidence rather than just a result file. [Queued/source records](https://github.com/IDSIA/sacred/blob/86865b03d05e83da35ca582392ca31777db88d11/sacred/observers/file_storage.py#L133-L167); [running record](https://github.com/IDSIA/sacred/blob/86865b03d05e83da35ca582392ca31777db88d11/sacred/observers/file_storage.py#L170-L186); [heartbeat/completion](https://github.com/IDSIA/sacred/blob/86865b03d05e83da35ca582392ca31777db88d11/sacred/observers/file_storage.py#L260-L276).

## Important limit

A stale RUNNING record is not a successful experiment, and the observer events alone do not decide abandonment, retries or sufficient output coverage. Source copying can be disabled; recorded references then need a separate immutability guarantee.

## Questions to take into your own design

- Which terminal state is assigned to an expired heartbeat with incomplete outputs?
- Can a retry overwrite the original run or make a source reference point at changed bytes?

## Why this score for a trading system

3/5: a useful local lifecycle and source-evidence reference, requiring trading-specific completion gates and immutable artifacts.

**Scope of this review:** File observer lifecycle and source records; other observers and experiment execution were not evaluated.
