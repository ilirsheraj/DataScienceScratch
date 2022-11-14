from typing import List
import math


vector = List[float]


def subtract(v: vector, w: vector) -> vector:
	"""Subtracts the corresponding elements"""
	# vectors must be of the same length
	assert len(v) == len(w)
	return [v_i - w_i for v_i, w_i in zip(v, w)]


def sum_of_squares(v: vector) -> float:
	return dot(v, v)


def magnitude(v: vector) -> float:
	return math.sqrt(sum_of_squares(v))


def squared_distance(v: vector, w: vector) -> float:
	"""Computes (v_1 - w_1)**2 + ... + (v_n - w_n)**2"""
	return sum_of_squares(subtract(v, w))


def distance(v: vector, w: vector) -> float:
	"""Computes the distance between v and w"""
	return math.sqrt(squared_distance(v, w))


def distance2(v: vector, w: vector) -> float:
	return magnitude(subtract(v, w))
