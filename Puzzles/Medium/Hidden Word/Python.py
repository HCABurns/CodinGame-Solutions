# Get words to find and their sizes.
clues = []
sizes = []
n = int(input())
for i in range(n):
    clue = input()
    clues.append(clue)
    if len(clue) not in sizes:
        sizes.append(len(clue))

# Form grid and string representation of the grid.
grid = []
s = ""
h, w = [int(i) for i in input().split()]
for i in range(h):
    line = input()
    s+=line
    grid.append(list(line))

# Check each direction for each size of word. Perform once per character.
for i in range(len(s)):
    for size in sizes:
        # Convert position in string to grid.
        new_i = i//w
        new_j = i%w
        #Forwards and backwards
        if s[i:i+size] in clues or s[i:i+size][::-1] in clues:
            word = s[i:i+size]
            reversed_word = s[i:i+size][::-1]
            grid[new_i][i%w:i%w+size] = " "*len(word)
        
        #Up and Down
        if s[i:i+(w*size):w] in clues or s[i:i+(w*size):w][::-1] in clues:
            for char in s[i:i+(w*size):w]:
                grid[new_i%w][new_j] = " "
                new_i += 1
        
        #Diagonal Down
        if s[i:i+(w*size):w+1] in clues or s[i:i+(w*size):w+1][::-1] in clues:
            for char in s[i:i+(w*size):w+1]:
                grid[new_i%w][new_j%w] = " "
                new_i += 1
                new_j += 1
        
        #Diagonal Up
        if s[i:i+((w-1)*size):w-1] in clues or s[i:i+((w-1)*size):w-1][::-1] in clues:
            for char in s[i:i+((w-1)*size):w-1]:
                grid[new_i%w][new_j%w] = " "
                new_i += 1
                new_j -= 1

# Output a string of the letters unused.
print("".join([char for char in "".join(["".join(row) for row in grid]) if char != " "]))
