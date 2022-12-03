from typing import List, Callable
import matplotlib.pyplot as plt


Vector = List[float]


def dot(v: Vector, w: Vector) -> float:
	"""Computes the dot product of two vectors"""
	assert len(v) == len(w), "Vectors must be the same length"
	return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
	"""Computes the sum of squared elements in v"""
	return dot(v, v)


def difference_quotient(f: Callable[[float], float], x: float, h: float) -> float:
	"""The derivative is defined as the limit of the differences of quotient"""
	return (f(x + h) - f(x)) / h


def square(x: float) -> float:
	return x * x


def derivative(x: float) -> float:
	return 2 * x


xs = range(-10, 11)
actuals = [derivative(x) for x in xs]
estimates = [difference_quotient(square, x, h=0.001) for x in xs]

plt.plot(xs, actuals, "rx", label="Actual")
plt.plot(xs, estimates, "b+", label="Estimates")
plt.title("Actual Derivatives vs Estimates")
plt.legend()
plt.show()


