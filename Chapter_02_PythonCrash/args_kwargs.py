def doubler(f):
	"""Define a new function that keeps a referenc eof f"""
	def g(x):
		return 2 * f(x)
	# Return the new function
	return g


# This works in some cases
def f1(x):
	return x + 1

g = doubler(f1)
print(g(3))  # (3 + 1) * 2
print(g(-1))  # (-1 + 1) * 2
