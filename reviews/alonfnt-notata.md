# notata — Parameter strings are not a safe run key

**Decision question:** Can distinct experiments overwrite or skip each other when their labels match?

| Field | Review |
| --- | --- |
| Upstream | [notata](https://github.com/alonfnt/notata) |
| Primary area | Research & Reproducibility |
| Source commit | [beb45d37bd284873bdf7dbe9907ccef59d2d3459](https://github.com/alonfnt/notata/commit/beb45d37bd284873bdf7dbe9907ccef59d2d3459) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/alonfnt/notata/blob/beb45d37bd284873bdf7dbe9907ccef59d2d3459/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The run ID is assembled from formatted parameter strings and skip_existing only checks whether that directory exists; the index records status and metrics. Different datasets or code with identical parameters can collide, and floats are rounded to five significant digits in the key. |

## What this project does

A local filesystem logbook for scientific runs. [README](https://github.com/alonfnt/notata/blob/beb45d37bd284873bdf7dbe9907ccef59d2d3459/README.md).

## Mechanism inspected

The run ID is assembled from formatted parameter strings and skip_existing only checks whether that directory exists; the index records status and metrics. [Implementation](https://github.com/alonfnt/notata/blob/beb45d37bd284873bdf7dbe9907ccef59d2d3459/notata/experiment.py#L48-L100).

## Limitation that matters

Different datasets or code with identical parameters can collide, and floats are rounded to five significant digits in the key. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Key reuse on data/code/rule hashes, preserve origin_run and record whether a result came from cache.

## Why this score

Transferable engineering pattern: The run ID is assembled from formatted parameter strings and skip_existing only checks whether that directory exists; the index records status and metrics. Different datasets or code with identical parameters can collide, and floats are rounded to five significant digits in the key.

## Source trail

[README](https://github.com/alonfnt/notata/blob/beb45d37bd284873bdf7dbe9907ccef59d2d3459/README.md) · [Documentation](https://github.com/alonfnt/notata/blob/beb45d37bd284873bdf7dbe9907ccef59d2d3459/docs/source/tutorials.rst) · [Implementation](https://github.com/alonfnt/notata/blob/beb45d37bd284873bdf7dbe9907ccef59d2d3459/notata/experiment.py#L48-L100).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
