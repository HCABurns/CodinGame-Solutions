# Form Grid
grid = []
n = int(input())
for i in range(n):
    grid.append([int(j) for j in input().split()])

# Declare required variables.
# To visit nodes in form - (Row, Column, Previous Height)
middle = (n//2 ,n//2, grid[n//2][n//2]+1)
visited = set()
to_visit = [middle]
valid = False

while to_visit:
    # Get next node and upack.
    node = to_visit.pop()
    i , j, height = node

    # Ensure node has not been visited and not out of grid.
    if node in visited or i < 0 or i > n or j<0 or j>n:
        continue
    # Add node to the visited set.
    visited.add(node)

    # Ensure that the distance from current node to previous is either 1 or 0.
    if abs(height - grid[i][j]) <= 1:
        # If current position is 0 (water), set valid flag and exit loop.
        if grid[i][j] == 0:
            valid = True
            break
        # Add adjacent nodes to the list to be visited.
        to_visit.append((i-1, j , grid[i][j]))
        to_visit.append((i+1, j , grid[i][j]))
        to_visit.append((i, j-1 , grid[i][j]))
        to_visit.append((i, j+1 , grid[i][j]))

# Print yes if possible to exit island otherwise no.
print("yes" if valid else "no")
