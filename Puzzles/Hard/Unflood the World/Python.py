from collections import deque
from collections import defaultdict

# Form grid and find starting locations.
grid = []
starts = []
unflooded = 0
w, h = [int(i) for i in input().split()]
for i in range(h):
    row = []
    for j,val in enumerate(input().split()):
        hi = int(val)
        starts.append([hi,i,j])
        row.append(hi)
    grid.append(row)

# Find neighbours for all the tiles.
neighbours = defaultdict(list)
for i in range(h):
    for j in range(w):
        for y,x in [[0,1],[-1,0],[0,-1],[1,0]]:
            if 0<=i+y<h and 0<=j+x<w and grid[i][j] <= grid[i+y][j+x]:
                neighbours[(i,j)].append([i+y,j+x])

# Perform a BFS to find how many tiles to unflood.
queue = deque(sorted(starts))
while queue:
    val, i, j = queue.popleft()
    if grid[i][j] == "X":continue
    unflooded += 1

    new_queue = deque([[i,j]])
    while new_queue:
        new_i, new_j = new_queue.popleft()
        for y,x in neighbours[(new_i,new_j)]:
            if grid[y][x] != "X":
                new_queue.append([y,x])
                grid[y][x] = "X"

# Print the number to unflood.
print(unflooded)
