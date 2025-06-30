from collections import defaultdict

# Form grid and hashmap of pairing numbers.
h, w = [int(i) for i in input().split()]
grid = []
numbers = defaultdict(list)
for i in range(h):
    row = input()
    grid += [[]]
    for j, char in enumerate(row):
        grid[-1] += char
        if char != ".":
            numbers[char] += (i,j)

# Define directions and empty hashmap for list of paths from number to number.
directions = [(1,0),(0,1),(-1,0),(0,-1)]
paths = defaultdict(list)
def get_paths(y1,x1,y2,x2, number):
    def dfs(y,x, path, visited):
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            if ny == y2 and nx == x2:
                paths[number] += [path+[(y2,x2)]]
            elif 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == "." and (ny,nx) not in visited:
                dfs(ny, nx, path + [(ny, nx)], visited|{(ny,nx)})
    dfs(y1,x1, [(y1,x1)], set())

# Get all paths from node to node for each number.
for number in numbers.keys():
    get_paths(*numbers[number], number)

# Sort based on length (May or may not help)
for key in paths.keys():
    paths[key] = sorted(paths[key], key = len)

# Get all valid combinations of connected grids with their respective path ids.
combinations = []
def get_combinations(keys, current_path, index, path_index):
    if index == len(keys):
        combinations.append([current_path, path_index])
        return
    for j, path in enumerate(paths[keys[index]]):
        new_path = current_path | set(path)
        if len(new_path) == len(current_path) + len(path):
            get_combinations(keys, new_path, index+1, path_index+[j])
get_combinations(list(paths.keys()), set(), 0, [])
combinations.sort(key = lambda c : len(c[0]))

# Change the . to be the number in a path.
for i,key in enumerate(paths.keys()):
    for y,x in paths[key][combinations[0][1][i]]:
        grid[y][x] = key

# Print the altered grid.
for row in grid:
    print("".join(row))
