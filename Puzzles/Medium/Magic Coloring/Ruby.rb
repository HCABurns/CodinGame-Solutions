# Form Grid.
valid = false
grid = []
x, y = gets.split.map { |x| x.to_i }
y.times do
  line = gets.chomp
  valid = true if line.count("123456789") > 0
  grid << line
end

# If no colouring positions, print and quit.
if !valid
  puts "No coloring today"
  exit()
end

# Fill all connectect "val" with "0"
def fill(i, j, val, y, x, grid)
  return if i<0 || i>=y || j<0 || j>=x || grid[i][j] != val
  grid[i][j] = "0"

  [[1,0],[-1,0],[0,1],[0,-1]].each do |iy,jx|
    fill(iy+i,jx+j,val, y ,x, grid)
  end
  return 
end

# Find the sections, count sections and fill with 0s. 
total = Hash.new(0.0)
y.times do |i|
  x.times do |j|
    if grid[i][j] != "0"
      val = grid[i][j]
      fill(i, j, val, y, x, grid)

      total[val.to_s] += 1
    end
  end
end

# Print out the number of segments of each colour.
total.sort.each do |val, count|
  puts "#{val} -> #{count.to_i}"
end
