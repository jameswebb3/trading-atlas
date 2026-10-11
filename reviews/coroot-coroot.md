# coroot — Show missing telemetry as unknown, not healthy

**Decision question:** What does an alert report when its SLI has no samples?

| Field | Review |
| --- | --- |
| Upstream | [coroot/coroot](https://github.com/coroot/coroot) |
| Primary area | Operations & Observability |
| Source commit | [ecf2a6aeeead958ce87817ce0914add14c7860d6](https://github.com/coroot/coroot/commit/ecf2a6aeeead958ce87817ce0914add14c7860d6) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/coroot/coroot/blob/ecf2a6aeeead958ce87817ce0914add14c7860d6/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | If an SLI is unconfigured or raw request counts have no tail data, the check becomes UNKNOWN with a reason before any OK path is reached. It audits service requests rather than market feeds; a configured SLI may still be semantically wrong, and UNKNOWN needs its own operational response. |

## What this project does

Service auditor with availability and latency SLO checks. [README](https://github.com/coroot/coroot/blob/ecf2a6aeeead958ce87817ce0914add14c7860d6/README.md).

## Mechanism inspected

If an SLI is unconfigured or raw request counts have no tail data, the check becomes UNKNOWN with a reason before any OK path is reached. [Implementation](https://github.com/coroot/coroot/blob/ecf2a6aeeead958ce87817ce0914add14c7860d6/auditor/slo.go#L20-L68).

## Limitation that matters

It audits service requests rather than market feeds; a configured SLI may still be semantically wrong, and UNKNOWN needs its own operational response. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

For feed freshness, collector health and fill coverage, distinguish healthy from no-data, not-configured and stale before publishing a green status.

## Why this score

If an SLI is unconfigured or raw request counts have no tail data, the check becomes UNKNOWN with a reason before any OK path is reached. It audits service requests rather than market feeds; a configured SLI may still be semantically wrong, and UNKNOWN needs its own operational response.

## Source trail

[README](https://github.com/coroot/coroot/blob/ecf2a6aeeead958ce87817ce0914add14c7860d6/README.md) · [Implementation](https://github.com/coroot/coroot/blob/ecf2a6aeeead958ce87817ce0914add14c7860d6/auditor/slo.go#L20-L68) · [License](https://github.com/coroot/coroot/blob/ecf2a6aeeead958ce87817ce0914add14c7860d6/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
