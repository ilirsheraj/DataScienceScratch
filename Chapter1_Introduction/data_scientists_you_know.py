from collections import defaultdict, Counter


# List of tuples: number is the user ID, and interest
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"), (1, "NoSQL"),
    (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
    (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data"),
]

for i in interests:
    print(i)
print("=" * 50)

# Create a dictionary of interest as key and user_id as value
user_ids_by_interest = defaultdict(list)
print(user_ids_by_interest)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
print(user_ids_by_interest)
print("=" * 50)

# Create a dictionary of user_ids as key and interest as value
interest_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interest_by_user_id[user_id].append(interest)
print(interest_by_user_id)
print("=" * 50)


# Find out who has the most interests in common with a user
def most_common_interests_with(user):
    return Counter(
        interested_user_id for interest in interest_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )


# Find data scientists with common interests
def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interest."""
    return [user_id for user_id, user_interest in interests if user_interest == target_interest]


# Count the number of words in the list above to find the most popular subject
words_and_counts = Counter(
	word for user, interest in interests for word in interest.lower().split()
)
print(words_and_counts)
print("=" * 50)

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
