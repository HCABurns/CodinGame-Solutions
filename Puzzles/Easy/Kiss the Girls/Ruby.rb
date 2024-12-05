# Define variable of number of kisses and odds array.
total_kisses = 0
odds = []

# Populate odds array with odds of catching monkeypox of a girl.
h, w = gets.split.map { |x| x.to_i }
h.times do |i|
  line = gets.chomp
  line.each_char.with_index do |char, j|
    odds << ([i,j].min.to_f / (i**2 + j**2 + 1)) if char == "G"
  end
end

# Sort based on probability of catching monekypox.
odds = odds.sort

# Find maximum number of girls that can be kissed with total chance of
# catching monkeypox is less than 40%.
(1..odds.size-1).each do |i|
  odds[i] = odds[i] + odds[i-1] - odds[i-1]*odds[i]
  total_kisses += 1 if odds[i] < 0.4
end

# Print number of people that can be kissed
puts odds[0] < 0.4 ? total_kisses+1 : total_kisses
