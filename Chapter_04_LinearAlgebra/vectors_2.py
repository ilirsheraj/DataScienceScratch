from typing import List


vector = List[float]
# Summing a list of vectors
def vector_sum(vectors: List[vector]) -> vector:
	""" Sums all the corresponding elements"""
	# Make sure the vector is not empty
	assert vectors, "no vectors provided"

	# make sure all vectors are of the same size
	num_elements = len(vectors[0])
	assert all(len(v) == num_elements for v in vectors), "different sizes"

	return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

vec_sum = vector_sum([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
print(vec_sum)
