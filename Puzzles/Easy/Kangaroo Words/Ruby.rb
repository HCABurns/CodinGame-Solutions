# Array for storing words and their joey words.
kangaroo_and_joeys = []

n = gets.to_i
n.times do
  # Get words.
  lines = gets.chomp.split ", "

  # Find all joey words for each word.
  lines.each do |word|
    matches = []
    lines.each do |joey|
      next if joey == word
      # Check if joey is a joey for word.
      i = j = 0
      while i < word.size && j < joey.size do 
        while i != word.size && word[i] != joey[j] do 
          i+=1
        end
        j += 1
        i += 1
      end
      matches << joey if j == joey.size && i != word.size+1
    end
    # If word is a kangaroo word, add to the array.
    kangaroo_and_joeys << [word,matches] if matches != []
  end
end

# Print the word and their joey words. If none then print NONE.
if kangaroo_and_joeys.size == 0
  puts "NONE"
else
  kangaroo_and_joeys.sort.each do |word, joeys|
    puts "#{word}: #{joeys.join ', '}"
  end
end
