import random
from typing import TypeVar, List, Iterator
from basis_code import distance, add, scalar_multiply, vector_mean, linear_gradient, gradient_step


T = TypeVar('T')  # This allows us to use "generic" functions


def minibatches(dataset: List[T], batch_size: int, shuffle: bool=True) -> Iterator[List[T]]:
	"""The function generates batch_size minibatches from the dataset"""
	# start indexes 0, batch_size, 2 * batch_size,...
	batch_starts = [start for start in range(0, len(dataset), batch_size)]
	if shuffle:
		random.shuffle(batch_starts)

	for start in batch_starts:
		end = start + batch_size
		yield dataset[start:end]


inputs = [(x, 20 * x + 5) for x in range(-50, 50)]
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
learning_rate = 0.001

for epoch in range(1000):
	for batch in minibatches(inputs, batch_size=20):
		grad = vector_mean([linear_gradient(x, y, theta) for x, y in batch])
		theta = gradient_step(theta, grad, -learning_rate)
	print(epoch, theta)

slope, intercept = theta
print(slope, intercept)


# Stochastic Gradient Descent
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
inputs = [(x, 20 * x + 5) for x in range(-50, 50)]
for epoch in range(100):
	for x, y in inputs:
		grad = linear_gradient(x, y, theta)
		theta = gradient_step(theta, grad, - learning_rate)
	print(epoch, theta)

slope, intercept = theta
print(slope, intercept)
