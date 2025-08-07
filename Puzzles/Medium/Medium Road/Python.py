# Define grid and max length with which player it's for.
grid = []
max_char = ""
max_path = 4

# Form grid.
n = int(input())
for i in range(n):
    line = input()
    grid.append(line)

# DFS to find the max path length.
def dfs(y,x, char, path, visited):
    global max_path
    global max_char
    if len(path) > max_path:
        max_path = len(path)
        max_char = char

    visited.add((y,x))

    directions = [[0,1],[-1,0],[0,-1],[1,0]]
    for dy, dx in directions:
        ny , nx = y+dy, x+dx

        if 0 <= ny < n and 0 <= nx < n and (ny,nx) not in visited:
            if grid[ny][nx] == char:
                dfs(ny,nx, char, path+[[ny,nx]], visited)
            elif grid[ny][nx] == char.upper():
                dfs(ny,nx, char, path, visited)
    visited.remove((y,x))

# Check each position for max road length.
for i in range(n):
    for j in range(n):     
        if grid[i][j].isalpha():
            if grid[i][j].islower():
                dfs(i,j, grid[i][j].lower(), [[i,j]], set())
            else:
                dfs(i,j, grid[i][j].lower(), [], set())

# Print the max path otherwise 0 if less than 5.
if max_char:
    print(max_char.upper(),max_path)
else:
    print(0)
