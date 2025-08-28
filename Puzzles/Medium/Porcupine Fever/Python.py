from collections import deque

n = int(input())
y = int(input())

# Sum alive porcupines and store farm information.
porcupines = deque()
alive = 0
for i in range(n):
    s, h, a = [int(j) for j in input().split()]
    alive += a
    if s > 0:
        porcupines.append([s,h])

# Perfrom y years of simulations.
for i in range(y):
    tmp = deque()
    while porcupines:
        s,h = porcupines.popleft()

        # Sick die
        alive -= s
        
        # Infect other porcupines.
        tmp_s = s
        s = 0
        while tmp_s > 0 and h > 0:
            if h == 1:
                h -= 1
                s += 1
            else:
                h -= 2
                s += 2
            tmp_s -= 1
        
        # Update
        if s != 0:
            tmp.append([s,h])
    porcupines = tmp
    
    # Print number of alive porcupines.
    print(alive)
    if alive == 0:break
