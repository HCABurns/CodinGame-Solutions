# Get inputs.
a = int(input())
b = int(input())
m = int(input())

# Get starting position, starting direction and hashmap of available moves.
pos = [0,0]
D = 0
direction = {0:[-1,0], 1:[1,0], 2:[0,-1],3:[0,1]}
moves = 0

# Loop until position returns to [0,0]
while True:
    # Increment moves and change direction.
    moves += 1
    D = ((a*D+b)%m)

    # Move position.
    pos[0] += direction[D%4][0]
    pos[1] += direction[D%4][1]
    
    # Check if returned to start position.
    if pos == [0,0]:
        break

# Output number of moves to return to start.
print(moves)
