# Form grid, get starting location and direction.
width, height = [int(i) for i in input().split()]
grid = []
start_square = [-1,-1]
chars = {"<":0,"^":1,">":2,"v":3,"#":0}
direction = 0
for i in range(height):
    grid.append([])
    for j,char in enumerate(input()):
        grid[-1].append(0 if char not in chars else char)
        if char in chars and char != "#":
            start_square = [i,j]
            direction = chars[char]
            grid[i][j] = 0

# Get which wall to follow and convert to value to be used.
# Value of side determines turn direction.
# 1 means left turn, -1 means right turn.
side = 1 if input() == "L" else -1

#Set directions-L        U        R       D
directions = {0:[0,-1],1:[-1,0],2:[0,1],3:[1,0]}

# Required variables: previous square, i ,j.
# Previous square used to check when Pika reaches the start again.
# I, J are the y,x coordinates of Pika.
previous_square = [-1,-1]
i = start_square[0]
j = start_square[1]
chars = {0:"<",1:"^",2:">",3:"v"}
while previous_square != start_square:

    # Check for next valid move and turn until loop completed or valid move available.
    start_direction = direction
    loop = 0
    while loop<4:
        y , x = directions[direction]
        iy = i+y
        jx = j+x
        
        # Wrapping of Möbius strip. Left to right is a simple modulus wrap.
        # Wrapping vertically is more complex. If it wraps over the top, then it will
        # appear at the bottom equidistant from the centre, but the other side.
        wrap = False
        if iy < 0:
            iy = height-1
            wrap = True
        elif iy>=len(grid):
            iy = 0
            wrap=True
        
        if wrap:
            if width % 2 == 1:
                middle = width/2
                jx = abs(middle-jx)
                if jx < middle:
                    jx = width - jx
            else:
                middles = [width//2-1,width//2]
                if jx <= middles[0]:
                    jx = width - abs(middles[1]-jx)
                else:
                    jx = middles[0] - (width-1-jx)
        jx = jx%width
        if grid[iy][jx] == "#":
            direction = (direction+side)%4
        else:
            break  
        loop+=1
    # If Pika coun't find a move in any direction, he is blocked, therefore end.
    if loop==4:break

    # Move in the current direction. Alter direction to be the previous direction.
    # This will ensure that Pika 'hugs' the wall.
    i = iy
    j = (jx)%width
    grid[i][j] += 1 
    previous_square = [i,j]
    direction = (direction+(side*-1))%4

# Output the new grid which number of times each square was visited.
for row in grid:
    print("".join([str(i) for i in row]))
