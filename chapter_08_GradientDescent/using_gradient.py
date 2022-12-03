import random
from typing import List
from basis_code import distance, add, scalar_multiply


Vector = List[float]
def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
	"""Moves `step_size` in the gradient direction from v"""
	assert len(v) == len(gradient)
	step = scalar_multiply(step_size, gradient)
	return add(v, step)


def sum_of_squares_gradient(v: Vector) -> Vector:
	return [2 * v_i for v_i in v]


# Pick a random starting point
v = [random.uniform(-10, 10) for i in range(3)]
print(v)

# The higher the number of epochs, the closer v gets to zero
for epoch in range(1000):
	grad = sum_of_squares_gradient(v)
	v = gradient_step(v, grad, -0.01)
	print(epoch, v)

print(distance(v, [0, 0, 0]))
