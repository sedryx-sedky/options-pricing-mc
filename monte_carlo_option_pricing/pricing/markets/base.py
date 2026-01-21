from abc import ABC, abstractmethod
import numpy as np

class Market(ABC):

	@abstractmethod
	def simulate(self, spot: float, maturity: float, Z: np.ndarray) -> np.ndarray:
		...

	@abstractmethod
	def discount_factor(self, maturity: float) -> float:
		...