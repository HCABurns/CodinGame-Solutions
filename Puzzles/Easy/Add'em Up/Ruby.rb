# Get inputs, map to int and sort in decreasing order.
n = gets.to_i
cards = gets.split.map(&:to_i).sort.reverse

# Set total and idx.
total = 0
idx = cards.size - 1

# While there is still cards to be combined, combine the cheapest cost.
while cards.size > 1
  # Get new card and increment cost.
  new_card = cards.pop() + cards[-1]
  total += new_card

  # Set last item to new card.
  cards[-1] = new_card

  # Sort again with the new card in the list.
  cards = cards.sort.reverse
end

# Output total minimum.
p total
