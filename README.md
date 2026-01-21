# Monte Carlo Simulation for Pricing and Risk Analysis of Exotic Options
Python-based Monte Carlo framework for pricing and risk analysis of exotic path-dependent options (Asian, barrier, lookback) under Black–Scholes, including variance reduction, benchmarking, and Greeks.

## Model and Pricing Framework

The underlying asset price is modeled as a Geometric Brownian Motion under the
risk-neutral measure:

$$
\mathrm{d}S_t = r S_t \mathrm{d}t + \sigma S_t \mathrm{d}W_t^{\mathbb{Q}}.
$$

Option prices are computed as discounted expected payoffs,

$$
V = r^{-rT} \mathbb{E}^\mathbb{Q} \left[ \Pi\left((S_t)_{t\in[0,T]}\right)\right],
$$

where $\Pi$ may depend on the full price path. Path-dependent payoffs generally
preclude closed-form solutions, motivating the use of Monte Carlo simulation.

## Monte Carlo Methodology

Asset price paths are generated via time discretization of the GBM dynamics.
For each option, the payoff is evaluated pathwise and averaged across simulated
paths to obtain an unbiased estimator of the option price.

Key parameters:
- Number of simulated paths
- Time discretization grid
- Random number generation and seeding

## Variance Reduction

To improve estimator efficiency, the following variance reduction techniques
are implemented:

- Antithetic variates
- Control variates (where analytical benchmarks are available)
- Moment matching

The impact of variance reduction is evaluated in terms of estimator variance
and runtime for a fixed accuracy target.

## Greeks Estimation

Option sensitivities are computed using Monte Carlo-based methods, including:

- Finite-difference approximations
- Pathwise estimators (where applicable)

Greeks are analyzed with respect to stability and convergence.

## Validation and Benchmarks

Monte Carlo prices are validated against analytical results where available,
including closed-form solutions for geometric Asian options.

Convergence behavior and pricing error are analyzed as a function of the
number of simulated paths.

