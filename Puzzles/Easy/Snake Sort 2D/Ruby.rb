# Form grid and store rows with apples.
grid = []
100.times{grid << " "*100}
n = gets.to_i
rows = []
n.times do
  name, r, c = gets.split
  r = r.to_i
  c = c.to_i
  grid[r][c] = name
  rows << r if !rows.include?(r)
end

# Sort rows, create output variable and direction variable.
rows.sort!
output = []
direction = 1

# Go along the rows of apples in the correct order and store apples.
rows.each do |i|
  j = direction == 1 ? 0 : 99 
  while j >= 0 && j <= 99
    output << grid[i][j] if grid[i][j] != " "
    j += direction  
  end 
direction *= -1
end

# Print the apples the snake will eat.
puts output.join(",")
