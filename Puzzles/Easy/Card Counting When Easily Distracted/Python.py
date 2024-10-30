# Get stream of information and bust threshold.
stream_of_consciousness = input().split(".")
bust_threshold = int(input())

# Convert threshold if required.
if bust_threshold == 10:
    bust_threshold = "T"

# Form hashmap of cards and number of remaining in the deck.
card_string = "A23456789TJKQ"
cards = {card:4 for card in card_string}

# Remove cards from the deck if thought is only valid cards.
for thought in stream_of_consciousness:
    if all(1 if i in cards else 0 for i in thought):
        for card in thought:
            cards[card] -= 1

# Find count of cards left under the threshold.
count_below = sum(cards[card] for card in card_string[:card_string.index(str(bust_threshold))])

# Output the percentage change of a card below the threshold.
print(f"{round(count_below / sum(cards.values()) * 100)}%")
