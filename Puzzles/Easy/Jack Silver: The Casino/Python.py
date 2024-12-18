# Import for ceiling round.
from math import ceil

# Get rounds amount and starting cash amount.
rounds = int(input())
cash = int(input())
for i in range(rounds):
    # Get bet and remove from cash.
    bet_amount = ceil(cash/4)
    cash -= bet_amount
    
    # Get the play and get required variables.
    play = input().split(" ")
    number = int(play[0]) 
    bet = play[1]
    
    # Detemrine if bet it a win or loss. 
    if bet == "ODD":
        if number % 2 == 1:
            cash += bet_amount*2
    elif bet == "EVEN":
        if number != 0 and number % 2 == 0:
            cash += bet_amount*2
    else:
        if number == int(play[2]):
            cash+= bet_amount * 36

# Print cash after playing.
print(cash)
