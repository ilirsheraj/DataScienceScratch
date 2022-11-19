from typing import List
from math import sqrt


print("Dispersion refers to measures of how spread-out our data is")
num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11,
			   10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
			   9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6,
			   6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
			   4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
			   3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
			   1, 1, 1, 1, 1, 1, 1, 1, 1]


# Define a bunch of functions created in previous modules: They can be imported as well, but re-writing them is better
Vector = List[float]


def dot(v: Vector, w: Vector) -> float:
	"""Computes v_1 * w_1 + ... + v_n * w_n"""
	assert len(v) == len(w), "vectors must be same length"
	return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
	"""Returns v_1 * v_1 + ... + v_n * v_n"""
	return dot(v, v)


def mean(xs: List[float]) -> float:
	return sum(xs) / len(xs)


def quantile(xs: List[float], p: float) -> float:
	"""Returns the pth-percentile value in x"""
	p_index = int(p * len(xs))  # p_index is always the floor
	return sorted(xs)[p_index]


# define a function to calculate the range
def data_range(xs: List[float]) -> float:
	"""Returns the difference between the smallest and the largest data point"""
	return max(xs) - min(xs)


# Define functions to compute variance
def de_mean(xs: List[float]) -> List[float]:
	"""Translates xs by subtracting its mean so the result has mean zero"""
	x_bar = mean(xs)
	return [x - x_bar for x in xs]


def variance(xs: List[float]) -> float:
	"""Almost the average squared deviation from the mean"""
	assert len(xs) >= 2, "variance requires at least two numbers"

	n = len(xs)

	deviations = de_mean(xs)
	return sum_of_squares(deviations) / (n - 1)


# Define standard deviation
def standard_deviation(xs: List[float]) -> float:
	"""It is just the square root of variance"""
	return sqrt(variance(xs))


# Inter-quartile range
def interquartile_range(xs: List[float]) -> float:
	"""Returns the difference between 75th and 25th quantiles"""
	return quantile(xs, 0.75) - quantile(xs, 0.25)


print(f"The range of the number of friends is {data_range(num_friends)}")
print(f"The variance of number of friends is {variance(num_friends)}")
print(f"The standard deviation of number of friends is {standard_deviation(num_friends)}")
print(f"The inter-quartile range of number of friends is {interquartile_range(num_friends)}")
