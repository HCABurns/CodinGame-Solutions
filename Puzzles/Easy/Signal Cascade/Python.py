from collections import deque

# Form grid and get starting position.
grid = []
h, w = [int(i) for i in input().split()]
for i in range(h):
    row = input()
    grid.append([int(char) for char in row])
r, c = [int(i) for i in input().split()]

# Simulate the cascading overload.
directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1], [1,-1], [-1,1]]
queue = deque([(r,c)])
overloaded = set()
while queue:
    i,j = queue.popleft()
    if (i,j) in overloaded:
        continue
    grid[i][j] += 1

    # Overload occurred.
    if grid[i][j] == 10:
        grid[i][j] = 0
        overloaded.add((i,j))

        for di, dj in directions:
            ni, nj = i+di, j+dj
            if ni >= 0 and ni < h and nj >= 0 and nj < w and (ni,nj) not in overloaded:
                queue.append((ni,nj))

# Print result.
for row in grid:
    print("".join([str(i) for i in row]))
