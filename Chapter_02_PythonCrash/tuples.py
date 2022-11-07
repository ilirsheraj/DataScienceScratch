my_tuple = (1, 2)
print(my_tuple)

try:
	my_tuple[1] = 3
except TypeError:
	print("You cannot modify a tuple")


def sum_and_product(x, y):
	return (x + y), (x * y)


sp = sum_and_product(2, 3)
print(sp)
s, p = sum_and_product(2, 10)
print(s)
print(p)

print("Multiple Assignment")
x, y = 1, 2
print(x, y)
x, y = y, x
print(x, y)
