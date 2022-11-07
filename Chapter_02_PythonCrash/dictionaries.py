# "Pythonic way of creating an empty dictionary
empty_dict = {}
print(empty_dict)
# Not that pythonic way
empty_dict2 = dict()
print(empty_dict2)

# Create a dictionary of grades
grades = {"Joel": 80, "Tim": 95}
print(grades)

# Retrieve the value of Tim
print(f"The grade of Tim is {grades['Tim']}")
print(f"The grade of Joel is {grades['Joel']}")

# If you ask for a key not present in a dictionary you'll get a KeyError message
try:
	kates_grade = grades["Kate"]
except KeyError:
	print("There is no grade for Kate")
print("=" * 30)
# get() method does not return error of key does not exist
joels_grade = grades.get("Joel", 0)
print(joels_grade)
kates_grade = grades.get("Kate", 0)
print(kates_grade)
no_ones_grade = grades.get("No One")
print(no_ones_grade)
print("=" * 30)
# Assign keys and values to dictionary
grades["Tim"] = 99
grades["Kate"] = 100
print(grades)

# Use dictionary for structural data
tweet = {
	"user": "joelgrus",
	"text": "Data Science is Awesome",
	"retweet_count": 100,
	"hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

print(tweet)
for i in tweet:
	print(f"{i}: {tweet[i]}")
print("=" * 30)
# Access keys, values and both
print(tweet.keys())
print("=" * 30)
print(tweet.values())
print("=" * 30)
print(tweet.items())
print("=" * 30)
for key, value in tweet.items():
	print(f"{key}: {value}")
print("=" * 30)
# Check for presence of keys and values in dictionary
print("user" in tweet)
print("joelgrus" in tweet)  # doesnt work this way
print("joelgrus" in tweet.values())
