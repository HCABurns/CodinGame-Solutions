# Get inputs.
decimal_value = gets.to_i
alphabet = gets.chomp

# Ensure not 0 input.
if decimal_value == 0
  puts alphabet[0]
  exit!
end

# Get base and output.
base = alphabet.size
out = ""

# Continue until converted from base 10 to base len(c).
while decimal_value > 0
  decimal_value -= 1 if out != "" # Since aa = 4 instead of ba - Minus 1 each loop to set correct.

  # Regular base conversion.
  rem = decimal_value % base
  out += alphabet[rem]
  decimal_value = (decimal_value / base).floor
end

# Output the conversion.
puts out
