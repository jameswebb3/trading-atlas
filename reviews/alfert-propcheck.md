# propcheck — Parallel traces need a serializable outcome

**Decision question:** Can concurrent commands produce a state no valid ordering permits?

| Field | Review |
| --- | --- |
| Upstream | [propcheck](https://github.com/alfert/propcheck) |
| Primary area | Testing & Verification |
| Source commit | [270e00c6b202a0329cbc4098121ac7224dee39d8](https://github.com/alfert/propcheck/commit/270e00c6b202a0329cbc4098121ac7224dee39d8) |
| Reviewed | 2026-10-06 |
| Declared license | [GPL-3.0](https://github.com/alfert/propcheck/blob/270e00c6b202a0329cbc4098121ac7224dee39d8/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its state-machine documentation and API generate symbolic command sequences and evaluate parallel outcomes against possible serializations. A generic state model will miss exchange timing unless ACK, fill, cancel and restart semantics are modeled explicitly; GPL-3 code should not be copied. |

## What this project does

An Elixir wrapper over PropEr with state-machine property testing. [README](https://github.com/alfert/propcheck/blob/270e00c6b202a0329cbc4098121ac7224dee39d8/README.md).

## Mechanism inspected

Its state-machine documentation and API generate symbolic command sequences and evaluate parallel outcomes against possible serializations. [Implementation](https://github.com/alfert/propcheck/blob/270e00c6b202a0329cbc4098121ac7224dee39d8/lib/statem.ex#L108-L145).

## Limitation that matters

A generic state model will miss exchange timing unless ACK, fill, cancel and restart semantics are modeled explicitly; GPL-3 code should not be copied. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Write a tiny local model for two concurrent order intents and one shared balance, then test valid serializations.

## Why this score

Transferable engineering pattern: Its state-machine documentation and API generate symbolic command sequences and evaluate parallel outcomes against possible serializations. A generic state model will miss exchange timing unless ACK, fill, cancel and restart semantics are modeled explicitly; GPL-3 code should not be copied.

## Source trail

[README](https://github.com/alfert/propcheck/blob/270e00c6b202a0329cbc4098121ac7224dee39d8/README.md) · [Implementation](https://github.com/alfert/propcheck/blob/270e00c6b202a0329cbc4098121ac7224dee39d8/lib/statem.ex#L108-L145).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
