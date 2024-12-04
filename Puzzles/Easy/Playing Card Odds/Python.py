# Define suits.
card = "23456789TJQKA"
suits = "SDHC"

# Define pile of cards set.
cards = set()

# Populate set with cards.
for c in card:
    for s in suits:
        cards.add(c+s)

def cards_parser(card_string):
    """ 
    Helper function to parse cards into values and suits.
    Parameters: card_string : str - String to be parsed.
    Returns : array, array - Two arrays containing card values and suits respectively.
    """
    cards_parsed = []
    suits_parsed = []
    for char in card_string:
        if char in card:
            cards_parsed.append(char)
        else:
            suits_parsed.append(char)
    if suits_parsed == []:
        suits_parsed = suits
    if cards_parsed == []:
        cards_parsed = card
    return cards_parsed, suits_parsed

# Remove any cards defined.
r, s = [int(i) for i in input().split()]
for i in range(r):
    removed = input()
    cards_to_remove, suits_to_remove = cards_parser(removed)

    for suit in suits_to_remove:
        for card_value in cards_to_remove:
            if card_value+suit in cards:
                cards.remove(card_value+suit)

# Find any cards sought after still in the deck.
cards_sought = set()
for i in range(s):
    sought = input()
    cards_to_find, suits_to_find = cards_parser(sought)

    for suit in suits_to_find:
        for card_value in cards_to_find:
            if card_value+suit in cards:
                cards_sought.add(card_value+suit)

# Print percentages of selecting one of the sought after cards.
print(f"{int(len(cards_sought)/len(cards) * 100)}%")
