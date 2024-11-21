# Form Grid and get starting position.
w, h = gets.split.map { |x| x.to_i }
x, y = gets.split.map { |x| x.to_i }
grid = h.times.map{gets.chomp}

# Set required directions variables.
get_direction_index = "^>v<"
directions = {0=>[-1,0] , 1=>[0,1],2=>[1,0],3=>[0,-1]}
direction = get_direction_index.index(grid[y][x])

# Set starting position and moves counter. variables.
starting = [x,y]
moves = 0

# Continue until reaches the start or out of the grid.
while (starting != [x,y] || moves == 0) && 0<=x && x<w and 0<=y && y<h do

  # Get current direction of square on.
  direction = get_direction_index.index(grid[y][x])

  # Increment direction (Turn Left)
  direction = (direction + 1) % 4

  # Set new direction.
  grid[y][x] = get_direction_index[direction]

  # Move to next square.
  x += directions[direction][1]
  y += directions[direction][0]

  # Increment moves counter.
  moves += 1
end
  
# Output number of moves to return to starting position.
puts moves
