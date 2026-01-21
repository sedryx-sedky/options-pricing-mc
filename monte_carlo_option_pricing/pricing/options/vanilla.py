from dataclasses import dataclass
import numpy as np

from .base import Option

@dataclass(frozen = True)
class EuropeanCall(Option):
	strike: float

	def payoff(self, paths: np.ndarray) -> np.ndarray:
		return np.maximum(paths[:, -1] - self.strike, 0)

@dataclass(frozen = True)
class EuropeanPut(Option):
	strike: float

	def payoff(self, paths: np.ndarray) -> np.ndarray:
		return np.maximum(self.strike - paths[:, -1], 0)