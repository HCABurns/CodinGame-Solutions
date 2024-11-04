# Hashmap for conversion.
MORSE = {'A'=> '.-', 'B'=> '-...', 'C'=> '-.-.', 'D'=> '-..', 'E'=> '.', 'F'=> '..-.', 'G'=> '--.', 'H'=> '....', 'I'=> '..', 'J'=> '.---', 'K'=> '-.-', 'L'=> '.-..', 'M'=> '--', 'N'=> '-.', 'O'=> '---', 'P'=> '.--.', 'Q'=> '--.-', 'R'=> '.-.', 'S'=> '...', 'T'=> '-', 'U'=> '..-', 'V'=> '...-', 'W'=> '.--', 'X'=> '-..-', 'Y'=> '-.--', 'Z'=> '--..'}

# Get the unknown morse and store length.
unknown_morse = gets.chomp

# Convert words into morse.
words = []
gets.to_i.times do
  word = gets.chomp
  morse_word = word.each_char.map { |char| MORSE[char] }.join
  words << morse_word
end

# Create a cache for memoization.
cache = {}
def search(idx, unknown_morse, words, cache)
  # If idx is length of morse, it's a valid combination.
  return 1 if idx == unknown_morse.size

  # If idx in cache then return result.
  return cache[idx] if cache.key?(idx)

  combinations = 0
  # Recursively search if current combination is equal to the unknown_morse of the same length.
  words.each do |word|
    if unknown_morse[idx, word.size] == word
      combinations += search(idx + word.size, unknown_morse, words, cache)
    end
  end

  # Cache result and return.
  cache[idx] = combinations
  return combinations
end

# Return the number of possible ways to dorm unknown morse with given dictionary.
puts search(0, unknown_morse, words, cache)
