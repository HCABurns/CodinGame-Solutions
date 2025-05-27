# Get the value and set the remainder.
n = gets.to_i
remainder = 1

# Array for storing ints, hashmap for storing index and index.
res = []
values = Hash.new()
idx = 0

# Complete the divison until terminates or repeat found.
while remainder != 0 do
  # Check for repeating remainder.
  if values.has_key?(remainder)
    res.insert(values[remainder], "(")
    res << ')'
    break
  end
  values[remainder] = idx

  # Complete the division.
  remainder = remainder * 10
  val = (remainder / n).to_i
  res << val.to_s
  remainder = remainder % n
  # Increment index variable.
  idx += 1   
end

# Print the value.
print "0."+res.join
