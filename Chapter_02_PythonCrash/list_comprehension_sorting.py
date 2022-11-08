# Sorting lists
x = [4, 1, 2, 3]
y = sorted(x)  # create new list
print(x)
print(y)
x.sort()  # sort in place
print(x)
x.sort(reverse=True)
print(x)

# sort list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
print(x)

# List Comprehension
even_numbers = [x for x in range(5) if x%2 == 0]
print(even_numbers)
squares = [x**2 for x in range(5)]
print(squares)
even_squares = [x**2 for x in range(5) if x % 2 == 0]
print(even_squares)
print("=" * 30)
# turn list to dictionary
square_dict = {x: x ** 2 for x in range(5)}
print(square_dict)
square_set = {x ** 2 for x in range(5)}
print(square_set)

# list with same length as even numbers set
zeros = [0 for _ in even_numbers]
print(zeros)

# nested list comprehension
pairs = [(x, y) for x in range(10) for y in range(10)]
print(pairs)
print(len(pairs))

increasing_pairs = [(x, y) for x in range(10) for y in range(x + 1, 10)]
print(increasing_pairs)
print(len(increasing_pairs))
