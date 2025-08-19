# Read dimensions and energy. Also set required variables.
w, h = [int(i) for i in input().split()]
energy = int(input())
fruits = {"*": 5, ")": 3, ".": 1}
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
grid = []
pos = (-1, -1)
fruit_positions = {}
ghosts = []

# Form grid and locate all fruit cells and the starting position.
fruit_index = 0
for i in range(h):
    grid.append([i for i in input()])
    for j, char in enumerate(grid[-1]):
        if char == "P":
            pos = (i, j)
        elif char == "G":
            ghosts.append((i,j))
        elif char in fruits:
            fruit_positions[(i, j)] = fruit_index 
            fruit_index += 1

# Set barrier around each ghosts reach. (Avoids having to check in recursive function)
for i,j in ghosts:
    grid[i][j] = "#"
    for y, x in directions:
        grid[(i+y)%h][(j+x)%w] = "#"

# Find available neighbours for cells.
neighbours = {}
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":continue
        for dy,dx in [[0,1],[-1,0],[0,-1],[1,0]]:
            ny, nx = i+dy, j+dx
            ny_wrapped, nx_wrapped = (ny%h) , (nx%w)
            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] != "#" or grid[ny_wrapped][nx_wrapped] != "#":
                neighbours.setdefault((i,j), [])
                if ny_wrapped != ny or nx_wrapped != nx:
                    neighbours[(i,j)].append([ny_wrapped,nx_wrapped,3])
                else:
                    neighbours[(i,j)].append([ny,nx,1])

# Recursive DFS function with cache to avoid recomputing.
cache = {}
max_score = [0]
def search(i, j, score, remaining_energy, visited):
    # Check if the current cell has a fruit and hasn't been visited.
    if (i, j) in fruit_positions:
        fruit_idx = fruit_positions[(i, j)]
        if not (visited & (1 << fruit_idx)):  
            score += fruits[grid[i][j]]  
            visited |= (1 << fruit_idx)
    
    if score > max_score[0]:
        max_score[0] = score
    if score + 5*remaining_energy <= max_score[0]:
        return score

    # Check if this state has already been seen.
    state = (i, j, score, remaining_energy, visited)
    if state in cache:
        return 

    # Explore neighbors in cardinal directions.
    for y, x, cost in neighbours.get((i,j),[]):
        if remaining_energy-cost >= 0:
            search(y, x, score, remaining_energy-cost, visited)

    # Cache and return.
    cache[state] = score
    return

# Print max score result from DFS using the initial position, energy and no visited fruits.
search(pos[0], pos[1], 0, energy, 0)
print(max_score[0])
