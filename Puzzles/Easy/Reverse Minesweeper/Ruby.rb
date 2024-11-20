# Get dimensions and form grid. Keep track of mines positions to be used.
grid = []
mines = []
directions = [[1,0],[-1,0],[0,-1],[0,1],[-1,-1],[1,1],[1,-1],[-1,1]]
w = gets.to_i
h = gets.to_i
h.times do |i|
  grid << []
  line = gets.chomp
  line.chars.each_with_index do |char, j|
    grid[-1] += [char]
    if char == "x"
      mines << [i,j]
      grid[i][j] = "x"
    end
  end
end

# Set +1 for all available squares around a bomb.
mines.each do |i ,j|
  directions.each do |x , y|  
    iy = i + y
    jx = j + x
    if 0<=iy && iy<grid.size && 0<=jx && jx<grid[0].size
      if grid[iy][jx] != "x"
        if grid[iy][jx] == "."
          grid[iy][jx] = 0
        end
        grid[iy][jx] += 1
      end
    end
  end
end

# Output the changed grid.
grid.each{|row| puts row.join.tr("x",".")}
