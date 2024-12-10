# Array for horses.
horses = []

# Store horses.
n = gets.to_i
n.times do
  v, e = gets.split.map { |x| x.to_i }
  horses << [v, e]
end

# Find minimum difference.
min_val = 1e9
(0..horses.size-2).each do |i|
  (i+1..horses.size-1).each do |j|
    min_val = [min_val,(horses[i][0] - horses[j][0]).abs + (horses[i][1] - horses[j][1]).abs].min
  end
end

# Print min difference.
puts min_val
