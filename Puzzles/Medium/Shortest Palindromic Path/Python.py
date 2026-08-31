import heapq

# Form grid.
n = int(input())
start = [int(i) - 1 for i in input().split()]
end = [int(i) - 1 for i in input().split()]
grid = "".join([input() for _ in range(n)])
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

# Define neighbours.
neighbours = [[] for _ in range(n * n)]
for i in range(n):
    for j in range(n):
        pos = i * n + j
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                neighbours[pos].append(pos + n * di + dj)

# Get starting positions.
v1 = start[0] * n + start[1]
v2 = end[0] * n + end[1]
if v1 > v2:
    v1, v2 = v2, v1

# A* BFS to find probable shortest path.
keyMultiplier = n * n
visited = {v1 * keyMultiplier + v2}
queue = [(2, 2, v1, v2)]
def score(a,b):
    return (abs(a//n - b//n) + abs(a%n - b%n))
while queue:
    _, length, a, b = heapq.heappop(queue)
    distance = abs(a // n - b // n) + abs(a % n - b % n)
    if distance <= 1:
        print(length - (distance == 0))
        break

    for nv1 in neighbours[a]:
        for nv2 in neighbours[b]:
            if grid[nv1] != grid[nv2]:
                continue
            n1, n2 = (nv1, nv2) if nv1 < nv2 else (nv2, nv1)
            key = n1 * keyMultiplier + n2
            if key not in visited:
                visited.add(key)
                heapq.heappush(queue, (length+score(n1,n2), length + 2, n1, n2))
