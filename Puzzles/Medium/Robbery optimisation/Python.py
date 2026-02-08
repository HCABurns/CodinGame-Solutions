# Get houses
n = int(input())
houses = [int(input()) for i in range(n)]

# Find the highest value given the neighbour constraint.
cache = {}
def search(pos):
    if pos in cache:
        return cache[pos]
    best = 0
    for i in range(pos+2,len(houses)):
        best = max(best, houses[i]+search(i))
    cache[pos] = best
    return best
# Print the result.
print(search(-2))
