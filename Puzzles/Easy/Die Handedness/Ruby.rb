# Form grid.
grid = []
3.times do
  grid << gets.chomp.strip # One line out of three in the string describing the arrangement of the numbers.
end

# Determine which pairs are in the middle given 1,2,3 at the top or bottom.
# If 1,2,3 at the bottom, then reverse middle.
right_handed = {"1"=>"23","2"=>"31","3"=>"12"}
if !"123".include?(grid[0][0])
  key = grid[2][0]
  grid[1] = grid[1].reverse
else
  key=grid[0][0]
end

# Output one of "right-handed", "left-handed" and "degenerate".
pairs = [[grid[0][0],grid[2][0]] , [grid[1][0],grid[1][2]], [grid[1][1],grid[1][3]]]
if pairs.select{|x,y| x.to_i+y.to_i!=7}.size > 0
  puts "degenerate"
elsif (grid[1]*2).include?(right_handed[key])
  puts "right-handed"
else
  puts "left-handed"
end
