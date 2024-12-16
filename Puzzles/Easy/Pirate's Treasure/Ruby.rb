# Form Grid.
w = gets.to_i
h = gets.to_i
grid = []
h.times do
  inputs = gets.split
  grid << []
  for j in 0..(w-1)
    v = inputs[j].to_i
    grid[-1] << v
  end
end

# Set directions to check.
directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
coords = "0 0"

# Find treasure.
h.times do |i|
  w.times do |j|
    # Storing the sum of obstacles.
    sum_val = 0

    # If current is an obstacle, move onto next.
    next if grid[i][j] != 0

    # Find amount of obstacles around current position.
    directions.each do |x,y|
      sum_val += grid[i+y][j+x] if i+y>=0 && i+y<h && x+j >= 0 && x+j < w
    end
    
    # Determine is current position is the treasure.
    if sum_val == 3 && ((i == 0 && j == 0 || j == w-1) || (i == h-1 && j == 0 || j == w-1))
      coords = "#{j} #{i}"
    elsif sum_val == 5 && ((i == 0 || i == h-1) || (j == 0 || j == w-1))
      coords = "#{j} #{i}"
    elsif sum_val == 8
      coords = "#{j} #{i}"
    end

    # If treasure has been found, exit and print.
    break if coords != "0 0"
  end
end

# Print location of treasure otherwise 0 0.
puts coords
