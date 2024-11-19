# Get grid size and from grid.
grid = []
quarter_size = gets.to_i
quarter_size.times do
  row = gets.chomp
  grid << row
end

# Helper function to convert a quadrant of the tile.
#
# Parameters:
# string : String - String to be transformed.
# direction : Integer - 0 indicates horizontal transformation, 1 indicates vertical transformation.
#
# Returns: String - Transformed string with required swaps.
def swapper(string , direction)
  if direction == 0
    string = string.tr("bpdq/\\\\","dqbp\\\\/")
  else
    string = string.tr("bdpq/\\\\" , "pqbd\\\\/")
  end
  return string
end

# Print border.
puts "+"+ "-"*grid[0].size*2 + "+" + "-"*grid[0].size*2 + "+"

# Create the top half and then the bottom half.
2.times do
    # Leave the TOP LEFT and horizontally flip the row for TOP RIGHT.
    new_grid = []
    grid.each do |row|
      tl = row
      tr = swapper(row,0).reverse
      new_row = tl+tr
      new_grid << ["|"+ new_row +"|" + swapper(new_row.reverse,0)+"|"]
    end

    # Vertical flip for BOTTOM LEFT and Vertical and Horizontal flip for BOTTOM RIGHT.
    grid.reverse.each do |row|
      bl = swapper(row,1)
      br = swapper(swapper(row,0),1).reverse
      new_row = bl + br
      new_grid << ["|"+new_row+"|" +swapper(new_row.reverse,0)+"|"]
    end
    # Print the half of the grid that has been formed.
    new_grid.each{|row| puts row}
    
    # Print splitter.
    puts "+"+ "-"*grid[0].size*2 + "+" + "-"*grid[0].size*2 + "+"
end
