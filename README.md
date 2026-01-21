# Monte Carlo Simulation for Pricing and Risk Analysis of Exotic Options
Python-based Monte Carlo framework for pricing and risk analysis of exotic path-dependent options (Asian, barrier, lookback) under Black–Scholes, including variance reduction, benchmarking, and Greeks.

## Model and Pricing Framework

The underlying asset price is modeled as a Geometric Brownian Motion under the
risk-neutral measure:

dS_t = r S_t dt + σ S_t dW_t^Q

Option prices are computed as discounted expected payoffs,

V = e^{-rT} E^Q[ Π((S_t)_{t∈[0,T]}) ],

where Π may depend on the full price path. Path-dependent payoffs generally
preclude closed-form solutions, motivating the use of Monte Carlo simulation.
