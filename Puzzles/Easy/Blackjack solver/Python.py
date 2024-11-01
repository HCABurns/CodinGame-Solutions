# Get inputs cards.
bank_cards = input().split(" ")
player_cards = input().split(" ")

# Convert to JQK to 10 and 1 for A
bank = [[i,[10,1]["A"==i]][i in "AJQK"] for i in bank_cards]
player = [[i,[10,1]["A"==i]][i in "AJQK"] for i in player_cards]

# Get two scores for player and bank. Score1 A is 1, score2 A is 11.
player_score1 = sum(int(i) for i in player)
player_score2 = player_score1
for i in range(player.count(1)):
    if player_score2 + 10 <= 21:
        player_score2 += 10
bank_score1 = sum(int(i) for i in bank)
bank_score2 = bank_score1
for i in range(bank.count(1)):
    if bank_score2 + 10 <= 21:
        bank_score2 += 10

# Find best score, 0 if bust for bank and -1 for player bust.
player = player_score2
if player > 21 and player_score1 > 21:
    player = -1
elif player_score2>21:
    player = player_score1

bank = bank_score2
if bank > 21 and bank_score1 > 21:
    bank = 0
elif player_score2>21:
    bank = bank_score1

# Output the correct result.
if player == 21 and len(player_cards)==2 and bank == 21 and len(bank_cards)==2:
    print("Draw")
elif player == 21 and len(player_cards)==2:
    print("Blackjack!")
elif bank == player:
    print("Draw")
elif bank > player:
    print("Bank")
else:
    print("Player")
