# Get card amount and deck.
n = int(input())
deck = input().split(" ")

# Complete algorithm n times.
for i in range(n):
    new_deck = []
    pile1 = deck[:len(deck)//2]  if len(deck)%2 == 0 else deck[:(len(deck)//2)+1] 
    pile2 = deck[len(deck)//2+1:] if len(deck)%2 == 1 else deck[(len(deck)//2):] 
    for card1, card2 in zip(pile1,pile2):
        new_deck += [card1]
        new_deck += [card2]
    if len(pile1) > len(pile2):
        new_deck += [pile1[-1]]
    deck = new_deck

# Print shuffled deck.
print(*deck)
