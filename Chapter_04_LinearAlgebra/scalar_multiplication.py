from typing import List


vector = List[float]


def scalar_multiply(c: float, v: vector) -> vector:
	"""Multiplies every element by c"""
	return [c * v_i for v_i in v]


vec = [1, 2, 3, 4, 5]
print(vec)
scl = 3
print(scl)
scalar = scalar_multiply(scl, vec)
print(scalar)
