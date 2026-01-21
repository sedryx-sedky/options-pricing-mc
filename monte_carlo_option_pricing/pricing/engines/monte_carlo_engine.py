from dataclasses import dataclass
from typing import Optional
import numpy as np

from pricing.options import Option
from pricing.markets import Market

@dataclass
class MonteCarloEngine:
	n_steps: int
	n_paths: int
	seed: Optional[int] = None

	def __post_init__(self):
		self.rng = np.random.default_rng(self.seed)

	def sample_Z(self) -> np.ndarray:
		return self.rng.standard_normal((self.n_paths, self.n_steps))


	def price(self, option: Option, market: Market, spot: float, maturity: float, Z: Optional[np.ndarray] = None) -> tuple[float, float]:
		if Z is None:
			Z = self.sample_Z()
			
		elif Z.shape != (self.n_paths, self.n_steps):
			raise ValueError(
				f"Shape of Z is incompatible with engine parameters, "
				f"expected ({self.n_paths}, {self.n_steps}) but got {Z.shape}"
			)

		paths = market.simulate(spot, maturity, Z)
		discounted = market.discount_factor(maturity) * option.payoff(paths)

		
		price = discounted.mean()
		std_error = discounted.std(ddof = 1) / np.sqrt(self.n_paths)

		return price, std_error