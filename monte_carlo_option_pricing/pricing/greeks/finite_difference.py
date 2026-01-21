from dataclasses import replace
import numpy as np

from pricing.options import Option
from pricing.markets import Market

def delta(option: Option, market: Market, spot: float, maturity: float, engine, eps) -> float:
	Z = engine.sample_Z()

	p1, se1 = engine.price(option, market, spot + eps, maturity, Z = Z)
	p2, se2 = engine.price(option, market, spot - eps, maturity, Z = Z)

	return (p1 - p2) / (2 * eps)

def rho(option: Option, market: Market, spot: float, maturity: float, engine, eps) -> np.ndarray:
	Z = engine.sample_Z()

	market_up = replace(market, r = market.r + eps)
	market_down = replace(market, r = market.r - eps)

	p_up, se1 = engine.price(option, market_up, spot, maturity, Z = Z)
	p_down, se2 = engine.price(option, market_down, spot, maturity, Z = Z)


	return (p_up - p_down) / (2 * eps)

@dataclass(frozen = True)
class FiniteDifference(Greeks):
	engine: Engine
	epsilon: float = 0.05

	def delta(option: Option, market: Market, spot: float, maturity: float) -> float:
		Z = self.engine.sample_Z()

		p_up, se_up = engine.price(option, market, spot + eps, maturity, Z = Z)
		p_down, se_down = engine.price(option, market, spot - eps, maturity, Z = Z)

		return (p_up - p_down) / (2 * eps)

	def rho(option: Option, market: Market, spot: float, maturity: float) -> float:
		Z = self.engine.sample_Z()

		market_up = replace(market, r = market.r + self.epsilon)
		market_down = replace(market, r = market.r - self.epsilon)

		p_up, se1 = self.engine.price(option, market_up, spot, maturity, Z = Z)
		p_down, se2 = self.engine.price(option, market_down, spot, maturity, Z = Z)


		return (p_up - p_down) / (2 * self.epsilon)