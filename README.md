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
V = e^{-rT} \mathbb{E}^\mathbb{Q} \left[ \Pi((S_t)_{t\in[0,T]})\right],
$$

where Π may depend on the full price path. Path-dependent payoffs generally
preclude closed-form solutions, motivating the use of Monte Carlo simulation.
