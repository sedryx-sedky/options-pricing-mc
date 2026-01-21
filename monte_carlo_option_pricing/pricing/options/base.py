from abc import ABC, abstractmethod
import numpy as np

class Option(ABC):

	@abstractmethod
	def payoff(self, paths: np.ndarray) -> np.ndarray:
		...