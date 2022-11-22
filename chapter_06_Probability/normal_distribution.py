import math
import matplotlib.pyplot as plt


def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
	"""A function to calculate the normal distribution with default parameters"""
	return (math.exp(-(x - mu) ** 2) / (2 * sigma **2)) / (math.sqrt(2 * math.pi * sigma))


xs = [x / 10.0 for x in range(-50, 50)]

plt.plot(xs, [normal_pdf(x) for x in xs], "-", label="mu: 0, sigma: 1")
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], "--", label="mu: 0, sigma: 2")
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], "*", label="mu: 0, sigma: 0.5")
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], ".", label="mu: -1, sigma: 1")
plt.plot(xs, [normal_pdf(x, mu=-1, sigma=2) for x in xs], ":", label="mu: -1, sigma: 2")
plt.legend()
plt.show()
