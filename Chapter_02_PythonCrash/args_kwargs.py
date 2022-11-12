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


# This will not work for function with ke than one argument
def f2(x, y):
	return x + y


g = doubler(f2)
try:
	g(1, 2)
except TypeError:
	print("As defined, g takes only one argument")


# This can be handled with argument unpacking
def magic(*args, **kwargs):
	print("unnamed args:", args)
	print("keyword args:", kwargs)


print(magic(1, 2, key="word", key2="word2"))


# Another way:
def other_way_magic(x, y, z):
	return x + y + z


x_y_list = [1, 2]
z_dict = {"z": 3}
print(other_way_magic(*x_y_list, **z_dict))
