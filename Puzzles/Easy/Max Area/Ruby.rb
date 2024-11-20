# Get heights of the segments.
height = []
n = gets.to_i
gets.split.each{|val| height << val.to_i}

# Left and right pointers.
l = 0
r = height.size - 1

# Max size variable.
max_area = 0

# Shift left and right pointers to find max area.
while l < r do 
  size = [height[l], height[r]].min * (r - l)
  max_area = [max_area , size].max
  if height[l] > height[r]
    r -= 1
  else
    l += 1
  end
end

# Output the max area.
puts max_area
