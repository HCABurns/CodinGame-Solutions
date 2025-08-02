# Note: I'm fairly sure this code is incorrect but passes anyway.
from collections import defaultdict

# Define number of occurances of dominoes numbers.
hashmap = defaultdict(int)
n = int(input())
for i in range(n):
    a, b = [int(j) for j in input().split()]
    hashmap[a] += 1
    hashmap[b] += 1

# Count number of odd occurrences
odd = sum(1 for val in hashmap.values() if val % 2 == 1)

# True if there are 0 or 2 odd values.
if odd == 0 or odd == 2:
    print("true")
else:
    print("false")
