# Get grid dimentions and bounce limit.
w = int(input()) + 2
h = int(input()) + 2
bounces = int(input())

# Set starting position.
i = 1
j = 1

# Set directions.
direction = 0
directions = {0:[1,1] , 1:[-1,1], 2:[1,-1], 3:[-1,-1]}

# Set directions for letterbox grid - if required,
if h == 3:
    directions = {0:[0,1] , 1:[0,1], 2:[0,-1], 3:[0,-1]}
if w == 3:
    bounces-=1
    directions = {0:[1,0] , 1:[1,0], 2:[-1,0], 3:[-1,0]}

# Form grid.
grid = [["#" for i in " "*w]]
for _ in range(h-2):
    grid.append([j for j in "#" + " "*(w-2) + "#"])
grid+=[["#" for i in " "*w]]
grid[i][j] = "1"

# Continue until all bounces are completed.
while bounces > 0:
    # Get next move
    iy , jx = directions[direction]
    iy = iy + i
    jx = jx + j
    # If invalid, find a valid move.
    if iy==0 or iy == h-1 or jx == 0 or jx == w-1:
        while iy==0 or iy == h-1 or jx == 0 or jx == w-1:
            if iy == 0: 
                direction = 0 if direction == 1 else 2
            elif iy == h-1:
                direction = 1 if direction == 0 else 3
            elif jx == 0: 
                direction = 0 if direction == 2 else 1
            elif jx == w - 1:
                direction = 2 if direction == 0 else 3
            iy , jx = directions[direction]
            iy = iy + i
            jx = jx + j
        bounces -= 1
    else:
        # Add 1 to visited location.
        if h == 3 or w == 3:bounces-=1
        i = iy
        j = jx
        if grid[i][j] == " " :
            grid[i][j] = str(1) 
        else:
            grid[i][j] = str(int(grid[i][j])+1) 

# Print Grid.
for r in grid:
    print("".join(r))
