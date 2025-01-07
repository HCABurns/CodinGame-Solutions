# Get clues.
clues = gets.chomp.split(":")

# Variables for country and match amount.
country = "No guess"
max_matches = 0

# Find the country with the most matches.
n = gets.to_i
n.times do
  country_name,*info = gets.chomp.split(':')
  matches = info.map{|i| clues.include?(i) ? 1 : 0}.sum
  if matches > max_matches
    max_matches = matches
    country = country_name
  end
end

# Print country with most matches, otherwise No guess.
puts country
