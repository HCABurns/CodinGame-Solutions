# Get sequence.
sequence = gets.chomp

# Hashmap for storing weights, how many tags are opened and index.
weights = Hash.new(0.0)
open_count = 0
idx = 0

# Count number of open, when closed add open to char hashmap, open - 1
while idx < sequence.size
  # Get character.
  char = sequence[idx]

  # If not a closing tag, increment open.
  if char != "-"
    open_count += 1
  # If closing tag, store weight.
  else
    idx += 1
    weights[sequence[idx]] += 1.0 / open_count
    open_count -= 1
  end
  idx += 1
end

# Print max weight of tag.
puts weights.max_by{|_,weight| weight}[0]
