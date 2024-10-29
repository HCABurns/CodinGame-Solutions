# Get width and hight of shape to fit
a, b = gets.split.map { |x| x.to_i }

# Find shape coordinates relative to the first * characters.
shape = []
start = []
a.times do |i|
  gets.chomp.each_char.with_index{|char , j|
      if char == "*"
        if start == []
          start = [i,j]
          shape << [0,0]
        else
          shape << [i-start[0], j-start[1]]
        end
      end
  }
end

# Form grid.
c, d = gets.split.map { |x| x.to_i }
grid = []
c.times{grid << gets.chomp}

def shape_can_fit(grid,shape,i,j,height,width)
  """
    Helper function to determine if the shape can fit when placed at i,j

    Parameters:
    grid : 2D Array - 2D Array of the grid to be checked.
    shape : 2D Array - 2D Array of the postions of the shape from one character.
    i : int - Row index of start position.
    j : int - Column index of start position.
    height : int - Height of the grid
    width : Width of the grid.

    Returns: boolean - True if the shape can fit otherwise False.
    """
  shape.each do |x,y|
    ix = i + x
    jy = j + y
    if ix<0 || ix>=height || jy <0 || jy >= width
      return false
    elsif grid[ix][jy] != "."
      return false
    end
  end
  return true
end

# Find positions that the shape can fit and store in array.
positions = []
grid.each.with_index do |row, i|
  row.each_char.with_index do |col , j|
    if col == "."
      if shape_can_fit(grid,shape,i,j,c,d){}
        positions << [i,j]
      end
    end
  end
end

# Output number of positions and if only one, place the shape in and print.
p positions.size
if positions.size == 1
  shape.each{|x,y| grid[positions[0][0] + x][positions[0][1] + y] = "*"}
  puts grid
end
