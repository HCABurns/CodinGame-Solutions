# Get values and store.
n = int(input())
values = {}
numbers = []
for idx,i in enumerate(input().split()):
    l = int(i)
    if l not in numbers: numbers += [l]
    if l not in values:
        values[l] = []
    values[l] += [idx]

# Find the maximum-length incrementing sequence with lowest starting value.
max_l = 0
max_r = [999999]
for num in numbers:
    v = num
    idx = values[v][0]
    l_r = [v]
    while v+1 in values and any(values[v+1][kk] > idx for kk in range(len(values[v+1]))):
        idx = next(values[v+1][kk] for kk in range(len(values[v+1])) if values[v+1][kk] > idx)
        v += 1
        l_r += [v]
    max_r = min(max_r, l_r , key = lambda x : (-len(x),x[0]))

# Print the values.
print(*max_r)
