from typing import Tuple
import math
import random


# CDF was defined in the previous section, but let's define it again
def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
	"""A function to derive the cdf for any value of x if X is normally distributed"""
	return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


# define a function to derive a normal approximation to binomial
def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
	"""Returns mu and sigma corresponding to a certain Bernoulli(n, p)"""
	mu = n * p
	sigma = math.sqrt(n * p * (1 - p))
	return mu, sigma


# The normal CDF is the probability that the variable is below a certain threshold
normal_probability_below = normal_cdf


# Normal probability above the threshold
def normal_probability_above(lo: float, mu: float = 0, sigma: float = 1) -> float:
	"""The probability that an N(mu, sigma) is greater than lo"""
	return 1 - normal_cdf(lo, mu, sigma)


# It is between if it's less than high (hi), but not less than low
def normal_probability_between(lo: float, hi: float, mu: float = 0, sigma: float = 1) -> float:
	"""The probability that N(mu, sigma) is between lo and hi"""
	return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# It's outside and it's not between
def normal_probability_outside(lo: float, hi: float, mu: float = 0, sigma: float = 1) -> float:
	"""The probability that N(mu, sigma) is not between lo and hi"""
	return 1 - normal_probability_between(lo, hi, mu, sigma)


# Define the inverse cdf as well to be able to find the cut-offs of tails given the mean and probability of interest
def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001) -> float:
	"""Find the approximate inverse cdf using binary search"""
	# If not standard, compute the standard and rescale accordingly
	if mu != 0 or sigma != 1:
		return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

	low_z = -10.0  # close to zero
	high_z = 10.0  # close to 1
	mid_z = None

	while high_z - low_z > tolerance:
		mid_z = (low_z + high_z) / 2
		mid_p = normal_cdf(mid_z)
		if mid_p < p:
			low_z = mid_z
		else:
			high_z = mid_z

	return mid_z


# Define function for the normal upper bound
def normal_upper_bound(probability: float, mu: float = 0, sigma: float = 1) -> float:
	"""Returns the z for which P(Z <= z) = probability"""
	return inverse_normal_cdf(probability, mu, sigma)


# Define function for the normal lower bound
def normal_lower_bound(probability: float, mu: float = 0, sigma: float = 1) -> float:
	"""Returns the z for which P(Z => z) = probability"""
	return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bound(probability: float, mu: float = 0, sigma: float = 1) -> Tuple[float, float]:
	"""Returns the symmetric (about the mean) bounds that contain the specified probability"""
	tail_probability = (1 - probability) / 2

	# Upper bound should have probability above it
	upper_bound = normal_lower_bound(tail_probability, mu, sigma)

	# Lower bound should have probability below it
	lower_bound = normal_upper_bound(tail_probability, mu, sigma)

	return lower_bound, upper_bound


# Define function for p-value
def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
	"""Calculate how likely we are to see a value at least as extreme as x in either direction
	if our values are from an N(mu, sigma)
	"""
	if x >= mu:
		# x is greater than the mean, so the tail is everything greater than x
		return 2 * normal_probability_above(x, mu, sigma)

	else:
		# x is less than the mean, so the tail is everything less than x
		return 2 * normal_probability_below(x, mu, sigma)


if __name__ == "__main__":
	mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)  # 1000*0.5, sqrt(1000 * 0.5 * 0.5)
	print(mu_0, sigma_0)

	lower_bound, upper_bound = normal_two_sided_bound(0.95, mu_0, sigma_0)
	print(lower_bound, upper_bound)

	# Calculate the power of the test
	# 95% bounds based on the assumption p = 0.5
	lo, hi = normal_two_sided_bound(0.95, mu_0, sigma_0)
	print(lo, hi)

	# Actual mu and sigma based on p = 0.55
	mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
	print(mu_1, sigma_1)

	type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
	power = 1 - type_2_probability
	print(power)

	hi = normal_upper_bound(0.95, mu_0, sigma_0)

	type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
	power = 1 - type_2_probability
	print(power)

	# for 230 heads
	print(two_sided_p_value(529.5, mu_0, sigma_0))

	# To confirm p-value carry out a simulation
	extreme_value_count = 0
	for _ in range(1000):
		num_heads = sum(1 if random.random() < 0.5 else 0 for _ in range(1000))

		if num_heads >= 530 or num_heads <= 470:
			extreme_value_count += 1

	print(extreme_value_count / 1000)

	# Confidence Intervals for 525 coins
	p_hat = 525 / 1000
	mu = p_hat
	sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)
	print(f"The standard deviation for 525 heads in 1000 coin flips is {sigma}")
	print(f"The 95% confidence interval for 525 coin flips is {normal_two_sided_bound(0.95, mu, sigma)}")

	# Confidence interval for 540 heads in 1000 coin flips
	p_hat = 540 / 1000
	mu = p_hat
	sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)
	print(f"The standard deviation for 540 heads in 1000 coin flips is {sigma}")
	print(f"The 95% confidence interval for 540 coin flips is {normal_two_sided_bound(0.95, mu, sigma)}")



