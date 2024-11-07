# Form hashmap of characters and their positions.
chars = {}
rows = int(input())
for i in range(rows):
    chars.update({char: [i,j] for j,char in enumerate(input().split(" "))})

# Output the coordinates of the message as a single string.
for char in input():
    print(*chars[char],sep="",end="")
