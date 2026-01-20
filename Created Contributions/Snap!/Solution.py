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
order = {"S":3,"H":2,"D":1,"C":0}

# Define central pile and starting turn
pile = []
turn = 0

"""
Function to perform the claiming of central pile

Return: int - Flag for which player is the next to play.
"""
def snap(top, bottom, turn):
    if order[top[1]] > order[bottom[1]]:
        deck = p1 if turn == 0 else p2
    else:
        deck = p2 if turn == 0 else p1
    deck.extend(pile)
    pile.clear()
    return 0 if deck == p1 else 1

# Simulate Snap until one player has no more cards.
while p1 and p2:
    deck = p1 if turn == 0 else p2
    pile.append(deck.popleft())
    if len(pile) > 1 and pile[-1][0] == pile[-2][0]:
        turn = snap(pile[-1],pile[-2], turn)
        continue
    turn ^= 1
    continue

# Print output.
if p1:
    print("Winner:","Player 1")
else:
    print("Winner:","Player 2")
print(max(len(p1),len(p2)))
