# Create hashmap of emojis and their associated value.
emoji_value = {}
for i in range(int(input())):
    value, emojis = input().split("=")
    cost = "".join([j for j in value if j.isnumeric()])
    for j in emojis.strip():
        emoji_value[ord(j)] = int(cost)

# Get all the emojis in the garden and store in hashmap.
garden_height = int(input())
emojis = {}
for _ in range(garden_height):
    for i in input():
        if ord(i) > 1000:
            if ord(i) not in emojis:
                emojis[ord(i)] = 0
            emojis[ord(i)] += 1

# Print the total worth of the garden.
total = sum([quantity * emoji_value.get(emoji,0) for emoji,quantity in emojis.items()])
print("$" + "{:,}".format(total))
