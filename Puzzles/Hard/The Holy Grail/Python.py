from collections import deque

# Form Grid.
w, h = [int(i) for i in input().split()]
grid = [[" " for i in range(w)]for i in range(h)]
grid[0][0] = "#"
grid[h-1][w-1] = "#"

# BFS to find if they connect to the start or not.
def bfs(i,j):
    queue = deque([[i,j]])
    start = False
    end = False
    seen = set((i,j))
    while queue:
        y,x = queue.pop()
        if y==x==0:start=True
        if y==h-1 and x==w-1:end=True
        if start and end:
            return True

        for dy,dx in [[0,1],[-1,0],[0,-1],[1,0]]:
            ny, nx = y+dy, x+dx
            if 0<=ny<h and 0<=nx<w and grid[ny][nx] == "#" and (ny,nx) not in seen:
                seen.add((ny,nx))
                queue.append([ny,nx])
    return False

# Get tiles and check if a path has been created.
moves = 0
while True:
    x, y = [int(j) for j in input().split()]
    grid[y][x] = "#"
    moves+=1
    if bfs(y,x):
        break

# Print number of tiles to create a path.
print(moves)
