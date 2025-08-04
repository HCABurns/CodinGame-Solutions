n = int(input())

# Convert data to correct format.
def value(s):
    try:return float(s)
    except:return sum([ord(c) for c in s])

# Read in data and sort for comparison.
arr = [value(input()) for i in range(n)]
temp = sorted(arr)

# Hashing elements with their correct positions
pos = {}
for i in range(len(arr)):
    pos[arr[i]] = i

# Find minimum number of swaps.
swaps = 0
for i in range(len(arr)):
    if temp[i] != arr[i]:
        # Index of the element that should be at index i.
        ind = pos[temp[i]]
        arr[i], arr[ind] = arr[ind], arr[i]

        # Update the indices in the dictionary
        pos[arr[i]] = i
        pos[arr[ind]] = ind

        swaps += 1

# Print -1 if duplicate in array otherwise minimum swaps.
if len(set(arr)) == len(arr):
    print(swaps)
else:print(-1)
