# Chapter 1: Introduction
from collections import Counter


# Create a list for users
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]
print(users)
print("=" * 50)

# Create a list of tuples representing friendships.
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9),
                    ]

print("Friendship pairs are: ")
print(friendship_pairs)
print("=" * 50)

# Initialize a dictionary with an empty list for each user ID
print("Here is an empty dictionary representing the pairs of friends: ")
friendships = {user["id"]: [] for user in users}
print(friendships)
print("=" * 50)

# Loop over the friendship pairs to fill the dictionary
# As a list of tuples, the numbers can be pulled in double
print("Fill the dictionary by unpacking the tuple: ")
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
print(friendships)
print("=" * 50)


# Find the total number of connections
def number_of_friends(user):
    """
	How many friends does the user have
	"""
    user_id = user["id"]
    friend_id = friendships[user_id]
    return len(friend_id)


total_connections = [number_of_friends(user) for user in users]
print(total_connections)
print(f"There are {sum(total_connections)} connections")
print(f"The average number of connections is {sum(total_connections) / len(total_connections)}")
print("=" * 50)

# Create a list of user ID and number of friends to sort them by friend number
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(num_friends_by_id)
num_friends_by_id.sort(key=lambda id_and_friends:id_and_friends[1], reverse=True)
print("Each pair is (user_id, num_friends){}".format(num_friends_by_id))
print("=" * 50)


# Data Scientists you may know: find friends of friends
def foaf_ids_bad(user):
    """
    foaf is short for friend of a friend
    """
    return [foaf_id for friend_id in friendships[user["id"]] for foaf_id in friendships[friend_id]]


print(foaf_ids_bad(users[0]))
print("=" * 50)

# The results above show that we are double-counting so we need to remove it
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
            foaf_id
            for friend_id in friendships[user_id]
            for foaf_id in friendships[friend_id]
            if foaf_id != user_id and foaf_id not in friendships[user_id]
            )


print(f"User 'Chi' has these mutual friends {friends_of_friends(users[3])}")
