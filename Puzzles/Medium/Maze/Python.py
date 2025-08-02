from collections import deque

# Form the grid.
w, h = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]
grid = []
for i in range(h):
    r = list(input())
    grid += [r]

# BFS to find the exits.
queue = deque([[y,x]])
ends = []
visited = set((y,x))
directions = [[0,1],[1,0],[0,-1],[-1,0]]
while queue:
    y,x = queue.popleft()

    if grid[y][x] == "." and (y == 0 or y == h-1 or x == 0 or x == w-1):
        ends.append([x,y])
        grid[y][x] = "#"

    for dy,dx in directions:
        ny, nx = y+dy, x+dx
        if 0 <= ny < h and 0 <= nx < w and (ny,nx) not in visited and grid[ny][nx] == ".":
            queue.append([ny,nx])
            visited.add((ny,nx))

# Sort and print.
ends.sort()
ends = [str(x)+" "+str(y) for x,y in ends]
print(len(ends))
if ends:
    print(*ends, sep = "\n")
