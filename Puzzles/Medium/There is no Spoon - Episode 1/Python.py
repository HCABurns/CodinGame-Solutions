#NOTE: All coordinates are in the form [y,x] or [row, column]
# Get size of grid and form 2D grid.
width = int(input())
height = int(input())
grid = [[i for i in input()] for _ in range(height)]

# Check each node for a node to its right or below. If found then print coordinate else -1 -1.
for row in range(height):#Row
    for column in range(width):#Column
        # Ensure power node has been found.
        node = grid[row][column]
        if node == ".":
            continue
        
        # Set variables below and right of current power node
        ti = row+1
        tj = column+1

        #Increment until out of grid or found a power node
        while ti<height and grid[ti][column]!="0":
            ti+=1
        while tj<width and grid[row][tj]!="0":
            tj+=1
        
        #Print neighbor nodes (right and down) - If node not found then print -1 -1.
        print(f"{column} {row} {tj if tj<width else -1} {row if tj<width else -1} {column if ti<height else -1} {ti if ti<height else -1}")
