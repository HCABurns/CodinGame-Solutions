from collections import deque

p1 = deque([])
p2 = deque([])

m = int(input())
for i in range(m):
    card = input()
    p1.append(card[0])

n = int(input())
for i in range(n):
    card = input()
    p2.append(card[0])

pile = []
turn = 1

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

if p1:
    print("Winner:","Player 1")
elif p2:
    print("Winner:","Player 2")
else:
    print("Draw")
print(max(len(p1),len(p2)))
