# Form grid.
GRID = []
HEIGHT = gets.to_i
HEIGHT.times do
  GRID << gets.chomp.chars.map(&:to_i)
end

# Get prizes.
PRIZES = []
(HEIGHT+1).times do
  PRIZES << gets.to_i
end

# Cache for efficiency.
cache = {}
def search(i, j, multiplier, cache) 
  # Goal case, return multiplier * prize amount.
  return multiplier * PRIZES[j] if i == HEIGHT

  # If in cache, return result.
  return cache[[i,j,multiplier]] if cache.key?([i,j,multiplier])
      
  # Get max of left and right.
  max_score = [search(i+1, j, multiplier+GRID[i][j], cache) , search(i+1, j+1,multiplier+GRID[i][j], cache)].max

  # Cache score and return.
  cache[[i,j,multiplier]] = max_score
  return max_score
end

# Output the max score.
puts search(0,0,0, cache)
