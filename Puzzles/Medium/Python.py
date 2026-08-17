from collections import deque

# Get inputs grid.
grid = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    grid.append(list(input()))

# Search the grid for holes.
total_holes = 0
for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char != ".":
            continue
        
        # Found empty, perform BFS: If edge is found, invalid hole, otherwise valid.
        queue = deque([(i,j)])
        hole = True
        while queue:
            y, x = queue.popleft()

            # Check if current cell touches boundary
            if y == 0 or y == h - 1 or x == 0 or x == w - 1:
                hole = False

            for dy, dx in [[0,1],[-1,0],[0,-1],[1,0]]:
                ny, nx = y + dy, x + dx

                # Boundary check before accessing grid array
                if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == ".":
                    grid[ny][nx] = "#"
                    queue.append((ny, nx))

        if hole:
            total_holes += 1

# Print total
print(total_holes)
