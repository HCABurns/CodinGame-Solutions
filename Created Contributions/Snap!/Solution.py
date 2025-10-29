from collections import deque

# Populate player decks - First card = Top
p1 = deque([])
p2 = deque([])
m = int(input())
for i in range(m):
    card = input()
    p1.append(card[:-1])
n = int(input())
for i in range(n):
    card = input()
    p2.append(card[:-1])

# Define central pile and starting turn
pile = []
turn = 1

# Simulate Snap until one player has no more cards.
while p1 and p2:
    if turn == 1:
        pile.append(p1.popleft())
        if len(pile) > 1 and pile[-1] == pile[-2]:
            while pile:
                p1.append(pile.pop())
            continue
        turn = 2
        continue

    if turn == 2:
        pile.append(p2.popleft())
        if len(pile) > 1 and pile[-1] == pile[-2]:
            while pile:
                p2.append(pile.pop())
            continue
        turn = 1
        continue

# Print output.
if p1:
    print("Winner:","Player 1")
else:
    print("Winner:","Player 2")
print(max(len(p1),len(p2)))
