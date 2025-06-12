# Get name.
name = input()

# Get lists.
adjList = "Adaptable Adventurous Affectionate Courageous Creative Dependable Determined Diplomatic Giving Gregarious Hardworking Helpful Hilarious Honest Non-judgmental Observant Passionate Sensible Sensitive Sincere".split(" ")
goodList = "Love, Forgiveness, Friendship, Inspiration, Epic Transformations, Wins".split(", ")
badList = "Crime, Disappointment, Disasters, Illness, Injury, Investment Loss".split(", ")

# Arrays for storing indexes.
a = []
b = []
chars = []
valid = True

# Find the indexes of the unique chars.
cons = "bcdfghjklmnpqrstvwxz"
vowels = "aeiouy"
for char in name:
    if char.isalpha() and char not in chars:
        if char.lower() in vowels:
            b+=[vowels.index(char.lower())]
        else:
            chars += char.lower()
            chars += char.upper()
            a += [cons.index(char.lower())]
            
# Print the correct output.
if len(a) > 2 and len(b)>1:
    print(f"It's so nice to meet you, my dear {adjList[a[0]].lower()} {name}.")
    print(f"I sense you are both {adjList[a[1]].lower()} and {adjList[a[2]].lower()}.")
    print(f"May our future together have much more {goodList[b[0]].lower()} than {badList[b[1]].lower()}.")
else:
    print(f"Hello {name}.")
