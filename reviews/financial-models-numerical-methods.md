# Financial Models & Numerical Methods: distinguish sampling error from model error

**Decision question:** Does a precise simulation estimate say anything about whether its market model is right?

| Field | Review |
| --- | --- |
| Upstream | [Financial Models & Numerical Methods](https://github.com/cantaro86/Financial-Models-Numerical-Methods) |
| Primary area | Portfolio & Risk |
| Source commit | [65a8124c4fdf80f8cf7de234be9f8393927b8488](https://github.com/cantaro86/Financial-Models-Numerical-Methods/commit/65a8124c4fdf80f8cf7de234be9f8393927b8488) |
| Reviewed | 2026-09-26 |
| Declared license | [AGPL-3.0](https://github.com/cantaro86/Financial-Models-Numerical-Methods/blob/65a8124c4fdf80f8cf7de234be9f8393927b8488/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Shows option prices computed through analytical and numerical methods, with optional Monte Carlo standard errors. A useful numerical validation reference, but its sampling precision does not validate a market model, trading signal, or execution assumption. |

## Mechanism worth inspecting

The [README contents](https://github.com/cantaro86/Financial-Models-Numerical-Methods/blob/65a8124c4fdf80f8cf7de234be9f8393927b8488/README.md#L63-L75) identify numerical pricing and simulation topics. The [Black-Scholes notebook](https://github.com/cantaro86/Financial-Models-Numerical-Methods/blob/65a8124c4fdf80f8cf7de234be9f8393927b8488/1.1%20Black-Scholes%20numerical%20methods.ipynb#L359-L411) calculates discounted payoff means and standard errors. In the [pricer implementation](https://github.com/cantaro86/Financial-Models-Numerical-Methods/blob/65a8124c4fdf80f8cf7de234be9f8393927b8488/src/FMNM/BS_pricer.py#L87-L99), an analytical formula is available alongside the [Monte Carlo method](https://github.com/cantaro86/Financial-Models-Numerical-Methods/blob/65a8124c4fdf80f8cf7de234be9f8393927b8488/src/FMNM/BS_pricer.py#L160-L183), which can return an estimate, its sample standard error, and elapsed time. That separation is worth carrying into numerical research reports.

## Important limit

The Monte Carlo method defaults to returning only the point estimate. Its error calculation is conditional on the supplied generator and payoff model. Agreement with the analytical formula would check a numerical implementation under matching assumptions; it would not establish predictive usefulness, causal data availability, or a tradable opportunity. The [README](https://github.com/cantaro86/Financial-Models-Numerical-Methods/blob/65a8124c4fdf80f8cf7de234be9f8393927b8488/README.md#L19-L30) presents educational finance material rather than an execution system.

## Questions to take into your own design

- Does every simulated estimate report its sample size, seed policy, numerical error, and model assumptions?
- Is implementation error checked against a known special case separately from the model's fit to observed data?

## Why this score for a trading system

2/5: an adjacent reference for validating simulation estimates, rather than a direct portfolio control or trading mechanism. The cited error reporting is concrete, but its meaning is narrower than economic uncertainty.

**Scope of this review:** We read the pinned overview, relevant documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
