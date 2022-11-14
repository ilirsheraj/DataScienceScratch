from typing import List, Tuple, Callable


Matrix = List[List[float]]
Vector = List[float]

def make_matrix(num_rows: int, num_cols: int,
				entry_fn: Callable[[int, int], float]) -> Matrix:
	"""
	Returns a num_rows x num_cols matrix whose (i,j)-th entry is entry_fn(i,j)
	"""
	return [[entry_fn(i, j) for j in range(num_cols) for i in range(num_rows)]]


# Create a 5x5 identity matrix
def identity_matrix(n: int) -> Matrix:
	"""Returns an nxn identity matrix"""
	return make_matrix(n, n, lambda i, j: 1 if j == i else 0)


id_matrix = identity_matrix(5)
print(id_matrix)
