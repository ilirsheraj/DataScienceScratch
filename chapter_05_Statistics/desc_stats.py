num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11,
			   10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
			   9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6,
			   6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
			   4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
			   3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
			   1, 1, 1, 1, 1, 1, 1, 1, 1
			   ]


# Some descriptive statistics
# 1 - Number of data points
num_points = len(num_friends)
print(f"There are {num_points} data points in this sample")

# 2 - The largest value
largest_value = max(num_friends)
print(f"The largest value is {largest_value}")

# 3 - The smallest value
smallest_value = min(num_friends)
print(f"The smallest value is {smallest_value}")

# 4 - Sort the values
sorted_values = sorted(num_friends)
print(f"The smallest value after sorting is {sorted_values[0]}")
print(f"The largest value after sorting is {sorted_values[-1]}")
print(f"The second smallest value is {sorted_values[1]}")
print(f"The largest second value is {sorted_values[-2]}")
