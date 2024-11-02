# Get inputs.
a = gets.to_i
b = gets.to_i
m = gets.to_i

# Get starting position, starting direction and hashmap of available moves.
pos = [0,0]
d = 0
direction = {0=>[-1,0], 1=>[1,0], 2=>[0,-1],3=>[0,1]}
moves = 0

# Loop until position returns to [0,0]
while true
    # Increment moves and change direction.
    moves += 1
    d = ((a*d+b)%m)

    # Move position.
    pos[0] += direction[d%4][0]
    pos[1] += direction[d%4][1]
    
    # Check if returned to start position.
    if pos == [0,0]
        break
    end
end

# Output number of moves to return to start.
puts moves
