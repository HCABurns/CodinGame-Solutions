#NOTE: Coordinates are in the form Y,X.
# Form grid, get starting position and get coordinated of barriers.
w, h = [int(i) for i in input().split()]
n = int(input())
grid = []
barriers = {}#Barrier pos: [Next barrier pos, distance between]
pos = []
for i in range(h):
    grid.append([])
    for j,char in enumerate(input()):
        grid[-1].append(char)
        if char == "#":
            barriers[(i,j)] = None
        elif char == "O":
            pos = [i,j]
            grid[i][j] = "."

# Set up directions.
directions = {0:[-1,0] , 1:[0,1], 2:[1,0],3:[0,-1]}
direction = 0

prev = None
# Mapping the barriers together.
while True:
    # If next move is a barrier, map the barrier until a loop is found.
    if (pos[0]+directions[direction][0],pos[1]+directions[direction][1]) in barriers:
        barrier_y = pos[0]+directions[direction][0]
        barrier_x = pos[1]+directions[direction][1]
        if prev == None:
            prev = (barrier_y , barrier_x)
        else:
            barriers[prev] = ((barrier_y , barrier_x),abs(barrier_y-prev[0])+abs(barrier_x-prev[1])-2)
            prev = (barrier_y , barrier_x)
            if barriers[prev] != None:
                break
    # Move to next position.
    while (pos[0]+directions[direction][0],pos[1]+directions[direction][1]) in barriers:
        direction = (direction + 1) % 4
    pos[0] += directions[direction][0]
    pos[1] += directions[direction][1]
    n-=1
    
# Calculate length of loop.
loop_length = 0
start = prev
while True:
    prev, distance = barriers[prev]
    loop_length += distance
    if prev==start:break

# Simulate the loops (Remainder of n / loop size).
n %= loop_length

# Move the remaining spaces.
while n>0:
    while (pos[0]+directions[direction][0],pos[1]+directions[direction][1]) in barriers:
        direction = (direction + 1) % 4
    pos[0] += directions[direction][0]
    pos[1] += directions[direction][1]
    n-=1

# Output the final position of the robot.
print(pos[1] , pos[0])
