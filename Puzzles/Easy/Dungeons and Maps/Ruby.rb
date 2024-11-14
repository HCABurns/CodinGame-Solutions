# Get inputs: grid dimensions and starting position.
w, h = gets.split.map { |x| x.to_i }
start_row, start_col = gets.split.map { |x| x.to_i }

# Set directions hashamp and set minimum path size and idx.
directions = {">"=>[0,1],"<"=>[0,-1],"^"=>[-1,0],"v"=>[1,0]}
min_path = w*h+1
min_path_idx = -1

# Check all grids for valid path and select idx of shortest.
gets.to_i.times do |idx|
  # Form grid.
  grid = visited = []
  h.times do
    grid << gets.chomp
  end

  # Traverse grid and find path length - If loops then quit loop.
  i , j = start_row, start_col
  path = 0
  while directions[grid[i][j]] && !visited.include?([i,j])
    visited << [i,j]
    iy , jx = directions[grid[i][j]]
    # Ensure a valid move is next.
    if i+iy<0 || i+iy>=grid.size || j+jx<0 || j+jx>=grid[0].size
      break
    end
    i += iy
    j += jx
    path += 1
  end
  # Change minimum if required.
  min_path = [min_path, path].min if grid[i][j] == "T"
  min_path_idx = idx if min_path == path
end

# Output the id of the map with the shortest path or TRAP if no route.
puts (min_path_idx != -1 ? min_path_idx : "TRAP")
