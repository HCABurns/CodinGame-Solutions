# Form grid, find Brodo and Mount Boom.
w, h = [int(i) for i in input().split()]
grid = [[] for _ in range(h)]
brodo = boom = ()
#boom = ()
for i in range(h):
    row = input()
    for j,char in enumerate(row):
        grid[i].append(char)
        if char == "B":
            brodo = (i,j)
            grid[i][j] = 0
        elif char == "M":
            boom = (i,j)

# Define the required variables.
to_visit = [brodo]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (1,1),(-1,-1),(1,-1),(-1,1)]
visited = set()

# Check that the diagonal move is not going through connected mountains.
routes = {(1,1):[(1,0),(0,1)],
(-1,-1):[(-1,0),(0,-1)],
(-1,1):[(-1,0),(0,1)],
(1,-1):[(1,0),(0,-1)]}

# Perfrom BFS, with early exit, to find distance from Frodo to Mount Boom.
while to_visit:
    current = to_visit.pop(0)
    visited.add(current)
    if current == boom:
        break
    
    for iy, jx in directions:
        # Check if the diagonal path is valid or blocked by mountains.
        if ((iy,jx) in routes):
            ti, tj = routes[(iy,jx)]
            if "^" == grid[ti[0]+current[0]][ti[1]+current[1]] == grid[tj[0]+current[0]][tj[1]+current[1]]:
                print("Yes: ", current , "direction",iy, jx)
                print(grid[ti[0]+current[0]][ti[1]+current[1]], grid[tj[0]+current[0]][tj[1]+current[1]])
                continue

        iy = current[0] + iy
        jx = current[1] + jx
        if 0 <= iy < h and 0 <= jx < w and (iy,jx) not in visited and grid[iy][jx] != "^":
            grid[iy][jx] = grid[current[0]][current[1]] + 1
            visited.add((iy,jx))
            to_visit.append((iy,jx))

# Output the distance from Brodo to Mount Boom.
print(f"{grid[boom[0]][boom[1]]} leagues")
