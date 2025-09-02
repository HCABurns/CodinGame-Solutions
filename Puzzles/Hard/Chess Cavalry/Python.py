from collections import defaultdict

# Form grid and find starting position of the knight.
start = [0,0]
grid = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    row = input()
    grid.append(list(row))
    if "B" in row:
        start = [i,row.index("B")]

# Find possible squares for a knight at each position.
neighbours = defaultdict(list)
for i in range(h):
    for j in range(w):
        for y,x in [[-2,1],[-2,-1],[-1,2],[-1,-2],[1,2],[1,-2],[2,1],[2,-1]]:
            ny, nx = i+y, j+x
            if 0<=ny<h and 0<=nx<w and grid[ny][nx] != "#":
                neighbours[(i,j)].append([ny,nx])

# Find the minimum moves to reach the end point.
cache = {}
min_moves = [999]
seen = set((start[0],start[1]))
def dfs(i , j , visited):
    
    if grid[i][j] == "E":
        min_moves[0] = min(min_moves[0], visited.bit_count())
        return True

    if (i,j) in cache and cache[(i,j)] <= visited.bit_count():
        return 

    for y,x in neighbours[(i,j)]:
        if (y,x) not in seen:
            seen.add((y,x))
            if dfs(y,x, visited | (1<<(y*w+x))):
                seen.remove((y,x))
                break
            else:
                seen.remove((y,x))

    cache[(i,j)] = visited.bit_count()
dfs(*start, 0)

# Print minimum moves otherwise, impossible.
if min_moves == [999]:
    print("Impossible")
else:
    print(*min_moves)
