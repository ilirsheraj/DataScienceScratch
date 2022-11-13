def add(a, b):
	return a + b


print(add(10, 5))
print(add([1, 2], [3]))
print(add("hi ", "there"))

try:
	print(add(10, "five"))
except TypeError:
	print("cannot add an int to a str")

# A better way would be to annotate the types of objects in a function
def add(a: int, b: int) -> int:
	return a + b


print(add(10, 5))
# You get warning, but program works normally
print(add("Hi ", "there"))

# At least 4 reasons to use type annotation
# 1 - Types are important types of documentation
def dot_product(x: Vector, y: Vector) -> float:
	return x @ y


# 2 - There are external tools that will read your code , inspect type annotations
# and let you know about type errors before you ever run the code, such as `mypy`.

# Having to think about the types in your code forces you to design cleaner functions and interfaces

# Using types allows your editor to help you with htings like autocomplete and get angry at your type errors

# Lets annotate a list
def total(xs: list) -> float:
	return sum(total)


# To make it better:
from typing import List


def total(xs: list[float]) -> float:
	return sum(total)


# We can do variable annotation but that is not necessary
a: int = 5

# When this is not obvious we provide inline type hints
from typing import Optional
values: List[int] = []
best_so_far: Optional[float] = None
