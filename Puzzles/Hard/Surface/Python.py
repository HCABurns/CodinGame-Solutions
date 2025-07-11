from collections import deque

# form the grid.
grid = []
l = int(input())
h = int(input())
for i in range(h):
    row = input()
    grid += [list(row)]

# Perform a BFS with flood fill.
def bfs(y,x, visited):
    queue = deque([[y,x]])
    while queue:
        y,x = queue.popleft()
        for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            ny = dy + y
            nx = dx + x
            if (ny,nx) not in visited and 0 <= ny < h and 0<=nx<l and grid[ny][nx] == "O":
                visited.add((ny,nx))
                queue.append([ny,nx])
    # Set coordinates in lake to max size.
    size = len(visited)
    for y,x in list(visited):
        grid[y][x] = size  
    return size  

# Check provided coordinates for the lake sizes.
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    if grid[y][x] == "#":
        print(0)
    elif grid[y][x] != "O":
        print(grid[y][x])
    else:
        print(bfs(y, x, {(y,x)}))
