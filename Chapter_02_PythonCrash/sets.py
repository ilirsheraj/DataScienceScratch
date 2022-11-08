# set represents a collection of distinct elements
primes_below_10 = {2, 3, 5, 7}
print(primes_below_10)

# empty set
s = set()
print(s)
s.add(1)
print(s)
s.add(2)
print(s)
s.add(2)
print(s)

x = len(s)
print(x)

print(2 in s)
print(3 in s)

# Quicker than lists to check for membership
stopwords_list = ["a", "an", "at"] + ["yet", "you"]
print(stopwords_list)
print("zip" in stopwords_list)

stopword_set = set(stopwords_list)
print("zip" in stopword_set)

# Find distinct items in a collection
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
print(num_items)

item_set = set(item_list)
print(item_set)

num_distinct_items = len(item_set)
print(num_distinct_items)

distinct_item_list = list(item_set)
print(distinct_item_list)
