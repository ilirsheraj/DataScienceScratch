import math


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
	"""A function to derive the cdf for any value of x if X is normally distributed"""
	return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p: float,
					   mu: float = 0,
					   sigma: float = 1,
					   tolerance: float = 0.00001) -> float:
	"""Find the approximate inverse cdf using binary search"""
	# If not standard, compute the standard and rescale accordingly
	if mu != 0 or sigma != 1:
		return mu + sigma * inverse_normal_cdf(p, tolerance = tolerance)

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

x = inverse_normal_cdf(0.8)
print(x)
