from typing import Tuple
import math
from coin_flip import two_sided_p_value


def estimated_parameters(N: int, n: int) -> Tuple[float, float]:
	p = n / N
	sigma = math.sqrt(p * (1 - p) / N)
	return p, sigma


def a_b_test_statistic(N_A: int, n_A: int, N_B: int, n_B: int) -> float:
	p_A, sigma_A = estimated_parameters(N_A, n_A)
	p_B, sigma_B = estimated_parameters(N_B, n_B)
	return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

z = a_b_test_statistic(1000, 200, 1000, 180)
print(two_sided_p_value(z))

# Try another one
z = a_b_test_statistic(1000, 200, 1000, 150)
print(two_sided_p_value(z))
