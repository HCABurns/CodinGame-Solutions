# Form Grid and get starting position.
w, h = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]
grid = [list(input()) for i in range(h)]

# Set required directions variables.
get_direction_index = "^>v<"
directions = {0:[-1,0] , 1:[0,1],2:[1,0],3:[0,-1]}
direction = get_direction_index.index(grid[y][x])

# Set starting position and moves counter. variables.
starting = (x,y)
moves = 0

# Continue until reaches the start or out of the grid.
while (starting != (x,y) or moves == 0) and 0<=x<len(grid[0]) and 0<=y<len(grid):

    # Get current direction of square on.
    direction = get_direction_index.index(grid[y][x])

    # Increment direction (Turn Left)
    direction = (direction + 1) % 4

    # Set new direction.
    grid[y][x] = get_direction_index[direction]

    # Move to next square.
    x += directions[direction][1]
    y += directions[direction][0]

    # Increment moves counter.
    moves += 1
    
# Output number of moves to return to starting position.
print(moves)
