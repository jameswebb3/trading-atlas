# paper-search-mcp — Postfiltering a capped search can miss relevant records

**Decision question:** Does a literature search return N matching papers or N fetched papers?

| Field | Review |
| --- | --- |
| Upstream | [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) |
| Primary area | Research & Reproducibility |
| Source commit | [cab1b5cc276a0cd004a0044003926a6440088049](https://github.com/openags/paper-search-mcp/commit/cab1b5cc276a0cd004a0044003926a6440088049) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/openags/paper-search-mcp/blob/cab1b5cc276a0cd004a0044003926a6440088049/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | The BASE connector asks its parent search for max_results, then applies local language, subject and full-text filters to that capped page. If early fetched records fail local filters, it can return fewer matches even when later source records might qualify. |

## What this project does

MCP server for searching and downloading academic papers across open sources. [README](https://github.com/openags/paper-search-mcp/blob/cab1b5cc276a0cd004a0044003926a6440088049/README.md).

## Mechanism inspected

The BASE connector asks its parent search for max_results, then applies local language, subject and full-text filters to that capped page. [Implementation](https://github.com/openags/paper-search-mcp/blob/cab1b5cc276a0cd004a0044003926a6440088049/paper_search_mcp/academic_platforms/base_search.py#L34-L101).

## Limitation that matters

If early fetched records fail local filters, it can return fewer matches even when later source records might qualify. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Record fetched count, filter count, continuation and source date when using external literature search to support a research claim.

## Why this score

The BASE connector asks its parent search for max_results, then applies local language, subject and full-text filters to that capped page. If early fetched records fail local filters, it can return fewer matches even when later source records might qualify.

## Source trail

[README](https://github.com/openags/paper-search-mcp/blob/cab1b5cc276a0cd004a0044003926a6440088049/README.md) · [Implementation](https://github.com/openags/paper-search-mcp/blob/cab1b5cc276a0cd004a0044003926a6440088049/paper_search_mcp/academic_platforms/base_search.py#L34-L101) · [License](https://github.com/openags/paper-search-mcp/blob/cab1b5cc276a0cd004a0044003926a6440088049/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
