# Define variable of number of kisses and odds array.
total_kisses = 0
odds = []

# Populate odds array with odds of catching monkeypox of a girl.
h, w = [int(i) for i in input().split()]
for i in range(h):
    line = input()
    for j,char in enumerate(line):
        if char == "G":
            odds += [min(i,j)/(j**2 + i**2 + 1)]

# Sort based on probability of catching monekypox.
odds.sort()

# Find maximum number of girls that can be kissed with total chance of
# catching monkeypox is less than 40%.
for i in range(1,len(odds)):
    odds[i] = odds[i] + odds[i-1] - odds[i-1]*odds[i]
    if odds[i] < 0.4:
        total_kisses += 1

# Print number of people that can be kissed
print(total_kisses + 1 if odds[0] < 0.4 else 0)
