# Get stream of information and bust threshold.
stream_of_consciousness = gets.chomp.split(".")
bust_threshold = gets.to_i

# Convert threshold if required.
bust_threshold = "T" if bust_threshold == 10

# Form hashmap of cards and number of remaining in the deck.
card_string = "A23456789TJKQ"
cards = Hash.new
card_string.each_char{|card| cards[card] = 4}

# Remove cards from the deck if thought is only valid cards.
stream_of_consciousness.each do |thought|
    valid = true
    thought.each_char{|char| valid = false if (card_string.include? char)==false}
    thought.each_char{|char| cards[char] -= 1} if valid
end

# Find count of cards left under the threshold.
count_below = 0.0
count_total = 0.0
card_string.each_char{|card|
    count_below += cards[card] if card_string.index(card) < card_string.index(bust_threshold.to_s)
    count_total += cards[card]
}

# Output the percentage change of a card below the threshold.
print (count_below/count_total*100).round,"%"
