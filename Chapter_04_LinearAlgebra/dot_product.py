from typing import List
import math


vector = List[float]


def dot(v: vector, w: vector) -> float:
	"""Computes the dot product between two vectors"""
	assert len(v) == len(w), "vectors are not of the same length"
	return sum(v_i * w_i for v_i, w_i in zip(v, w))


dot_prod = dot([1, 2, 3], [4, 5, 6])
print(dot_prod)


# Use this function to compute the sum of squares
def sum_of_squares(v: vector) -> float:
	return dot(v, v)


ss = sum_of_squares([1, 2, 3])
print(ss)

# Now we can use the above function to compute the magnitude
def magnitude(v: vector) -> float:
	return math.sqrt(sum_of_squares(v))


mag_v = magnitude([1, 2, 3])
print(mag_v)
