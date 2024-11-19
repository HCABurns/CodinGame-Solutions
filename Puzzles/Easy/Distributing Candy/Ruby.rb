# Get bags of sweets and sort in increasing order.
n, m = gets.split.map { |x| x.to_i }
sweets = gets.split.map(&:to_i).sort

# Output minimum difference between m sweet bags.
puts (0..n-m).map{|i| sweets[i+m-1] - sweets[i]}.min
