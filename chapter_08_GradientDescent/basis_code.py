from typing import List, Callable, Tuple
import math


Vector = List[float]
Matrix = List[List[float]]
def dot(v: Vector, w: Vector) -> float:
	"""Computes the dot product of two vectors"""
	assert len(v) == len(w), "Vectors must be the same length"
	return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
	"""Computes the sum of squared elements in v"""
	return dot(v, v)


def difference_quotient(f: Callable[[float], float], x: float, h: float) -> float:
	"""The derivative is defined as the limit of the differences of quotient"""
	return (f(x + h) - f(x)) / h


def square(x: float) -> float:
	return x * x


def derivative(x: float) -> float:
	return 2 * x


def add(v: Vector, w: Vector) -> Vector:
	"""Adds corresponding elements"""
	assert len(v) == len(w), "vectors must be the same length"
	return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
	"""Subtracts corresponding elements"""
	assert len(v) == len(w), "vectors must be the same length"
	return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: List[Vector]) -> Vector:
	"""Sums all corresponding elements"""
	# Check that vectors is not empty
	assert vectors, "no vectors provided!"

	# Check the vectors are all the same size
	num_elements = len(vectors[0])
	assert all(len(v) == num_elements for v in vectors), "different sizes!"

	# the i-th element of the result is the sum of every vector[i]
	return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


def scalar_multiply(c: float, v: Vector) -> Vector:
	"""Multiplies every element by c"""
	return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
	"""Computes the element-wise average"""
	n = len(vectors)
	return scalar_multiply(1 / n, vector_sum(vectors))


def magnitude(v: Vector) -> float:
	"""Returns the magnitude (or length) of v"""
	return math.sqrt(sum_of_squares(v))  # math.sqrt is square root function


def squared_distance(v: Vector, w: Vector) -> float:
	"""Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
	return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
	"""Computes the distance between v and w"""
	return math.sqrt(squared_distance(v, w))


def distance(v: Vector, w: Vector) -> float:  # type: ignore
	return magnitude(subtract(v, w))


def shape(A: Matrix) -> Tuple[int, int]:
	"""Returns (# of rows of A, # of columns of A)"""
	num_rows = len(A)
	num_cols = len(A[0]) if A else 0  # number of elements in first row
	return num_rows, num_cols


def get_row(A: Matrix, i: int) -> Vector:
	"""Returns the i-th row of A (as a Vector)"""
	return A[i]  # A[i] is already the ith row


def get_column(A: Matrix, j: int) -> Vector:
	"""Returns the j-th column of A (as a Vector)"""
	return [A_i[j]  # jth element of row A_i
			for A_i in A]  # for each row A_i


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
	"""
	Returns a num_rows x num_cols matrix
	whose (i,j)-th entry is entry_fn(i, j)
	"""
	return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
	"""Returns the n x n identity matrix"""
	return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
	"""Moves `step_size` in the gradient direction from v"""
	assert len(v) == len(gradient)
	step = scalar_multiply(step_size, gradient)
	return add(v, step)


def linear_gradient(x: float, y: float, theta:Vector) -> Vector:
	slope, intercept = theta
	predicted = slope * x + intercept
	error = (predicted - y)
	squared_error = error ** 2
	grad = [2 * error * x, 2 * error]
	return grad


def minibatches(dataset: List[T], batch_size: int, shuffle: bool=True) -> Iterator[List[T]]:
	"""The function generates batch_size minibatches from the dataset"""
	# start indexes 0, batch_size, 2 * batch_size,...
	batch_starts = [start for start in range(0, len(dataset), batch_size)]
	if shuffle:
		random.shuffle(batch_starts)

	for start in batch_starts:
		end = start + batch_size
		yield dataset[start:end]
