# Import queue data structure (Better efficiency that using array as queue)
# (This is because remove at front is O(1) in a queue but O(n) in an array)
from collections import deque

# Set up both players decks in a queue. (Only first char as suit doesn't matter)
# Convert from card value to integer value so it can be compared without extra searches.
cards = {"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"1":9,"J":10,"Q":11,"K":12,"A":13}
n = int(input()) 
p1 = deque(cards[input()[0]] for _ in range(n))
m = int(input())
p2 = deque([cards[input()[0]] for _ in range(m)])

# Helper function to add the cards to the correct pile in the correct order.
def fill(queue , pile1, pile2):
    for card in pile1:
        queue.append(card)
    for card in pile2:
        queue.append(card)
    pile1.clear()
    pile2.clear()

# Declare required variables.
war_pile = [[],[]]
PAT = False
rounds = 0

# Game loop
while len(p1)!=0 and len(p2)!=0:
    # Get next cards from the piles.
    card1 = p1.popleft()
    card2 = p2.popleft()
    war_pile[0].append(card1)
    war_pile[1].append(card2)

    # If cards values are not equal, add all cards to player with higher card.
    if card1 != card2:
        rounds += 1
        if card1<card2:
            fill(p2 , war_pile[0] , war_pile[1])
        else:
            fill(p1 , war_pile[0] , war_pile[1])
    else:
        #War case - Add 3 cards from each piles to their war pile. If not possible then set PAT and break.
        if len(p1) < 3 or len(p2)<3:
            PAT = True
            break
        for i in range(3):
            war_pile[0]+=[p1.popleft()]
            war_pile[1]+=[p2.popleft()]

# Output the winner and how many rounds it took or PAT.
if PAT:
    print("PAT")
elif len(p1) > len(p2):
    print("1" , rounds)
else:
    print("2", rounds)
