# Form Grid.
h = int(input())
w = int(input())
grid = [input() for i in range(h)]

# Define starting position.
i = 0
j = -1

# Define directions array and variable.
directions = [(1,0),(0,1),(-1,0),(0,-1)]#RDLU
direction = 0

# Print direction of the path.
while True:
    jx , iy = directions[direction]
    # If next is invalid, turn right / left, if that is invalid quit.
    if i + iy >= h or i + iy < 0 or j + jx >= w or j + jx < 0 or grid[i + iy][j + jx] == ".":
        ri , rj = i + directions[(direction+1)%4][1], j + directions[(direction+1)%4][0]
        li , lj = i + directions[(direction-1)%4][1], j + directions[(direction-1)%4][0]
        if ri < h and ri >=0 and w > rj and rj >= 0 and grid[ri][rj] == "#":
            print(end = "R")
            direction = (direction + 1) % 4
        elif li < h and li >=0 and w > lj and lj >= 0 and grid[li][lj] == "#":
            print(end = "L")
            direction = (direction - 1) % 4
        else:
            break

    # Move in current direction until can't move.
    jx , iy = directions[direction]
    moves = 0
    while i + iy < h and i + iy >=0 and w > j + jx and j + jx >= 0 and grid[i + iy][j + jx] == "#":
        moves += 1
        i += iy
        j += jx

    # Print number of moves.
    print(end = f"{moves}")
