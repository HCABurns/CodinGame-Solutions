from collections import deque

# Define queue and ids of bases.
queue = deque()
ids = {}
chars = set()
_id = 0

# Define grid and tower ids.
grid = []
w = int(input())
h = int(input())
for i in range(h):
    line = input()
    grid.append(list(line))
    for j,char in enumerate(line):
        if char not in ".#":
            queue.append([_id,i,j])
            ids[_id] = char
            chars.add(char)
            _id += 1

# Perform BFS extending soldiers from the bases.
while queue:
    tmp = deque()
    while queue:
        _id, i, j = queue.popleft()

        for y,x in [[0,1],[-1,0],[0,-1],[1,0]]:
            ny, nx = y+i, j+x

            if 0<=ny<h and 0<=nx<w and grid[ny][nx] != "#":
                if grid[ny][nx] in chars or grid[ny][nx] == "+":
                    continue
                
                if grid[ny][nx] == ".":
                    grid[ny][nx] = _id
                elif grid[ny][nx] != _id:
                    grid[ny][nx] = "+"
                tmp.append([_id, ny,nx])
    
    queue = tmp
    for i,row in enumerate(grid):
        for j,char in enumerate(row):
            if char in ids:
                grid[i][j] = ids[char]

# Print grid.
for row in grid:
    print("".join(row))
