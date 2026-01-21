import numpy as np

def exact_gbm(drift: float, volatility: float, s0: float, T: float, Z: np.ndarray) -> np.ndarray:
    
    # Bound checks for parameters
    if volatility < 0:
        raise ValueError('volatility must be non-negative')

    if s0 <= 0:
        raise ValueError('s0 must be strictly positive')
    
    if T <= 0:
        raise ValueError('T must be positive')

    n_paths, n_steps = Z.shape
    dt = T / n_steps

    # Exact solution of Geometric Brownian Motion
    mu_dt = (drift - volatility ** 2 / 2) * dt
    sigma_sqrt_dt = volatility * np.sqrt(dt)
    log_paths = np.cumsum(mu_dt + sigma_sqrt_dt * Z, axis = 1)

    S = np.empty((n_paths, n_steps + 1))
    S[:, 0] = s0
    S[:, 1:] = s0 * np.exp(log_paths)

    return S



    """
    Simulate sample paths of a Geometric Brownian Motion (GBM).

    The process Sₜ satisfies the stochastic differential equation (SDE):
        dSₜ = μSₜ dt + σSₜ dWₜ,

    where μ is the drift, σ is the volatility, and Wₜ is a standard Brownian motion.
    The simulation uses the exact discretization of the GBM solution:
        Sₙ+₁ = Sₙ exp((μ - σ² / 2) Δt + σ√Δt Zₙ+₁),

    with Zₙ ~ N(0, 1) i.i.d. and Δt = T / N.

    Parameters
    ----------
    drift : float
        Drift parameter μ.
    volatility : float
        Volatility parameter σ. Must be non-negative.
    s0 : float
        Initial asset value S₀ at time t = 0. Must be strictly positive.
    T : float
        Terminal time of the simulation interval [0, T].
    N : int, optional
        Number of uniform time steps over [0, T]. Must be positive. Defaults to 1.
    n_paths : int, optional
        Number of independent Monte Carlo paths to simulate. Defaults to 1.
    antithetic: bool, optional
        If True, use antithetic variates by simulating paths with Z and −Z.
        Defaults to False.
    seed : int, optional
        Seed for the random number generator to ensure reproducibility.
        If None, the default NumPy random generator state is used.

    Returns
    -------
    numpy.ndarray
        A NumPy array of shape (n_paths, N + 1) containing the simulated
        GBM paths. Each row corresponds to a single Monte Carlo path.

    Raises
    ------
    ValueError
        If any of the input parameters fail to satisfy the following conditions:
        - volatility >= 0
        - s0 > 0
        - T > 0
        - N > 0
        - n_paths > 0

    Notes
    -----
    If `antithetic = True`, paths are paired as [Z₁, ..., Zₘ, -Z₁, ..., -Zₘ].
    If `n_paths` is odd, an additional independent path Z* is appended at the end.
    """