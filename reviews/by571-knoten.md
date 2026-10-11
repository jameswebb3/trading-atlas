# knoten — A new claim must clear the gates of claims it replaces

**Decision question:** Can a broad summary quietly bury a narrower result that survived stronger tests?

| Field | Review |
| --- | --- |
| Upstream | [BY571/knoten](https://github.com/BY571/knoten) |
| Primary area | Research & Reproducibility |
| Source commit | [8b3f907d1fad2c2bdf2aad72ce6e047747e79d01](https://github.com/BY571/knoten/commit/8b3f907d1fad2c2bdf2aad72ce6e047747e79d01) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/BY571/knoten/blob/8b3f907d1fad2c2bdf2aad72ce6e047747e79d01/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its validator disallows a node from superseding findings outside the same question, requires the new claim to survive every gate its targets survived, and demands an explicit Covers section. Graph links and gates are only as correct as their authors; this is structural protection against losing negative results, not a proof that the new claim is true. |

## What this project does

Knowledge graph for research questions, hypotheses, findings and gates. [README](https://github.com/BY571/knoten/blob/8b3f907d1fad2c2bdf2aad72ce6e047747e79d01/README.md).

## Mechanism inspected

Its validator disallows a node from superseding findings outside the same question, requires the new claim to survive every gate its targets survived, and demands an explicit Covers section. [Implementation](https://github.com/BY571/knoten/blob/8b3f907d1fad2c2bdf2aad72ce6e047747e79d01/src/knoten/validate.py#L288-L363).

## Limitation that matters

Graph links and gates are only as correct as their authors; this is structural protection against losing negative results, not a proof that the new claim is true. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

When consolidating closed axes or repo findings, preserve the old studies and require a superseding summary to cite each covered item and meet their strongest evidentiary gate.

## Why this score

Its validator disallows a node from superseding findings outside the same question, requires the new claim to survive every gate its targets survived, and demands an explicit Covers section. Graph links and gates are only as correct as their authors; this is structural protection against losing negative results, not a proof that the new claim is true.

## Source trail

[README](https://github.com/BY571/knoten/blob/8b3f907d1fad2c2bdf2aad72ce6e047747e79d01/README.md) · [Implementation](https://github.com/BY571/knoten/blob/8b3f907d1fad2c2bdf2aad72ce6e047747e79d01/src/knoten/validate.py#L288-L363) · [License](https://github.com/BY571/knoten/blob/8b3f907d1fad2c2bdf2aad72ce6e047747e79d01/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
