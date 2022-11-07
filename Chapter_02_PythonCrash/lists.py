# List: An ordered collection of elements
integer_list = [1, 2, 3]
print(integer_list)
heterogeneous_list = ["string", 0.1, True]
print(heterogeneous_list)
print("=" * 20)

list_of_lists = [integer_list, heterogeneous_list, []]
for i in list_of_lists:
	print(i)
print("=" * 20)

list_length = len(integer_list)
print(list_length)

list_sum = sum(integer_list)
print(list_sum)
print("=" *30)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x)
print(f"First element is {x[0]}")
print(f"Second element is {x[1]}")
print(f"The last element is {x[-1]}")
print(f"One before last is {x[-2]}")
print("mutate the first element to -1")
x[0] = -1
print(x)
print("=" * 30)

print("List slicing operations")
print(f"First three elements {x[:3]}")
print(f"Elements 3 to end {x[3:]}")
print(f"Elements 1 to 4 included {x[1:5]}")
print(f"Last three elements {x[-3:]}")
print(f"Remove first and lat {x[1:-1]}")
print(f"Copy all x {x[:]}")
print(f"Every third element {x[::3]}")
print(f"Elements in reverse {x[5:2:-1]}")
print(f"Is 1 in [1, 2, 3] {1 in [1, 2, 3]}")
print(f"Is 0 in [1, 2, 3] {0 in [1, 2, 3]}")
print("=" * 30)

print("Modify list in place")
x = [1, 2, 3]
x.extend([4, 5, 6])
print(x)

print("Keep the original list")
x = [1, 2, 3]
y = x + [4, 5, 6]
print(y)

print("extend list using append() method")
x = [1, 2, 3]
x.append(0)
print(x)
print(len(x))
print("=" * 30)

print("Unpack lists")
x, y = [1, 2]
print(x)
print(y)
