STDOUT.sync = true # DO NOT REMOVE

# game loop
loop do
  # Required variables
  maxVal = 0
  maxIndex = 0

  # Find the index of the max height and store in max_index.
  8.times do |index|
    mountain_h = gets.to_i # represents the height of one mountain.
    if mountain_h>maxVal then
      maxVal = mountain_h
      maxIndex = index
    end
  end
  # Output the index of the mountain to fire on.
  puts maxIndex
end
