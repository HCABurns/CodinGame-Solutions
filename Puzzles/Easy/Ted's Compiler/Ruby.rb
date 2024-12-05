# Get input.
line = gets.chomp

# Define stack and int variable to hold number of matching (prefix only)
stack = []
longest_valid = 0

# Count pairs and end if invalid.
line.each_char do |char|
  if char == "<"
    stack << "<"
  else
    if stack.size == 0
      break
    else
      longest_valid += 2 if stack.pop() == "<"
    end
  end
end
                
# Output longest valid prefix length. 
puts longest_valid
