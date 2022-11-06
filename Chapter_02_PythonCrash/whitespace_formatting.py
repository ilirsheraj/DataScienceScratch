for i in [1, 2, 3, 4, 5]:
	print(i)
	for j in [1, 2, 3, 4, 5]:
		print(j)
		print(i + j)
	print(i)
print("done looping")
print("=" * 20)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_lists)
easier_to_read_list_of_lists = [[1, 2, 3],
								[4, 5, 6],
								[7, 8, 9]]
print(easier_to_read_list_of_lists)

# Use backslash for new line if it becomes too long
two_plus_three = 2 + \
	3
print(two_plus_three)
