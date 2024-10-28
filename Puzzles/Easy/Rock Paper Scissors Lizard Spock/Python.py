#Hashmap of which options beat others.
hashmap = {"C":"PL" , "R":"LC", "P":"RS", "L":"PS","S":"RC"}

# Create array of players - number, sign and array of players bat.
players = []
n = int(input())
for i in range(n):
    inputs = input().split()
    numplayer = int(inputs[0])
    signplayer = inputs[1]
    players.append([numplayer, signplayer, []])

# Run simulation.
while len(players) > 1:
    for p1 , p2 in zip(players[0::2],players[1::2]):
        
        # Set to_remove to be pointer to the loser of the duel.
        if p1[1] == p2[1]:
            to_remove = p1 if p1[0] > p2[0] else p2
        elif p2[1] in hashmap[p1[1]]:
            to_remove = p2
        else:
            to_remove = p1
        
        # Add to the list of players beat.
        if to_remove == p1:
            p2[2].append(p1[0])
        else:
            p1[2].append(p2[0])
        players.remove(to_remove)

# Output winner number and numbers of players they beat.
print(players[0][0])
print(*players[0][2])
