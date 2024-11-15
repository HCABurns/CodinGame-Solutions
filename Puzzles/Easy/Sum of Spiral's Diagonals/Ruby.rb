# Get size of spiral.
n = gets.to_i

# Initialise require variables.
total = 1# Total count of diagonals (Start at 1 as 1 isn't included)
idx = 1 # Value currently on.
corner_counter = 0 # Counter for how many corners have been visited.
distance_between_corner = n-1 # Distance between corners.
counter = 0 # Number of items passed since last corner.

# Continue from 1-N counting only corners. (Corners are diagonals)
while idx < n*n+1 do
    if counter == distance_between_corner
        total+=idx
        corner_counter+=1
        if corner_counter == 4
            distance_between_corner -= 2
            corner_counter=0
        end
        counter = 0
    end
    # Increment idx and counter.
    idx+=1
    counter += 1
end
# Output sum
p total
