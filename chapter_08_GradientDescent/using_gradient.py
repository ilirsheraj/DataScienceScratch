import random
from typing import List
from basis_code import distance, add, scalar_multiply, vector_mean


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


def linear_gradient(x: float, y: float, theta:Vector) -> Vector:
	slope, intercept = theta
	predicted = slope * x + intercept
	error = (predicted - y)
	squared_error = error ** 2
	grad = [2 * error * x, 2 * error]
	return grad


theta = [random.uniform(-1, 1), random.uniform(-1,1)]
learning_rate = 0.001

inputs = [(x, 20 * x + 5) for x in range(-50, 50)]
for epochs in range(5000):
	# compute gradient mean
	grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
	# Take a step in that direction
	theta = gradient_step(theta, grad, -learning_rate)
	print(epochs, theta)
