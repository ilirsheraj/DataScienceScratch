from typing import List, Tuple


Matrix = List[List[float]]
Vector = List[float]

A = [[1, 2, 3],
	 [4, 5, 6]]
print(A)

B = [[1, 2],
	 [3, 4],
	 [5, 6]]
print(B)


def shape(A: Matrix) -> Tuple[int, int]:
	"""Returns (# of rows of A, # of columns of A"""
	num_rows = len(A)
	num_cols = len(A[0]) if A else 0
	return num_rows, num_cols


M = [[1, 2, 3],
	 [4, 5, 6]]
print(shape(A))


def get_row(A: Matrix, i: int) -> Vector:
	"""Returns the ith row of A as a vector"""
	return A[i]


def get_column(A: Matrix, j: int) -> Vector:
	"""Returns the jth column of A as a vector"""
	return [A_i[j] for A_i in A]


print(get_row(A, 1))
print(get_column(A, 1))
