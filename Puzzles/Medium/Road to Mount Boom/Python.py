# Form grid, find Brodo and Mount Boom.
h, w = [int(i) for i in input().split()]
w, h = w+2, h+2
grid = [[] for _ in range(h)]
grid[0] = [" " for _ in range(w)]
brodo = boom = (0,0)
for i in range(1,h-1):
    row = " " + input() + " "
    assert len(row) == w, f"Row {i} is size {len(row)} instead of {w}"
    for j,char in enumerate(row):
        grid[i].append(char)
        if char == "B":
            brodo = (i,j)
            grid[i][j] = 0
        elif char == "M":
            boom = (i,j)
grid[-1] = [" " for _ in range(w)]
assert len(grid) == h, f"Grid is size {len(grid)} instead of {h}"

# Define the required variables to perfrom BFS.
to_visit = [brodo]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (1,1),(-1,-1),(1,-1),(-1,1)]
visited = set()

# Store relative positions to check if a diagonal move is not going through connected mountains.
routes = {(1,1):[(1,0),(0,1)],
(-1,-1):[(-1,0),(0,-1)],
(-1,1):[(-1,0),(0,1)],
(1,-1):[(1,0),(0,-1)]}

# Perfrom BFS, with early exit, to find distance from Frodo to Mount Boom.
while to_visit:
    current = to_visit.pop(0)
    i, j = current
    visited.add(current)
    # Early Exit Clause
    if current == boom:
        break
    
    for iy, jx in directions:
        # Check if the diagonal path is valid or blocked by connected mountains.
        if (iy,jx) in routes:
            diag1, diag2 = routes[(iy,jx)]
            di1 , dj1 = diag1[0]+i , diag1[1]+j
            di2 , dj2 = diag2[0]+i , diag2[1]+j
            if all(0 <= x < h and 0 <= y < w for x, y in [(di1, dj1), (di2, dj2)]):
                if "^" == grid[diag1[0]+i][diag1[1]+j] == grid[diag2[0]+i][diag2[1]+j]:
                    continue

        # If move has not been visited, is valid and not a mountain, add to to_visit array.
        iy = i + iy
        jx = j + jx
        if 0 <= iy < h and 0 <= jx < w and (iy,jx) not in visited and grid[iy][jx] != "^":
            grid[iy][jx] = grid[i][j] + 1
            visited.add((iy,jx))
            to_visit.append((iy,jx))

# Print the length from Brodo's starting position and Mount Boom.
distance = grid[boom[0]][boom[1]]
print(f"{distance} league{['','s'][distance != 1]}")
