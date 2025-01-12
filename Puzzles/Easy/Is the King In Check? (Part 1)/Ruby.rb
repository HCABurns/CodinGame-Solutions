# Get board and store position of pieces that aren't the king.
pieces = []
board = []
8.times do |i|
  chess_row = gets.chomp
  board << chess_row.tr(" ","")
  board[-1].chars.each.with_index{|char,j| pieces << [char,i,j] if "NRQB".include?(char)}
end

def is_check(start_i, start_j, directions, board)
  """
  Function to check if the king piece is in check.

  Parameters:
  start_i : int - Integer for row of the piece.
  start_j : int - Integer for column of the piece.
  directions : array - Array of array of directions to be checked. 

  Returns : boolean - True if the king is in check, otherwise false.
  """
  if board[start_i][start_j] == "K"
    return true
  end
  directions.each do |di,dj|
    i = start_i
    j = start_j
    while i + di >= 0 && i + di < 8 && j + dj >= 0 && j + dj < 8
      i += di
      j += dj
      return true if board[i][j] == "K"
      break if di.abs == 2 || dj.abs == 2
    end
  end
  return false
end

# Check each piece for if the king is in check.
check = false
pieces.each do |char, i, j|
  if char == "Q"
    if is_check(i,j,[[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,1],[1,-1],[-1,1]],board)
      check=true;break
    end
  elsif char == "R"
    if is_check(i,j,[[-1,0],[1,0],[0,-1],[0,1]],board)
      check=true;break
    end
  elsif char == "B"
    if is_check(i,j,[[-1,-1],[1,1],[1,-1],[-1,1]],board)
      check=true;break
    end
  elsif char == "N"
    if is_check(i,j,[[-2,1],[-2,-1],[-1,2],[-1,-2],[1,2],[1,-2],[2,-2],[2,-2]],board)
      check=true;break
    end
  end
end

# Print if the king is is check or not.
puts check ? "Check" : "No Check"
