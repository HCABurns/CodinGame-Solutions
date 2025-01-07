# Hashmap for converting
units = ["um", "mm", "cm", "dm", "m", "km"]
meter_conversion = [6, 3, 2, 1, 0, -3]

# Get left and right
left, right = gets.chomp.split(" + ")

# Get values
left_value = left.chars.select { |i| i =~ /[0-9.]/ }.join.to_f
right_value = right.chars.select { |i| i =~ /[0-9.]/ }.join.to_f

# Get units
left_units = left.chars.select { |i| i =~ /[a-zA-Z]/ }.join
right_units = right.chars.select { |i| i =~ /[a-zA-Z]/ }.join

# Get index of units
lidx = units.index(left_units)
ridx = units.index(right_units)

# Convert the larger to the smaller units
if lidx == ridx
  result_units = left_units
elsif lidx > ridx
  left_value *= 10**-meter_conversion[lidx]
  result_units = right_units
  left_value *= 10**meter_conversion[ridx]
elsif lidx < ridx
  right_value *= 10**-meter_conversion[ridx]
  result_units = left_units
  right_value *= 10**meter_conversion[lidx]
end

# Print the calculation in the smaller units
sum_val = left_value + right_value
if result_units == "um"
  sum_val = sum_val.to_i if sum_val == sum_val.to_i
  sum_val = sum_val.round(2) unless sum_val == sum_val.to_i
else
  sum_val = sum_val.to_i if sum_val == sum_val.to_i
end
puts "#{sum_val}#{result_units}"
