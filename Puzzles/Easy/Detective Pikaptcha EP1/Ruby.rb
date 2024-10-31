# Form Grid
grid = []
width, height = gets.split.map { |x| x.to_i }
height.times{
  grid << []
  gets.chomp.each_char do |char|
    grid[-1] << char
  end
}

# Set directions to be checked.
directions = [[1,0],[-1,0],[0,1],[0,-1]]

# Traverse grid setting each open square to number of neighbours which aren't walls.
grid.each.with_index do |row , i|
  row.each.with_index do |char , j|
    if char == "0"
      neighbours = 0
      directions.each do |x,y|
        neighbours += 1 if i+y>=0 && i+y<height && j+x >=0 && j+x <width && grid[i+y][j+x] != "#"
      end
      grid[i][j] = neighbours.to_s
    end
  end
end

# Output the ammended grid.
grid.each{|row| puts row.join}
