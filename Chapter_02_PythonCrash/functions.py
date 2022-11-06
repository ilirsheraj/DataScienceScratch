def double(x):
	"""
	This function multiplies its input by 2
	:param x: integer or float
	:return: integer or float
	"""
	return x * 2


# Python functions are `First Class`: We can assign them to variables and pass them into functions
# just like any other argument.

def apply_to_one(f):
	"""Calls the function f with 1 as it's argument"""
	return f(1)


my_double = double
x = apply_to_one(my_double)
print(x)

# Use lambda
y = apply_to_one(lambda x: x + 4)
print(y)

# Functions with default arguments
def my_print(message = "my default message"):
	print(message)


my_print()
my_print("hello there")

# Specify arguments by name
def full_name(first = "whats your name", last = "Something"):
	return first + " " + last


print(full_name("Ilir", "Sheraj"))
print(full_name("Ilir"))
print(full_name(last= "Sheraj"))
