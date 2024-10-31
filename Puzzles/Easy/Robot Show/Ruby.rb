# Get inputs
l = gets.to_i
n = gets.to_i

# Create array of bot positions.
arr = []
inputs = gets.split
for i in 0..(n-1){arr << inputs[i].to_i}

# Max time is for a furthest box from the end to reach the end.
puts [l-arr.min,arr.max].max
