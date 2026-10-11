# NNI: preserve trial identities before choosing a winner

**Decision question:** Can a tuning run reconstruct every attempted configuration?

| Field | Review |
| --- | --- |
| Upstream | [NNI](https://github.com/microsoft/nni) |
| Primary area | Research & Reproducibility |
| Source commit | [767ed7f22e1e588ce76cbbecb6c6a4a76a309805](https://github.com/microsoft/nni/commit/767ed7f22e1e588ce76cbbecb6c6a4a76a309805) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/microsoft/nni/blob/767ed7f22e1e588ce76cbbecb6c6a4a76a309805/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Models a tuning experiment as many identifiable trials, each with parameters and intermediate or final metrics. Resume is keyed by an experiment checkpoint. This gives a clear trial ledger, but it does not correct the statistical bias from selecting the best trial. |

## Mechanism worth inspecting

The [overview](https://github.com/microsoft/nni/blob/767ed7f22e1e588ce76cbbecb6c6a4a76a309805/README.md#L19-L20) presents hyperparameter tuning. The [experiment guide](https://github.com/microsoft/nni/blob/767ed7f22e1e588ce76cbbecb6c6a4a76a309805/docs/source/experiment/overview.rst#L1-L8) defines an experiment as one tuning process with multiple trials. The [trial records](https://github.com/microsoft/nni/blob/767ed7f22e1e588ce76cbbecb6c6a4a76a309805/nni/experiment/data.py#L11-L61) retain parameters, trial ID, metric type, timestamp, and sequence. The [resume path](https://github.com/microsoft/nni/blob/767ed7f22e1e588ce76cbbecb6c6a4a76a309805/nni/experiment/experiment.py#L238-L266) checks for a prior experiment manifest before continuing.

## Important limit

The inspected records describe individual trials, not the full universe of informal manual experiments outside NNI. Search continuation must preserve the same trial family and untouched evaluation period. A trial manager does not itself provide a deflated significance estimate.

## Questions to take into your own design

- Does the ledger include failed, stopped, and resumed trials?
- Is the final evaluation isolated from all tuning decisions?

## Why this score for a trading system

Explicit trial IDs and metric sequence support an auditable search ledger, while model-selection correction remains a separate research rule.

**Scope of this review:** We read the pinned README, experiment guide, trial data types, and resume path. We did not run tuning.
