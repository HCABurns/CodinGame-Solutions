# Get inputs.
height = gets.to_i
width = gets.to_i
threshold = gets.to_i

# Create visited set.
visited = {}

# Check each position and ensure value is below threshold and the cell is reachable from other valid cells.
(0..height-1).each do |i|
  (0..width-1).each do |j|
    if i==0 || visited.key?([i-1,j]) || visited.key?([i,j-1])
      sum_val = i.to_s.chars.map{|x| x.to_i}.sum + j.to_s.chars.map{|x| x.to_i}.sum
      if sum_val <= threshold
        visited[[i,j]] = 1 
      end
    end
  end
end
# Print number of valid cells.
puts visited.size
