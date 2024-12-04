# Define suits and values.
CARD = "23456789TJQKA"
SUITS = "SDHC"

# Define pile of cards array.
cards = []

# Populate set with cards.
SUITS.each_char do |suit|
  CARD.each_char do |card_value|
    cards << card_value+""+suit
  end
end

def cards_parser(card_string)
  cards_parsed = ""
  suits_parsed = ""
  card_string.each_char do |char|
    if SUITS.include?(char)
      suits_parsed += char
    else
      cards_parsed += char
    end
  end
  suits_parsed = SUITS if suits_parsed == ""
  cards_parsed = CARD if cards_parsed == ""
  return cards_parsed, suits_parsed
end

# Remove any cards defined.
r, s = gets.split.map { |x| x.to_i }
r.times do
  removed = gets.chomp
  cards_to_remove, suits_to_remove = cards_parser(removed)
  suits_to_remove.each_char do |suit|
    cards_to_remove.each_char do |card_value|
      cards.delete(card_value+""+suit) if cards.include?(card_value+""+suit)
    end
  end
end

# Find any cards sought after still in the deck.
sought_amount = 0
s.times do
  sought = gets.chomp
  cards_to_find, suits_to_find = cards_parser(sought)
  suits_to_find.each_char do |suit|
    cards_to_find.each_char do |card_value|
      if cards.include?(card_value+""+suit)
        cards.delete(card_value+""+suit) 
        sought_amount += 1
      end
    end
  end
end

# Print percentages of selecting one of the sought after cards.
puts ((sought_amount*100) / (cards.size+sought_amount)).round.to_s+"%"
