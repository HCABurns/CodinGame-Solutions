# Get inputs.
a1 = int(input())
n = int(input())

# Create hashmap for storing indexes.
hashmap = {}

# Complete sequence.
for i in range(n-1):
    if a1 not in hashmap:
        hashmap[a1] = i
        a1 = 0
    else:
        diff = i - hashmap[a1]
        hashmap[a1] = i
        a1 = diff

# Output the new result.
print(a1)
