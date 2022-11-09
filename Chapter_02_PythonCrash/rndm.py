import random


random.seed(10)
# random numbers between 0 and 1
uniform_randoms = [random.random() for _ in range(4)]
print(uniform_randoms)

random.seed(10)
print(random.random())
random.seed(10)
print(random.random())

# produce a random number from a given range
a = random.randrange(10)
print(a)
b = random.randrange(3, 6)
print(b)

# random.shuffle() rearranges elements of a list
up_to_10 = [i for i in range(11)]
print(up_to_10)
random.shuffle(up_to_10)
print(up_to_10)

# randomly pick an element from a list
best_friend = random.choice(["ALice", "Bob", "Charlie"])
print(best_friend)

# Choose sample without replacement
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)

# Sample with replacement
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)
