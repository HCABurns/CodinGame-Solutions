# Get number of inputs - Irrelevant so dont store
gets

# Map all values to int and store in array.
arr = gets.split.map(&:to_i)

# Print index of max value using y*-y to sort. (to_i used to convert nil to 0)
puts arr.max_by{|y| [y*-y,y]}.to_i
