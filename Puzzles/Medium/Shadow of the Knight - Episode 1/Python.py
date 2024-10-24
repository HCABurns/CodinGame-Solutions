# Get required inputs.
w, h = [int(i) for i in input().split()]
n = input()
x, y = [int(i) for i in input().split()]

# Set variables for binary search.
x_left = 0
x_right = w-1
y_top = 0
y_bottom = h-1

# Complete binary search until bomb is found (Game engine decides when to stop not code)
while 1:
    # Get bomb direction
    bomb_dir = input()

    # Move binary search limits based on the input.
    # (4 linear searches are fine here as bomb_dir has max len of 2)
    if "U" in bomb_dir:
        y_bottom = y-1
    
    if "D" in bomb_dir:
        y_top = y+1
    
    if "L" in bomb_dir:
        x_right = x-1
    
    if "R" in bomb_dir:
        x_left = x+1
    
    # Change valeus of x and y (Binary search)
    x = (x_left + x_right) //2
    y = (y_top + y_bottom) //2
    
    # Output the new coordinates.
    print(x , y)
