import numpy as np
from typing import Optional, Callable

from .processes import gbm
from .options import Option

__all__ = ['monte_carlo_pricer']

def monte_carlo_pricer(option: Option, r: float, sigma: float, s: float, T: float,
    N: int = 1, n_paths: int = 1,
    antithetic: bool = False, seed: Optional[int] = None
    ) -> tuple[float, float]:
    """
    """

    paths = gbm(r, sigma, s, T, N, n_paths, antithetic, seed)
    discounted_payoff = np.exp(-r * T) * option.payoff(paths)

    if antithetic:
        # need to compute the standard error in a slighly different way
        m, d = divmod(n_paths, 2)
        paired_payoffs = np.zeros(m + d)

        paired_payoffs[0:m] = 0.5 * (
            discounted_payoff[0:m] + discounted_payoff[m:2*m]
        ) # gbm returns [Z_1, ..., Z_m, -Z_1, ..., -Z_m]
        
        if d == 1:
            paired_payoffs[-1] = discounted_payoff[-1]

        price = paired_payoffs.mean()
        std_error = paired_payoffs.std(ddof = 1) / np.sqrt(len(paired_payoffs))
    else:
        price = discounted_payoff.mean()
        std_error = discounted_payoff.std(ddof = 1) / np.sqrt(n_paths)

    return price, std_error