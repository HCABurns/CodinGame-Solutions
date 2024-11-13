# Get dimensions, form grid, get starting location and teleport locations.
l, c = [int(i) for i in input().split()]
grid = [list(input()) for i in range(l)]
i = 0
j = 0
teleporters = []
for ix, row in enumerate(grid):
    for jx, col in enumerate(row):
        if col == "@":
            i,j = ix, jx
        if col == "T":
            teleporters.append((ix,jx))

# Declare required variables.
directions_changer = {"N":2,"S":0,"E":1,"W":3}
directions = [(1,0),(0,1),(-1,0),(0,-1)]
paths = {0:"SOUTH",1:"EAST",2:"NORTH",3:"WEST"}
if len(teleporters)>0:
    teleporters = {teleporters[0]:teleporters[1], teleporters[1]:teleporters[0]}
direction = 0
inverter = 0
breaker = 0
broken = 0
visited = []
found = False

# Iterative approach
while (i ,j, direction, inverter, breaker, broken) not in visited:
    # Add to visisted list.
    visited.append((i, j, direction, inverter, breaker, broken))

    # Goal Case - Suicide booth found.
    if grid[i][j] == "$":
        found = True
        break
    
    # Step #5 - Force direction if encounters NSEW.
    if grid[i][j] in ["N","S","E","W"]:
        direction = directions_changer[grid[i][j]]

    # Step 6 - Set invert flag if encounters I. 
    if grid[i][j] == "I":
        inverter ^= 1
    
    # Step 7 - Set breaker flag if encounters B.
    if grid[i][j] == "B":
        breaker ^= 1
    
    # Step 8 - Teleport to other teleported if encounters T.
    if grid[i][j] == "T":
        i , j = teleporters[(i,j)]

    # Set new direction. (Only used if current direction can#t be moved into)
    new_dir = -1 if not inverter else 4
    for _ in range(4):
        # Move in current direction.
        iy = i+directions[direction][0]
        jx = j+directions[direction][1]

        # If move if possible then move, otherwise change direction based on priority and try again.
        if 0<=iy<len(grid) and 0<=jx<len(grid[0]) and grid[iy][jx] != "X" and grid[iy][jx] != "#" or \
         (grid[iy][jx] == "X" and breaker and iy!=0 and iy!=len(grid)-1 and jx!=0 and jx!=len(grid[0])-1):
            # 'break' barrier if possible.
            if grid[iy][jx] == "X" and breaker:
                grid[iy][jx] = " "
                broken += 1
            # Recursively search until path loops or $ is found.
            i = iy
            j = jx
            break        
        else:
            # Change direction based on current priority.
            new_dir += 1 if not inverter else -1
            direction = (new_dir)%4

# Print path if existing, otherwise loop.
if found:
    for _,_,d,*_ in visited[1:]:
        print(paths[d])
else:
    print("LOOP")
