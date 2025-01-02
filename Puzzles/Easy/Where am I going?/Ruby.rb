# Form Grid.
h = gets.to_i
w = gets.to_i
grid = h.times.map{gets.chomp}

# Define starting position.
i = 0
j = -1

# Define directions array and variable.
directions = [[1,0],[0,1],[-1,0],[0,-1]]#RDLU
direction = 0

# Find path through grid.
path = ""
while 1 do
  jx , iy = directions[direction]
  
  # If next move is invalid, turn right / left, if that is invalid quit.
  if i + iy >= h || i + iy < 0 || j + jx >= w || j + jx < 0 || grid[i + iy][j + jx] == "."
    ri , rj = i + directions[(direction+1)%4][1], j + directions[(direction+1)%4][0]
    li , lj = i + directions[(direction-1)%4][1], j + directions[(direction-1)%4][0]
    # Check right.
    if ri < h && ri >=0 && w > rj && rj >= 0 && grid[ri][rj] == "#"
      direction = (direction + 1) % 4
      path += "R"
    # Check left.
    elsif li < h && li >=0 && w > lj && lj >= 0 && grid[li][lj] == "#"
      direction = (direction - 1) % 4
      path += "L"
    # End of path.
    else
      break
    end
  end

  # Move in current direction until can't move.
  jx , iy = directions[direction]
  moves = 0
  while i + iy < h && i + iy >=0 && w > j + jx && j + jx >= 0 && grid[i + iy][j + jx] == "#" do
    moves += 1
    i += iy
    j += jx
  end

  # Add number of moves to the path.
  path += moves.to_s
end

# Print path.
puts path



=begin
# Print direction of the path.
while True:
    jx , iy = directions[direction]
    # If next is invalid, turn right / left, if that is invalid quit.
    if i + iy >= h or i + iy < 0 or j + jx >= w or j + jx < 0 or grid[i + iy][j + jx] == ".":
        ri , rj = i + directions[(direction+1)%4][1], j + directions[(direction+1)%4][0]
        li , lj = i + directions[(direction-1)%4][1], j + directions[(direction-1)%4][0]
        if ri < h and ri >=0 and w > rj and rj >= 0 and grid[ri][rj] == "#":
            print(end = "R")
            direction = (direction + 1) % 4
        elif li < h and li >=0 and w > lj and lj >= 0 and grid[li][lj] == "#":
            print(end = "L")
            direction = (direction - 1) % 4
        else:
            break

=end
