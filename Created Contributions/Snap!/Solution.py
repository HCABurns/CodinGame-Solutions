from collections import deque

# Populate player decks - First card = Top
p1 = deque([])
p2 = deque([])
m = int(input())
for i in range(m):
    card = input()
    p1.append([card[:-1],card[-1]])
n = int(input())
for i in range(n):
    card = input()
    p2.append([card[:-1],card[-1]])

# Define Suit order
order = {"S":3,"D":2,"H":1,"C":0}

# Define central pile and starting turn
pile = []
turn = 1

"""
Function to claim the cards in the central pile in case of snap.
"""
def snap(card1, card2):
    if order[card1[1]] > order[card2[1]]:
        deck = p1
    else:
        deck = p2
    while pile:
        deck.append(pile.pop())

# Simulate Snap until one player has no more cards.
while p1 and p2:
    if turn == 1:
        pile.append(p1.popleft())
        if len(pile) > 1 and pile[-1][0] == pile[-2][0]:
            snap(pile[-1], pile[-2])
            continue
        turn = 2
        continue

    if turn == 2:
        pile.append(p2.popleft())
        if len(pile) > 1 and pile[-1][0] == pile[-2][0]:
            snap(pile[-1], pile[-2])
            continue
        turn = 1
        continue

# Print output.
if p1:
    print("Winner:","Player 1")
else:
    print("Winner:","Player 2")
print(max(len(p1),len(p2)))
