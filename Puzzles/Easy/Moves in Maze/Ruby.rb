#NOTE: Coordinates are formed as [y,x] / [Row , column]
w, h = gets.split.map { |x| x.to_i }

#Form grid in 2d array and store position of "S" in start
grid = []
start = []
h.times do |i|
  row = gets.chomp
  grid << row
  if row.include?("S")
    start = [i, row.index("S")]
    grid[i][start[1]] = "."
  end
end

#Iterative BFS changing any . characters to the next in the sequence
to_visit = [start]
val = 0
while to_visit.length > 0 do
  tmp = []
  while to_visit.length > 0 do
    node = to_visit.pop
    #Wrap the value (Wraps around the grid)
    x = node[1] % w
    y = node[0] % h
    #If spot is empty -> Add to the list and set to current character in sequence.
    if grid[y][x] == "."
      grid[y][x] = val < "A".ord ? val.to_s : val.chr
      tmp << [y+1,x]
      tmp << [y-1,x]
      tmp << [y,x-1]
      tmp << [y,x+1]
    end
  end

  #Update to_visit list and character in the sequence.
  to_visit = tmp
  val += 1
  val = "A".ord if val == 10
end

#Print out the changed grid.
grid.each{|row| puts row}
