from typing import List


vector = List[float]
print(vector)

# a 3D vector
height_weight_age = [70, 170, 48]
print(height_weight_age)

# a 4D vector
grades = [95, 80, 75, 62]
print(grades)

# Vectors are added component-wise
def add(v: vector, w: vector) -> vector:
	"""Adds the corresponding elements"""
	# vectors must be of the same length
	assert len(v) == len(w)
	return [v_i + w_i for v_i, w_i in zip(v, w)]


a = [1, 2, 3]
b = [4, 5, 6]
vector_sum = add(a, b)
print(vector_sum)


def subtract(v: vector, w: vector) -> vector:
	"""Subtracts the corresponding elements"""
	# vectors must be of the same length
	assert len(v) == len(w)
	return [v_i - w_i for v_i, w_i in zip(v, w)]


c = [5, 7, 9]
vector_diff = subtract(c, b)
print(vector_diff)
