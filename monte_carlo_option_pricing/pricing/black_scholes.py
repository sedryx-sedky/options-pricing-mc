from scipy.stats import norm
import numpy as np

__all__ = [
	'european_call', 'european_put',
	'delta'
]

def european_call(r, sigma, s, K, T):
	d1 = 1 / (sigma * np.sqrt(T)) * (np.log(s / K) + (r + sigma ** 2 / 2) * T)
	d2 = d1 - sigma * np.sqrt(T)

	return s * norm.cdf(d1) - np.exp(-r * T) * K * norm.cdf(d2)

def european_put(r, sigma, s, K, t = 0):
	d1 = 1 / (sigma * np.sqrt(T)) * (np.log(s / K) + (r + sigma ** 2 / 2) * T)
	d2 = d1 - sigma * np.sqrt(T - t)

	return K * np.exp(-r * T) * norm.cdf(-d2) - s * norm.cdf(-d1)

def delta(r, sigma, s, K, T, t = 0):
	d1 = 1 / (sigma * np.sqrt(T)) * (np.log(s / K) + (r + sigma ** 2 / 2) * T)
	return norm.cdf(d1)