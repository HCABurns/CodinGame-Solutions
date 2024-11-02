# Get inputs.
h = int(input())
w = int(input())

# Form Grid.
grid = [list(input().split()) for _ in range(h)] 

# Function to check if there's a path from (i, j) to the rightmost column
def can_reach_end(i, j, visited):
    # If reached the rightmost column, return True
    if j == w - 1:
        return True
    
    # Mark the cell as visited
    visited.add((i, j))

    # Explore the four possible directions (down, right, up, left)
    for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        iy, jx = i + y, j + x

        # Check bounds and if the cell is traversable and not visited
        if 0 <= iy < h and 0 <= jx < w and grid[iy][jx] == '+' and (iy, jx) not in visited:
            if can_reach_end(iy, jx, visited):
                return True

    return False

# Count the number of cells in the left column that can reach the rightmost column
count_reachable = 0
for i in range(h):
    if grid[i][0] == '+':
        if can_reach_end(i, 0, set()):
            count_reachable += 1

# Output the count.
print(count_reachable)
