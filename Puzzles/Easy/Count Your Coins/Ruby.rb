# Get required inputs.
value_to_reach = gets.to_i
n = gets.to_i

# Get coins and put into a sorted array in increasing order. 
coins = gets.split.zip(gets.split).each.map{|count , value| [value.to_f, count.to_i]}.sort

# Find the minimum coins required to reach value_to_reach.
#To do this go from the least value coins increasing until value is met or no more coins left.
total = 0
coins.each do |value , count|
  # Value is too large and needs only a proportion of the coins left.
  if value_to_reach - count*value < 0
    total += (value_to_reach/value).ceil
    value_to_reach = -1
  else
    #Value is too big still so add all the coins with this value
    value_to_reach -= count*value 
    total += count
  end
end

# Print correct output.
puts total > 0 && value_to_reach < 0 ? total : -1
