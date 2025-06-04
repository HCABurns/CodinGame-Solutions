# Form Grid.
grid = []
n = gets.to_i
inputs = gets.split
for i in 0..(n-1)
  grid << inputs[i].to_i
end

# Swaps left most 0 with right most 1 until R < L.
swaps, l, r = 0, 0, n-1
while l < r do
  while (l<r && grid[l] != 0) do
    l += 1
  end
  while l<r && grid[r] != 1 do
    r -= 1
  end
  if l < r
    swaps += 1
    l += 1
    r -= 1
  end
end
  
# Print number of swaps
puts swaps
