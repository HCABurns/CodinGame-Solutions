# Get grid dimensions and starting position.
w, h = [int(i) for i in input().split()]
start_row, start_col = [int(i) for i in input().split()]

# Set directions hashmap and set minimum path size and idx.
directions = {">":(0,1),"<":(0,-1),"^":(-1,0),"v":(1,0)}
min_path = w*h+1
min_path_idx = None

# Check all grids for valid path and select idx of shortest.
n = int(input())
for idx in range(n):
    # Form grid.
    grid = []
    visited = set()
    for j in range(h):
        grid.append(input())
    
    # Traverse grid and find path length - If loops then quit loop.
    i , j = start_row, start_col
    path = 0
    while grid[i][j] in directions and (i,j) not in visited:
        visited.add((i,j))
        iy , jx = directions[grid[i][j]]
        # Ensure a valid move is next.
        if i+iy<0 or i+iy>=len(grid) or j+jx<0 or j+jx>=len(grid[0]):
            break
        i += iy
        j += jx
        path += 1
    
    # Change minimum if required.
    if grid[i][j] == "T":
        min_path = min(min_path , path)
    if min_path == path:
        min_path_idx = idx

# Output the id of the map with the shortest path or TRAP if no route.
if min_path_idx != None:
    print(min_path_idx)
else:
    print("TRAP")
