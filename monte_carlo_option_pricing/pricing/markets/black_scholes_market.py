from dataclasses import dataclass
from typing import Callable
import numpy as np

from .base import Market

@dataclass(frozen = True)
class BlackScholesMarket(Market):
	r: float
	sigma: float
	solver: Callable

	def simulate(self, spot: float, maturity: float, Z: np.ndarray) -> np.ndarray:
		return self.solver(self.r, self.sigma, spot, maturity, Z)

	def discount_factor(self, maturity: float) -> float:
		return np.exp(-self.r * maturity)