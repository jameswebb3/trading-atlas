# QuantResearch: distinguish position weights from modeled risk contributions

**Decision question:** Can a portfolio report explain why capital allocation differs from risk contribution?

| Field | Review |
| --- | --- |
| Upstream | [QuantResearch](https://github.com/letianzj/QuantResearch) |
| Primary area | Portfolio & Risk |
| Source commit | [79bbf6a8b5ad74ac2c165663b5e12eb70d76a54e](https://github.com/letianzj/QuantResearch/commit/79bbf6a8b5ad74ac2c165663b5e12eb70d76a54e) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT (repository)](https://github.com/letianzj/QuantResearch/blob/79bbf6a8b5ad74ac2c165663b5e12eb70d76a54e/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Collects educational quantitative-research examples. Its value-at-risk script calculates portfolio, marginal, and component risk under a normal covariance model, providing a transparent example of attributing modeled risk rather than equating it with position weights. |

## Project overview

A collection links quantitative-finance notebooks and code to accompanying author explanations. [Project documentation](https://github.com/letianzj/QuantResearch/blob/79bbf6a8b5ad74ac2c165663b5e12eb70d76a54e/README.md#L8-L14).

## Mechanism worth inspecting

The [VaR example](https://github.com/letianzj/QuantResearch/blob/79bbf6a8b5ad74ac2c165663b5e12eb70d76a54e/notebooks/value_at_risk_one.py#L26-L51) computes portfolio covariance, marginal risk, and component allocations in currency units. The [author's explanation](https://letianzj.github.io/value-at-risk-one.html) states the return-normality assumption and shows how the component allocations reconcile to model portfolio VaR.

## Important limit

The [example](https://github.com/letianzj/QuantResearch/blob/79bbf6a8b5ad74ac2c165663b5e12eb70d76a54e/notebooks/value_at_risk_one.py#L9-L39) uses a fixed equity basket and historical covariance. This is an educational linear model, with no liquidity, nonlinear payoff, funding, or liquidation treatment; the model quantile should not be described as a maximum possible loss. The accompanying blog has its own content license.

## Questions to take into your own design

- Does risk attribution reconcile to the same total under the stated model?
- Are covariance stress scenarios and tail assumptions shown alongside the point estimate?

## Why this score for a trading system

2/5: transparent educational risk attribution, with strong distributional and market-scope limits.

**Scope of this review:** Full README, author VaR explanation, complete VaR script and repository license; no data download or model execution.
