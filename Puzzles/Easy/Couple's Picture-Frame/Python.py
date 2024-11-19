import math
# Get names.
wife = input()
husband = input()

# Find smallest common multiple.
width = math.lcm(len(wife),len(husband))

# Create new strings.
wife = wife * (width//len(wife))
husband = husband * (width//len(husband))

# Output the picture frame.
print(wife)
for char1, char2 in zip(husband, wife):
    print(char1 + " "*(width-2) + char2)
print(husband)
