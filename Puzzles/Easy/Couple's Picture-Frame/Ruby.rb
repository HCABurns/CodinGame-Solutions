# Get names.
wife = gets.chomp
husband = gets.chomp

# Find smallest common multiple.
width = wife.size.lcm(husband.size)

# Create new strings.
wife = wife * (width/wife.size).floor
husband = husband * (width/husband.size).floor

# Output the picture frame.
puts wife
husband.chars.zip(wife.chars).each{|char1 , char2| puts char1 + " "*(width-2) + char2}
puts husband
