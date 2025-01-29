# Define the singles, doubles, and trebles as hash maps
singles = (1..20).to_a + [25]
singles = singles.map { |val| [val, "#{val}"] }.to_h

doubles = (1..20).map { |val| val * 2 } + [50]
doubles = doubles.map { |val| [val, "D#{val / 2}"] }.to_h

trebles = (1..20).map { |val| val * 3 }
trebles = trebles.map { |val| [val, "T#{val / 3}"] }.to_h

# Initialize a set to hold unique combinations
require 'set'
combinations = Set.new

# Recursive search function
def search(score, darts, left, singles, doubles, trebles, combinations)
  # Base cases
  return if score < 0 || left < 0

  if score == 0 && darts.any? && darts.last.include?("D")
    combinations.add(darts)
    return
  end

  # Choose the appropriate dart sets
  dart_sets = left > 1 ? [singles, doubles, trebles] : [doubles]

  dart_sets.each do |dart_set|
    dart_set.each do |dart, dart_str|
      search(score - dart, darts + [dart_str], left - 1, singles, doubles, trebles, combinations)
    end
  end
end

# Input: target score and number of darts
score = gets.to_i
darts = gets.to_i

# Start the recursive search
search(score, [], darts, singles, doubles, trebles, combinations)

# Output the result
puts combinations.size
