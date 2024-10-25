from collections import deque 

# Declare required parameters.
n = int(input())
players = [] # Array of queues.
names = [[0,input()] for i in range(n)] #Array of Arrays of round count and player name.
scores = [] # Array of ints indicating score.
for i in range(n):
    players.append(deque())
    scores.append(0)
    for j in input().split():
        players[i].append(j)
players_go = 0 # Int representing index of player whos throwing.

# Game loop - Runs each round one player at a time - Saves having to go through
# all possibilties and ends when one player hits 101.
while True:
    # Required variables.
    #tmp_score = scores[players_go]
    misses = 0
    prev = ""
    names[players_go][0] +=1
    tmp_score = scores[players_go]
    # Run 3 throws simulation, unless early exit.
    for i in range(3):
        # Get the players throw and change value if miss.
        val = players[players_go].popleft()
        if val == "X":
            misses+=1
            val = "-20"
            if prev == "-20":
                val = "-30"
            elif misses == 3:
                scores[players_go]=0
                break
        prev = val

        # Add correct value to the tmp score.
        scores[players_go] += eval(val)

        #Finished, bust or missed too many.
        if scores[players_go] > 101:
            scores[players_go] = tmp_score
            break
        if scores[players_go] == 101:
            # Exit case.
            break

    if scores[players_go] == 101:
            # Exit case.
            break
    
    # Change players_go to the next player.
    players_go += 1
    if players_go == n:
        players_go = 0

# Output the name of the user with 101.
for i,score in enumerate(scores):
    if score == 101:
        print(names[i][1])
        break
