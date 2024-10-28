#NOTE: Code converted from 'if then end' to {} for testing.
# Get required inputs.
w, h = gets.split.map { |x| x.to_i }

# Get starting position
chars = gets.split(" ")

grid = []
(h-2).times{|i|
  line = gets.chomp

  # On first run, form grid.
  if i==0 then
    line.each_char.with_index{|char,index|
    grid << index if char == "|"
    }
  end

  # Iterate over the grid, row by row, checking for steps to move over columns.
  grid.each_with_index{|column,j|
    # Check  if moving right - If so, shift to next column
    grid[j] += 3  if column != line.size-1 and line[column+1] == "-"
      
    # Check if moving left - If so, shift to previous column
    grid[j] -= 3 if column != 0 and line[column-1] == "-"
  }
}

# Output starting charater with ending position character. 
end_chars = gets.split(" ")
chars.each_with_index{|i,j|
  puts chars[j].to_s+end_chars[grid[j]/3].to_s
}
