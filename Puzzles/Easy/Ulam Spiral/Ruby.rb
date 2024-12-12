# Directions array and current direction.
directions = [[-1,0],[0,-1,],[1,0],[0,1]]
current_direction = 0

# Form Grid
n = gets.to_i
grid_size = n
grid = []
n.times do
  grid << []
  n.times{grid[-1] << " "}
end

# Index of the grid.
i = j = n-1

# Value of bottom left
n **=2

# Check Ulam spiral for primes.
while n > 1
  # Determine if prime.
  prime = true
  test_n = n
  (2..((test_n+1)/2).floor).each do |k|
    if test_n % k == 0
      prime = false
      break
    end
  end
  
  # Set as prime or seen.
  if prime == true
      grid[i][j] = "#"
  else
      grid[i][j] = "X"
  end

  # If next is OOB or already visited then change direction.
  x, y = directions[current_direction]
  if j+x < 0 || j+x>=grid_size || i+y<0 || i+y>=grid_size || grid[i+y][j+x] != " "
    current_direction = (current_direction+1)%4
    x, y = directions[current_direction]
  end
  i += y
  j += x
  n -= 1
end

# Print grid - Replace seen with space character.
grid.each do |row|
  puts row.join(" ").tr("X"," ")
end
