# Get text, covert to lowercase and remove any non-alpha characters.
text = gets.chomp.chars.select{|char| char.match(/[A-Za-z]/)}.join.downcase

# Set array for max string and max word.
max_str = ["",""]

# Check text for given hidden words.
gets.to_i.times do
  word = gets.chomp

  # If current word length is less than max, continue as it can't be longer.
  next if word.size < max_str[0].size

  # Get possible starting positions.
  starts = []
  text.chars.each.with_index{|char , i| starts << i if char == word[0]}

  # Check all starting positions for hidden word.
  starts.each do |pos|
    # Check evenly spaced positions for "word"
    (1..((text.size-pos)/(word.size-1)).ceil).each do |j|
      hidden_word = word.size.times.map{|i| text[pos+j*i]}.join
      # If found, add capitalization where required and set new max.
      if hidden_word == word
        txt = text[pos,j*(word.size-1)+1]
        word.size.times{|i| txt[i*j] = hidden_word[i].upcase}
        max_str = [word , txt]
      end
    end
  end
end

# Output the max hidden string.
puts max_str[1]
