def generate_range(n):
	i = 0
	while i < n:
		yield i
		i += 1


for i in generate_range(5):
	print(f"i: {i}")

# Infinite sequence
def natural_numbers():
	"""Returns natural numbers"""
	n = 1
	while True:
		yield n
		n += 1


even_below_20 = (i for i in generate_range(20) if i % 2 == 0)
print(even_below_20)

data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
evens_square = (x ** 2 for x in evens)
evens_square_ending_in_six = (x for x in evens_square if x % 10 == 6)

# enumerate
names = ["Alice", "Bob", "Charlie", "Debie"]
for i, name in enumerate(names):
	print(f"name {i + 1} is {name}")
