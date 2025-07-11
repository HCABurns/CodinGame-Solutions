# Get inputs.
word = input()
chars = input().split(" ")
output = ["_" if char.isalpha() else " " for char in word]

# Define the hangman boards.
hangman="""+--+   +--+   +--+   +--+   +--+   +--+   +--+ 
|      |  o   |  o   |  o   |  o   |  o   |  o 
|      |      |  |   | /|   | /|\\  | /|\\  | /|\\
|\\     |\\     |\\     |\\     |\\     |\\/    |\\/ \\""".split("\n")

# Complete all the guesses or end if the game is over.
hm = 0
i = 0
while i < len(chars) and hm < 7:
    if chars[i] not in word or chars[i] in output:
        hm+=1
    for idx,char in enumerate(word):
        if char == chars[i] or char.lower() in chars[i]:
            output[idx] = char
    i+=1

# Print the hangman board and the word with the guesses.
for row in hangman:
    print(row[(7*hm) : 7*hm+5].strip())
print(*output,sep="")
