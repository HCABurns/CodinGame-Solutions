# Get custom order.
d = gets.to_i
n = gets.to_i
custom_order = gets.split.map{|i| i.to_i - 1}

# Array for storing coordinates.
coordinates = []

# Get coordinates in custom order.
n.times do |i|
  # Get coordinates in original position.
  vals = gets.split.map(&:to_i)

  # Change order based on custom order.
  perm = custom_order.map{|j| vals[j]}
  
  # Add new coordinates to array.
  coordinates << [perm, i]
end

# Print indexes of topology space sorted in custom order.
puts coordinates.sort.map{|i| (i[1]+1).to_s}.join " "
