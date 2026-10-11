# skfolio: inspect what the purge removes

**Decision question:** Does a purged cross-validation splitter know when financial labels actually overlap?

| Field | Review |
| --- | --- |
| Upstream | [skfolio/skfolio](https://github.com/skfolio/skfolio) |
| Primary area | Portfolio & Risk |
| Source commit | [f45fa1e1915ae17d0b07a3912af44946e38e77e4](https://github.com/skfolio/skfolio/commit/f45fa1e1915ae17d0b07a3912af44946e38e77e4) |
| Reviewed | 2026-09-25 |
| Declared license | [BSD-3-Clause](https://github.com/skfolio/skfolio/blob/f45fa1e1915ae17d0b07a3912af44946e38e77e4/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Builds multiple out-of-sample paths with combinatorial folds and configurable purge and embargo widths. The inspected splitter removes fixed numbers of rows around fold boundaries; both widths default to zero and do not derive from label event times. |

## Project overview

Portfolio optimization and risk library with a scikit-learn-compatible interface. Combines model selection, cross-validation, and stress testing to compare portfolio construction choices.

[Project documentation](https://github.com/skfolio/skfolio/blob/f45fa1e1915ae17d0b07a3912af44946e38e77e4/README.rst#L54-L61).

## Mechanism worth inspecting

The [README](https://github.com/skfolio/skfolio/blob/f45fa1e1915ae17d0b07a3912af44946e38e77e4/README.rst#L54-L64) positions skfolio as portfolio optimization and risk tooling. Its [CombinatorialPurgedCV description](https://github.com/skfolio/skfolio/blob/f45fa1e1915ae17d0b07a3912af44946e38e77e4/src/skfolio/model_selection/_combinatorial.py#L49-L86) describes multiple testing paths plus purge and embargo. The [split implementation](https://github.com/skfolio/skfolio/blob/f45fa1e1915ae17d0b07a3912af44946e38e77e4/src/skfolio/model_selection/_combinatorial.py#L314-L361) creates fold assignments, removes configured row counts around test boundaries, and yields train and test indices.

## Important limit

The constructor documentation gives zero as the default for both widths. The inspected code acts on positions, not each label's start/end interval. A user must set widths appropriate to their label horizon and verify overlap explicitly when horizons vary. Multiple paths do not by themselves correct model selection across many attempted ideas or a small effective sample.

## Questions to take into your own design

- What unit sets purge and embargo: rows, bars, or actual label intervals?
- Are both widths nonzero when labels overlap?
- How many independent decisions remain after recombining paths?

## Why this score for a trading system

Path accounting is relevant to portfolio selection, but zero-default positional purge must not be mistaken for event-time protection.

**Scope of this review:** We read the pinned README, documentation index, and splitter implementation. We did not run a cross-validation or inspect all portfolio estimators.
