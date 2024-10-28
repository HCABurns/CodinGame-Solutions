# Form long string and grid.
s = ""
grid = []
n = int(input())
for i in range(n):
    grid.append([" "]*n)
    s+=input()

# Get clues and form set. Changed to upper for beter efficiency searching.
clues = set(i.upper() for i in input().split(" "))

# Get sizes of each word for searching.
sizes = []
for clue in clues:
    if len(clue) not in sizes:
        sizes.append(len(clue))

# Check each direction for each size of word. Perform once per character.
for i in range(len(s)):
    for size in sizes:
        # Convert position in string to grid
        new_i = i//n
        new_j = i%n
        #Forwards and backwards (Example of slightly better readability)
        if s[i:i+size] in clues or s[i:i+size][::-1] in clues:
            word = s[i:i+size]
            reversed_word = s[i:i+size][::-1]
            clues.remove(word if word in clues else reversed_word)
            grid[new_i][i%n:i%n+size] = word
        
        #Up and Down
        if s[i:i+(n*size):n] in clues or s[i:i+(n*size):n][::-1] in clues:
            clues.remove(s[i:i+(n*size):n] if s[i:i+(n*size):n] in clues else s[i:i+(n*size):n][::-1] )
            for char in s[i:i+(n*size):n]:
                grid[new_i%n][new_j] = char
                new_i += 1
        
        #Diagonal Down
        if s[i:i+(n*size):n+1] in clues or s[i:i+(n*size):n+1][::-1] in clues:
            clues.remove(s[i:i+(n*size):n+1] if s[i:i+(n*size):n+1] in clues else s[i:i+(n*size):n+1][::-1])
            for char in s[i:i+(n*size):n+1]:
                grid[new_i%n][new_j%n] = char
                new_i += 1
                new_j += 1
        
        #Diagonal Up
        if s[i:i+((n-1)*size):n-1] in clues or s[i:i+((n-1)*size):n-1][::-1] in clues:
            clues.remove(s[i:i+((n-1)*size):n-1] if s[i:i+((n-1)*size):n-1] in clues else s[i:i+((n-1)*size):n-1][::-1])
            for char in s[i:i+((n-1)*size):n-1]:
                grid[new_i%n][new_j%n] = char
                new_i += 1
                new_j -= 1

# Output the new grid, containing only words found.
print(*["".join(i) for i in grid],sep="\n")
