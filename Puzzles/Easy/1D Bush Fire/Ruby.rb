# Get the number of bush fires.
n = gets.to_i
n.times do
  # Get bush fire.
  grid = gets.chomp + ".."
  
  # Start at i = 2 and with 0 water used.
  i = 2
  water = 0

  # Go through the array and find fires to put out.
  while i < grid.size do
    if grid[i-2] == "f"
      water += 1
      grid[(i-2)..i] = "..."
    end
    i += 1
  end
  # Print the number of water used to put out the fires.
  puts water
end
