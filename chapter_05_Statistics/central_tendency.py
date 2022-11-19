from typing import List
from collections import Counter


num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11,
			   10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
			   9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6,
			   6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
			   4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
			   3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
			   1, 1, 1, 1, 1, 1, 1, 1, 1]


# Define a function to calculate the mean
def mean(xs: List[float]) -> float:
	return sum(xs) / len(xs)


def _median_odd(xs: List[float]) -> float:
	"""If len of xs is odd, median is the middle point"""
	return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
	"""If len of xs is even, median is the average of the two middle elements"""
	sorted_x = sorted(xs)
	hi_midpoint = len(xs) // 2
	return (sorted_x[hi_midpoint - 1] + sorted_x[hi_midpoint]) / 2


def median(xs: List[float]) -> float:
	"""Finds the middle-most value of v"""
	return _median_even(xs) if len(xs) % 2 == 0 else _median_odd(xs)


def quantile(xs: List[float], p: float) -> float:
	"""Returns the pth-percentile value in x"""
	p_index = int(p * len(xs))  # p_index is always the floor
	return sorted(xs)[p_index]


def mode(xs: List[float]) -> List[float]:
	"""Returns a list since there may be more than one mode"""
	counts = Counter(xs)
	max_count = max(counts.values())
	return [x_i for x_i, count in counts.items() if count == max_count]


print(f"The mean of the number of friends is {mean(num_friends)}")
print(f"The median of the number of friends is {median(num_friends)}")
print(f"The 10th percentile in number of friends is {quantile(num_friends, 0.1)}")
print(f"The 25th percentile in number of friends is {quantile(num_friends, 0.25)}")
print(f"The 50th percentile in number of friends is {quantile(num_friends, 0.50)}")
print(f"The 75th percentile in number of friends is {quantile(num_friends, 0.75)}")
print(f"The mode of number of friends is {set(mode(num_friends))}")
