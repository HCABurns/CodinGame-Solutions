# Get inputs.
order = input()
side = input()

# Hashmaps for storing: current number of sheets visible, opposite direction and adjacent sides. 
sheets = {"L":1,"U":1,"R":1,"D":1}
opposite = {"L":"R","R":"L","U":"D","D":"U"}
adjacent = {"L":"DU","R":"DU","D":"RL","U":"RL"}

# Complete the folds.
for move in order:
    # Add current sheets to the opposite side.
    sheets[opposite[move]] += sheets[move]

    # Double the values on the adjacent sides.
    for direction in adjacent[move]:
        sheets[direction] = sheets[direction] * 2
    
    # Set current move to new value.
    sheets[move] = 1

# Output the number of sheets visible from given side.
print(sheets[side])
