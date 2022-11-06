# Import the module itself
import re
# Import alias
import re as regex
# For long names
import matplotlib.pyplot as plt
# Import specific modules from library
from collections import defaultdict, Counter
# Import everything: not advisable
from re import *


my_regex = re.compile("[0-9]+", re.I)
print(my_regex)

my_regex = regex.compile("[0-9]+", regex.I)
print(my_regex)

lookup = defaultdict(int)
my_counter = Counter()
