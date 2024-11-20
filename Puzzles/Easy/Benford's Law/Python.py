# Set percentages.
percentages = {1: 30.1,
2: 17.6,
3: 12.5,
4: 9.7,
5: 7.9,
6: 6.7,
7: 5.8,
8: 5.1,
9: 4.6}

# Create empty count of 1..9
counts = {i:0 for i in range(1,10)}

# Get the first non-zero digit in the transaction.
n = int(input())
for i in range(n):
    transaction = input()
    for i in transaction:
        if i in "123456789":
            counts[int(i)] += 1
            break

# Compare with percentages and if difference of more than 10, set to 
fraudulent = False
for i in range(1,10):
    val = counts[i] / n / 0.01
    if percentages[i]<=val<=percentages[i]+10 or percentages[i]-10<=val<=percentages[i]+10:
        continue
    else:
        fraudulent = True
        break

# Output the "false" if not fraud and true if fraud.
if not fraudulent:
    print("false")
else:
    print("true")
