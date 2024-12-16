# Form Grid.
w = int(input())
h = int(input())
grid = []
for i in range(h):
    grid.append(list(map(int,input().split())))

# Set directions to check and set coordinates.
directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
coords = "0 0"

# Find treasure.
for i in range(h):
    for j in range(w):
        # Storing the sum of obstacles.
        sum_val = 0

        # If current is an obstacle, move onto next.
        if grid[i][j] != 0:
            continue

        # Find amount of obstacles around current position.
        for x,y in directions:
            if i+y>=0 and i+y<h and x+j >= 0 and x+j < w:
                sum_val += grid[i+y][j+x]
        
        # Determine is current position is the treasure.
        if sum_val == 3 and ((i == 0 and j == 0 or j == w-1) or (i == h-1 and j == 0 or j == w-1)):
                coords = f"{j} {i}"
        elif sum_val == 5 and ((i == 0 or i == h-1) or (j == 0 or j == w-1)):
            coords = f"{j} {i}"
        elif sum_val == 8:
            coords = f"{j} {i}"

        # If treasure has been found, exit and print.
        if coords != "0 0":
            break

# Print location of treasure otherwise 0 0.
print(coords)
