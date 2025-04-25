# Get the input, form the grid and store the location of snake heads.
n, m = [int(i) for i in input().split()]
grid = []
heads = []
for i in range(n):
    t = input()
    row = []
    for j,char in enumerate(t):
        if char == "o":
            heads.append([i,j])
        row.append(char)
    grid.append(row)


# Define the required variables.
largest = [0,0]
directions = [[1,0],[-1,0],[0,-1],[0,1]]
tails = {"<",">","^","v"}
body = {"|","-"}
direction = 0

# Find the length of the snake.
for i,j in heads:
    size = 2
    while grid[i][j] not in tails:
        if grid[i][j] == "*":
            size +=1

        # Determine direction of snake.
        if i-1 >=0 and grid[i-1][j] == "|":
            direction = 1
            i-=1
        elif i+1 < len(grid) and grid[i+1][j] == "|":
            direction = 0
            i+=1
        elif j-1 >=0 and grid[i][j-1] == "-":
            direction = 2
            j-=1
        else:
            direction = 3
            j+=1

        # Move until a blocker.
        while grid[i][j] in body:
            grid[i][j] = "."
            i += directions[direction][0]
            j += directions[direction][1]
            size += 1
        
    # Update the largest snake size and quanity.
    if size > largest[0]:
        largest = [size, 1]
    elif size == largest[0]:
        largest[1] += 1


# Print the largest size and number of snakes with that size.
print(*largest,sep = "\n")
