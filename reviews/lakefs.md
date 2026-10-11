# lakeFS: stop a data commit when a gate fails

**Decision question:** Can a quality check block a data version before publication?

| Field | Review |
| --- | --- |
| Upstream | [treeverse/lakeFS](https://github.com/treeverse/lakeFS) |
| Primary area | Research & Reproducibility |
| Source commit | [24bfa90317e6e3ead13fb5cc8820f7c036baf088](https://github.com/treeverse/lakeFS/commit/24bfa90317e6e3ead13fb5cc8820f7c036baf088) |
| Reviewed | 2026-09-25 |
| Declared license | [Business Source License 1.1](https://github.com/treeverse/lakeFS/blob/24bfa90317e6e3ead13fb5cc8820f7c036baf088/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Calls prepare-commit and pre-commit hooks before advancing a branch to a new data version. A hook has to be configured to check trading-data quality, and the Business Source License limits direct reuse. |

## Mechanism worth inspecting

The [README](https://github.com/treeverse/lakeFS/blob/24bfa90317e6e3ead13fb5cc8820f7c036baf088/README.md#L19-L27) describes versioned object storage and its [write-audit-publish section](https://github.com/treeverse/lakeFS/blob/24bfa90317e6e3ead13fb5cc8820f7c036baf088/README.md#L77-L83) proposes checking data before publication. In the pinned [commit implementation](https://github.com/treeverse/lakeFS/blob/24bfa90317e6e3ead13fb5cc8820f7c036baf088/pkg/graveler/graveler.go#L2239-L2287), a failed prepare hook aborts. The [pre-commit hook](https://github.com/treeverse/lakeFS/blob/24bfa90317e6e3ead13fb5cc8820f7c036baf088/pkg/graveler/graveler.go#L2307-L2329) can also abort before the [new commit becomes the branch head](https://github.com/treeverse/lakeFS/blob/24bfa90317e6e3ead13fb5cc8820f7c036baf088/pkg/graveler/graveler.go#L2368-L2379).

The transferable idea is a publication gate: stage a candidate market dataset, run explicit checks, and expose its immutable version only after the checks pass.

## Important limits

Hooks provide a place for checks; the inspected path does not prescribe per-symbol completeness, decision-time availability, or a meaningful fail-closed policy when no hook exists. The [license](https://github.com/treeverse/lakeFS/blob/24bfa90317e6e3ead13fb5cc8820f7c036baf088/LICENSE#L1-L46) is Business Source License 1.1 with specific additional-use conditions. This review recommends a pattern to consider, not adopting the product.

## Questions to take into your own design

- What checks must pass before a dataset version becomes readable?
- Is the gate tied to a specific immutable input snapshot?
- What happens if the check did not run or returned no evidence?

## Why this score for a trading system

A pre-publication data gate is useful, but trading-specific checks are external to the inspected hook and the source-available license narrows direct use.

**Scope of this review:** We read pinned README, commit code, and license. We did not install or run lakeFS or inspect every hook implementation.
