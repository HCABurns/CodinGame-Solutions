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

# Recursive DFS function with memoization.
cache = {}
def search(i, j, score, remaining_energy, visited):
    # Check if the current cell has a fruit and hasn't been visited.
    if (i, j) in fruit_positions:
        fruit_idx = fruit_positions[(i, j)]
        if not (visited & (1 << fruit_idx)):  
            score += fruits[grid[i][j]]  
            visited |= (1 << fruit_idx)

    # Check if this state has already been computed.
    state = (i, j, score, remaining_energy, visited)
    if state in cache:
        return cache[state]

    # Set max score to the current score gained from path.
    max_score = score

    # Explore neighbors in cardinal directions.
    for y, x in directions:
        iy, jx = i+y, j+x
        iy_wrapped , jx_wrapped = iy%h, jx%w
        # Recursively search and update max score if valid move.
        if (h==iy or iy < 0 or w==jx or jx < 0) and grid[iy_wrapped][jx_wrapped] != "#" and remaining_energy > 2:
            max_score = max(max_score, search(iy_wrapped, jx_wrapped, score, remaining_energy-3, visited))
        elif 0 <= iy < h and 0 <= jx < w and grid[iy][jx] != "#" and remaining_energy > 0:
            max_score = max(max_score, search(iy, jx, score, remaining_energy-1, visited))

    # Cache and return.
    cache[state] = max_score
    return max_score

# Print max score result from DFS using the initial position, energy and no visited fruits.
print(search(pos[0], pos[1], 0, energy, 0))
