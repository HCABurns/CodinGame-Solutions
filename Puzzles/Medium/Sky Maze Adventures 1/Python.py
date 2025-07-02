# Form grid and get the goal position.
w, h = [int(i) for i in input().split()]
dx, dy = [int(i) for i in input().split()]
grid = []
for i in range(h):
    c = input()
    grid += [c]
goal = [dy,dx]

# Perform DFS to find a valid route.
final_path = [[]]
swapper = {(1,0):"DOWN", (-1,0):"UP", (0,1):"RIGHT", (0,-1):"LEFT"}
def dfs(y,x,visited,path):
    if [y,x] == goal:
        final_path[0] = path
        return 1
    visited.add((y,x))
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    for dy,dx in directions:
        ny, nx = y+dy, x+dx
        if 0<= ny < h and 0<=nx<w and (ny,nx) not in visited and grid[ny][nx] == "0":
            res = dfs(ny,nx, visited, path + [swapper[(dy,dx)]])
            if res == 1: return 1
    return 0

while True:
    # Get starting location.
    x, y = [int(i) for i in input().split()]

    # Perform DFS to find route.
    dfs(y,x, set(), [])

    # Print the route.
    for direction in final_path[0]:
        print(direction)
    break
