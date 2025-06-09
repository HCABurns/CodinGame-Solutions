#NOTE: All coordinates are in the form [y,x] or [row,column]
#Form grid from inputs and find coordinates of all "a" characters and store in array.
n = gets.to_i
starts = []
$grid = []
n.times.map do |i|
  row = gets.chomp
  $grid << row
  row.chars.each_with_index do |char, j|
    starts << [i,j] if char == "a" 
  end
end

"""
Search function used for BFS searching grid for next character

Parameters:
int y - Row index to be searched
int x - Column index to be seached
String char - Character to be searched for. 

Return:
boolean - Boolean value indicating if Z has been found.
"""
def search(y,x,char)
  return true if char == ("z".ord+1).chr
  
  #If an index is out of the grid, return False. 
  return false if (y < 0 || y>=$grid.size || x<0 || x>=$grid[0].size)

  #Check if position has value of char.
  if $grid[y][x] == char
    #Set output array to char in correct position.
    $out[y][x] = char
    next_char = (char.ord+1).chr
    #Search in each direction from current position.
    v1 = search(y+1,x,next_char)
    v2 = search(y-1,x,next_char)
    v3 = search(y,x-1,next_char)
    v4 = search(y,x+1,next_char)
    #Check if Z has been found or not.
    if (v1==v2 && v1==v3 && v1==v4 && v1==false)
      $out[y][x] = "-"
      return false
    end
    #If any search returns True then return True - Indicates search has resulted in Z being found
    return true
  end
  return false
end

#Check all the start positions if they result in the correct sequence.
starts.each do |pos|
  y, x = pos
  #Reset output
  $out = []
  n.times{ $out << "-"*$grid[0].size}
  
  #Search starting with a character
  if search(y,x,"a")
    $out.each{|row| puts row}
    break
  end
end
