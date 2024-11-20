# Get inputs, map to int and sort in decreasing order.
n = int(input())
cards=sorted(map(int,input().split()) , reverse = True)

# Set total.
total = 0

# While there is still cards to be combined, combine the cheapest cost.
while len(cards) > 1:
    # Get new card and increment cost.
    new_card = cards.pop() + cards[-1]
    total += new_card

    # Set last item to new card.
    cards[-1] = new_card

    # Sort again with the new card in the list.
    cards.sort(reverse=True)

# Output total minimum.
print(total)
