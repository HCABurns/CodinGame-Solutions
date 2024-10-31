# Get inputs
l = gets.to_i
n = gets.to_i

# Create array of bot positions.
arr = []
inputs = gets.split(" ")
inputs.each{|i| arr << i.to_i}

# Max time is for a furthest box from the end to reach the end.
puts [l-arr.min,arr.max].max
