# BayesianOptimization — Can probing an existing parameter point return an old result without a new evaluation

**Decision question:** Can probing an existing parameter point return an old result without a new evaluation?

| Field | Review |
| --- | --- |
| Upstream | [BayesianOptimization](https://github.com/fmfn/BayesianOptimization) |
| Primary area | Research & Reproducibility |
| Source commit | [af8b928212f0eacd1ce20c20be72c1a7b1d8d421](https://github.com/fmfn/BayesianOptimization/commit/af8b928212f0eacd1ce20c20be72c1a7b1d8d421) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/fmfn/BayesianOptimization/blob/af8b928212f0eacd1ce20c20be72c1a7b1d8d421/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Can serve a cached result for a repeated parameter point instead of running another evaluation. Useful for making cache hits, repeated trials and experiment identity explicit in optimisation reports. |

## Project overview

A Gaussian-process-based Bayesian optimisation package for expensive bounded objectives, including constrained optimisation. [Project documentation](https://github.com/fmfn/BayesianOptimization/blob/af8b928212f0eacd1ce20c20be72c1a7b1d8d421/README.md#L14-L22).

## Mechanism worth inspecting

TargetSpace caches parameter points. Probe returns a cached result when duplicates are disallowed; when duplicates are enabled it can evaluate and register the point again, and registration maintains a duplicate counter. [Duplicate policy](https://github.com/fmfn/BayesianOptimization/blob/af8b928212f0eacd1ce20c20be72c1a7b1d8d421/bayes_opt/target_space.py#L464-L477); [probe cache and evaluation](https://github.com/fmfn/BayesianOptimization/blob/af8b928212f0eacd1ce20c20be72c1a7b1d8d421/bayes_opt/target_space.py#L547-L563).

## Important limit

The cache key in this path is the parameter point, not a complete data/code/evaluation identity. Reusing an optimiser across changed experimental conditions can therefore reuse a result whose wider context needs separate validation.

## Questions to take into your own design

- Does the experiment identity include data, code and evaluation rules as well as parameters?
- Are cache hits reported separately from new executions and repeated trials?

## Why this score for a trading system

3/5: an inspectable transferable cache-identity boundary with clear relevance to reproducible research.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
