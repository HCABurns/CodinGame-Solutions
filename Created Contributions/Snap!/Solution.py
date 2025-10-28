from collections import deque

p1 = deque([])
p2 = deque([])
p1_score = p2_score = 0

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
            p1_score += len(pile)
            while pile:
                p1.append(pile.pop())
            continue
        turn = 2

    if turn == 2:
        pile.append(p2.popleft())
        if len(pile) > 1 and pile[-1] == pile[-2]:
            p2_score += len(pile)
            while pile:
                p2.append(pile.pop())
            continue
        turn = 1

if p1_score > p2_score:
    print("Winner:","Player 1")
elif p2_score > p1_score:
    print("Winner:","Player 2")
else:
    print("Draw")
print(max(p1_score,p2_score))
