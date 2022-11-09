list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

print([pair for pair in zip(list2, list1)])

# unzip
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(letters)
print(numbers)

def my_addition(a, b):
	return a + b


print(my_addition(1, 2))

try:
	print(my_addition([1, 2]))
except TypeError:
	print("my_add expects two numbers")
	print(my_addition(*[1,2]))
