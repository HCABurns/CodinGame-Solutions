# Get sequence.
sequence = list(input())

# Hashmap for storing weights, how many tags are opened and index.
chars = {}
opened = 0
idx = 0

# Count number of open, when closed add open to char hashmap, open - 1
while idx < len(sequence):
    # Get character.
    char = sequence[idx]

    # If not a closing tag, increment open.
    if char != "-":
        opened += 1
    # If closing tag, store weight.
    else:
        idx += 1
        char = sequence[idx]
        if char not in chars:
            chars[char] = 0
        chars[char] += 1 / opened
        opened -= 1
    idx += 1

# Print max weight of tag.
print(max(chars.items(), key = lambda x : x[1])[0])
