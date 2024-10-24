# Create set for storing numbers.
o=set()
size = int(input())

# For each numbers, add every substring starting from the first position to the set. 
for _ in range(size):
    number = input()
    for j in range(len(number)):
        o.add(number[0:j+1])

# Output the length of the set
print(len(o))
