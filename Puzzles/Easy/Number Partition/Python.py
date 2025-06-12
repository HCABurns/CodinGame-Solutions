# Target Value
n = int(input())

# Set for storing partition.
result = set()

# DFS to find the partitions which add to n.
def search(value, k,  path):
    if value == n:
        result.add(tuple(sorted(path,reverse=True)))

    if value > n:
        return

    for i in range(k,n+1):
        search(value+i, i, path+[i])
search(0, 1, [])

# Print in reverse order.
res = sorted(list(result),reverse = True)
for i in res:
    print(*i)
