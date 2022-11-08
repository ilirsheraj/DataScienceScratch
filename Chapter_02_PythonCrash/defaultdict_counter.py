# Different ways for word count using dictionaries
# 1 - Classical way
word_count = {}

for word in document:
	if word in word_count:
		word_count[word] += 1
	else:
		word_count = 1

# 2 - Forgiveness is better than permission approach
word_counts = {}

for word in document:
	try:
		word_counts[word] += 1
	except KeyError:
		word_counts[word] = 1

# 3 - Use get()
word_counts = {}

for word in document:
	previous_count = word_counts.get(word, 0)
	word_counts[word] = previous_count + 1

# 4 - defaultdict: It is a regular dictionary, except that when you try to look up a key it does not contain,
# it first adds a value for it using a zero-argument function you provided when you created it
from collections import defaultdict


word_counts = defaultdict(int)  # int() produces 0
for word in document:
	word_counts[word] += 1

# These are also useful with lists and dictinaries
dd_list = defaultdict(list)  # list() produces an empty list
dd_list[2].append(1)
print(dd_list)

dd_dict = defaultdict(dict)  # dict() produces an empty dictionary
dd_dict["Joel"]["City"] = "Seatle"
print(dd_dict)

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1
print(dd_pair)
print("=" * 30)

# Counters turn a sequence of values into a defaultdict(int)-like object mapping keys to counts
from collections import Counter


c = Counter([0, 1, 2, 0])  # will count how many times each integer is present in the list
print(c)

# Simple way to solve word count problem
word_count = Counter(document)

# It also has "most_common()" method that returns the most frequent occurrences of something
for word, count in word_count.most_common(10):  # 10 most common words
	print(word, count)
