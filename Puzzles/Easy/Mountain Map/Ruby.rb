# Get number of mountains and form a array of the heights.
n = gets.to_i
inputs = gets.split
heights = []
for i in 0..(n-1)
  heights << inputs[i].to_i
end

# Get width and height of the grid.
width = heights.sum*2
height = heights.max

# Form Grid
grid = [] 
height.times{grid << [" "]*width}

# Place mountains in the correct places in the grid.
i = height-1
j = 0
heights.each do |height|
  height.times{
    grid[i][j] = "/"
    i-=1
    j+=1
  }
  i+=1

  height.times{
    grid[i][j] = "\\"
    i+=1
    j+=1
  }
  i-=1
end

# Print grid with rstrip to remove trailing spaces.
grid.each{|row| puts row.join('').rstrip}
