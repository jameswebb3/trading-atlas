# CorruptChain — A failed tool can contaminate a final decision

**Decision question:** Can a failed research tool still shape the final answer?

| Field | Review |
| --- | --- |
| Upstream | [thevoodjev/CorruptChain](https://github.com/thevoodjev/CorruptChain) |
| Primary area | Agents & Decision Systems |
| Source commit | [3625de16dffb9dc30f4c9a2f390ff031d40c5865](https://github.com/thevoodjev/CorruptChain/commit/3625de16dffb9dc30f4c9a2f390ff031d40c5865) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/thevoodjev/CorruptChain/blob/3625de16dffb9dc30f4c9a2f390ff031d40c5865/LICENSE)) |
| Review depth | 3/3: README and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | It seeds taint at degraded tool steps, walks declared or inferred dependency edges in trace order, and keeps the origin, full path and weakest evidence link in each result. Inferred edges use literal output-substring matching with an eight-character floor; coincidence and paraphrase can create false links or miss real dependencies. The inspected tests are synthetic. |

## What this project does

Small local analyzer for step-by-step agent traces that identifies degraded tool outputs and follows their downstream consumers. [README](https://github.com/thevoodjev/CorruptChain/blob/3625de16dffb9dc30f4c9a2f390ff031d40c5865/README.md).

## Mechanism inspected

It seeds taint at degraded tool steps, walks declared or inferred dependency edges in trace order, and keeps the origin, full path and weakest evidence link in each result. [Implementation](https://github.com/thevoodjev/CorruptChain/blob/3625de16dffb9dc30f4c9a2f390ff031d40c5865/src/corruptchain/taint.py#L66-L106). [Test source](https://github.com/thevoodjev/CorruptChain/blob/3625de16dffb9dc30f4c9a2f390ff031d40c5865/tests/test_taint.py#L33-L68).

## Limitation that matters

Inferred edges use literal output-substring matching with an eight-character floor; coincidence and paraphrase can create false links or miss real dependencies. The inspected tests are synthetic. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Record explicit tool-output references and statuses in research runs; propagate invalidity to downstream claims while marking inferred links as weaker evidence.

## Why this score

It seeds taint at degraded tool steps, walks declared or inferred dependency edges in trace order, and keeps the origin, full path and weakest evidence link in each result. Inferred edges use literal output-substring matching with an eight-character floor; coincidence and paraphrase can create false links or miss real dependencies. The inspected tests are synthetic.

## Source trail

[README](https://github.com/thevoodjev/CorruptChain/blob/3625de16dffb9dc30f4c9a2f390ff031d40c5865/README.md) · [Implementation](https://github.com/thevoodjev/CorruptChain/blob/3625de16dffb9dc30f4c9a2f390ff031d40c5865/src/corruptchain/taint.py#L66-L106) · [Test source](https://github.com/thevoodjev/CorruptChain/blob/3625de16dffb9dc30f4c9a2f390ff031d40c5865/tests/test_taint.py#L33-L68) · [License](https://github.com/thevoodjev/CorruptChain/blob/3625de16dffb9dc30f4c9a2f390ff031d40c5865/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
