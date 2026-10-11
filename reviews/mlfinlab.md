# mlfinlab: the public purge API is a stub

**Decision question:** Is the advertised purged cross-validation path implemented in this public tree?

| Field | Review |
| --- | --- |
| Upstream | [mlfinlab](https://github.com/hudson-and-thames/mlfinlab) |
| Primary area | Signals & Models |
| Source commit | [79dcc7120ec84110578f75b025a75850eb72fc73](https://github.com/hudson-and-thames/mlfinlab/commit/79dcc7120ec84110578f75b025a75850eb72fc73) |
| Reviewed | 2026-09-25 |
| Declared license | [All rights reserved / proprietary terms](https://github.com/hudson-and-thames/mlfinlab/blob/79dcc7120ec84110578f75b025a75850eb72fc73/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | The public tree describes interval-aware purging, but the inspected PurgedKFold constructor and split method contain only pass statements. The combinatorial split module is similarly stubbed. Its license reserves rights; this tree is a conceptual reference, not a usable implementation. |

## Mechanism worth inspecting

The [README](https://github.com/hudson-and-thames/mlfinlab/blob/79dcc7120ec84110578f75b025a75850eb72fc73/README.md#L69-L74) lists code modules and identifies an all-rights-reserved license. The [cross-validation module](https://github.com/hudson-and-thames/mlfinlab/blob/79dcc7120ec84110578f75b025a75850eb72fc73/mlfinlab/cross_validation/cross_validation.py#L20-L79) explains interval overlap and embargo in docstrings, yet ml_get_train_times, PurgedKFold.__init__, and PurgedKFold.split are all pass bodies. The [combinatorial module](https://github.com/hudson-and-thames/mlfinlab/blob/79dcc7120ec84110578f75b025a75850eb72fc73/mlfinlab/cross_validation/combinatorial.py#L20-L78) also exposes empty bodies. Reading the implementation changes the practical verdict materially.

## Important limit

The [license terms](https://github.com/hudson-and-thames/mlfinlab/blob/79dcc7120ec84110578f75b025a75850eb72fc73/LICENSE.txt#L1-L29) are not an open-source grant. A private or paid distribution may differ, which this review has not inspected. No performance or leakage claim can be assigned to the public stubs.

## Questions to take into your own design

- Has the actual splitter implementation been inspected, not just its API name?
- Does a test prove training-label intervals do not overlap the held-out interval?

## Why this score for a trading system

The purging concept is directly relevant to trading research, but the public methods inspected are unimplemented and the license is proprietary.

**Scope of this review:** We read the pinned README, license, and public cross-validation source. We did not obtain or run a private distribution.
