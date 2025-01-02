# Dictionary for converting direction to character.
chars = { "right" => ">", "left" => "<" }

# Get input information.
input_data = gets.chomp.split
direction, *rest = input_data
amount, height, width, spacing, indent = rest.map(&:to_i)

# Print the 'turn here sign'.
range = direction == "left" ? (height / 2...height + height / 2) : (0...height)
range.each do |i|
  spaces = " " * indent * (i < height / 2 ? i : (height - i - 1).abs)
  content = ([chars[direction] * width] * amount).join(" " * spacing)
  puts spaces + content
end
