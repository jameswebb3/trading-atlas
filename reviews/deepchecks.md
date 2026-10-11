# Deepchecks: a clean date split can still leak through labels

**Decision question:** What does a train-test date-overlap check detect, and miss?

| Field | Review |
| --- | --- |
| Upstream | [Deepchecks](https://github.com/deepchecks/deepchecks) |
| Primary area | Data Quality & Lineage |
| Source commit | [98475d17b08a21fca29d533b94b8ec3c70544a85](https://github.com/deepchecks/deepchecks/commit/98475d17b08a21fca29d533b94b8ec3c70544a85) |
| Reviewed | 2026-09-25 |
| Declared license | [AGPL-3.0](https://github.com/deepchecks/deepchecks/blob/98475d17b08a21fca29d533b94b8ec3c70544a85/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Samples train and test sets, then counts test dates earlier than the latest training date; a second check finds duplicate rows across sets. Both are useful alarms, but neither computes a label's event end or feature publication time. |

## Mechanism worth inspecting

The [overview](https://github.com/deepchecks/deepchecks/blob/98475d17b08a21fca29d533b94b8ec3c70544a85/README.md#L31-L35) positions Deepchecks as data and model validation. The [date-overlap check](https://github.com/deepchecks/deepchecks/blob/98475d17b08a21fca29d533b94b8ec3c70544a85/deepchecks/tabular/checks/train_test_validation/date_train_test_leakage_overlap.py#L19-L75) samples each set and reports the share of test dates before the latest sampled training date. The [sample-mix check](https://github.com/deepchecks/deepchecks/blob/98475d17b08a21fca29d533b94b8ec3c70544a85/deepchecks/tabular/checks/train_test_validation/train_test_samples_mix.py#L29-L91) joins unique rows to report exact train-test duplicates. They answer different questions and should not be conflated.

## Important limit

The date check [defaults to a sample and uses one datetime column](https://github.com/deepchecks/deepchecks/blob/98475d17b08a21fca29d533b94b8ec3c70544a85/deepchecks/tabular/checks/train_test_validation/date_train_test_leakage_overlap.py#L24-L63). A training label whose information window overlaps the test period can pass if its start date is earlier. Neither check establishes available-at time for features.

## Questions to take into your own design

- Are label start and end intervals checked, not only row dates?
- Does sampling hide a rare but consequential overlap?

## Why this score for a trading system

Its date and duplicate checks are practical research alarms, but sampled row-level tests do not replace event-interval and publication-time validation.

**Scope of this review:** We read the pinned README and two tabular validation implementations. We did not run their suites or assess every check.
