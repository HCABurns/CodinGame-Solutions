import random

# Constants
GRID_SIZE = 28
ENERGY_LIMIT = 12
ENERGY_MAX = 14
GHOST_LIMIT = 5
GHOST_MAX = 20
BARRIERS = 0

# Symbols for the grid
PACMAN = 'P'
GHOST = 'G'
FRUIT_5 = '*'  
FRUIT_1 = '.'  
FRUIT_3 = ')'  
EMPTY = ' '
BARRIER = '#'

# Create an empty grid
grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

if BARRIERS:
    grid[0] = ["#" for j in range(GRID_SIZE)]
    grid[-1] = ["#" for j in range(GRID_SIZE)]
    for i in range(len(grid)):
        grid[i][0] = "#"
        grid[i][-1] = "#"
 
# Randomly place Pac-Man
pacman_x = random.randint(0, GRID_SIZE - 1)
pacman_y = random.randint(0, GRID_SIZE - 1)
grid[pacman_x][pacman_y] = PACMAN
#grid[GRID_SIZE - 1][0] = PACMAN

# Randomly place ghosts, ensuring they do not overlap with Pac-Man
num_ghosts = random.randint(GHOST_LIMIT, GHOST_MAX)  # Random number of ghosts
for _ in range(num_ghosts):
    while True:
        ghost_x = random.randint(0, GRID_SIZE - 1)
        ghost_y = random.randint(0, GRID_SIZE - 1)
        if grid[ghost_x][ghost_y] != PACMAN:
            grid[ghost_x][ghost_y] = GHOST
            break

# Randomly fill the rest of the grid with fruits
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if grid[i][j] == EMPTY:  # Only fill empty spaces
            fruit_type = random.choices(
                [FRUIT_5, FRUIT_1, FRUIT_3 , EMPTY, BARRIER],
                weights=[0.3, 0.4, 0.3,0.0,0.0],k=1)[0]
            grid[i][j] = fruit_type


# Print height and width of grid and energy.
print(len(grid) , len(grid[0]))
energy = random.randint(ENERGY_LIMIT, ENERGY_MAX)
print(energy)

# Print the grid - With Barriers

#print("#"*len(grid))
#for row in grid[1:-1]:
#    print("#"+''.join(row[1:-1])+"#")
#print("#"*len(grid))


# Print the grid without barriers
for row in grid:
    print("".join(row))


# Print answer

# Read dimensions and initial energy. Also set required variables.
w, h = GRID_SIZE , GRID_SIZE
energy = energy
fruits = {"*": 5, ")": 3, ".": 1}
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pos = (-1, -1)
#grid = []
fruit_positions = {}
ghosts = []

# Form grid and locate all fruit cells and the starting position.
fruit_index = 0
for i in range(h):
    #grid.append([i for i in input()])
    for j, char in enumerate(grid[i]):
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
maximum_score = search(pos[0], pos[1], 0, energy, 0)
print(maximum_score)

# Get visited of max
for key,score in cache.items():
    if key[2] == maximum_score:
        visited = key[-1]


        # Print ALL Paths.
        print("\nUpdated Path:")
        for i,j in fruit_positions:
            fruit_idx = fruit_positions[(i, j)]
            if (visited & (1 << fruit_idx)):
                grid[i][j] = "?"
        for row in grid:
            print("".join(row))

