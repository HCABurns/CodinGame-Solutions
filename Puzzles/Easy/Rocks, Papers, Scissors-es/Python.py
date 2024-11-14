# Define hashmaps to be used.
beats = {"Scissors":"Paper","Paper":"Rock","Rock":"Scissors"}
loses = {"Scissors":"Rock","Rock":"Paper","Paper":"Scissors"}

# Get all players choices and store in array.
n = int(input())
players = []
for i in range(n):
    a = input()
    players.append(a)

# Find the best choice and starting position to win the most without losing once.
max_winning = 0
max_selection = ["",0]
for i in range(len(players)):
    first_opponent_idx = (i+1)%n
    wins = 1
    player_selection = loses[players[first_opponent_idx]]
    for j in range(0,len(players)-1):
        if beats[player_selection] == players[(first_opponent_idx+j)%n]:
            wins+=1
        elif loses[player_selection] == players[(first_opponent_idx+j)%n]:
            break
    if wins > max_winning:
        max_winning = wins
        max_selection = [player_selection,first_opponent_idx]

# Output choice and first opponent id.
print(max_selection[0])
print(max_selection[1])
