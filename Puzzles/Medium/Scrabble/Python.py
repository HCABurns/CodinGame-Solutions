#Hashmap of chars and points.
scores_hashmap = {}
chars = ["eaionrtlsu","dg","bcmp","fhvwy","k","qz"]
scores = [1,2,3,4,5,10]
for word,score in zip(chars,scores):
    for char in word:
        scores_hashmap[char] = score

# Get words and store in array.
n = int(input())
words = [input() for i in range(n)]

# Get available letters.
letters = input()

# Set required variables.
max_val = 0
max_word = ""

# Check if each word is valid and if so store points and string of the word with max points.
for word in words:
    if all(1 if char in letters and word.count(char) <= letters.count(char) else 0 for char in word):
        val = sum([scores_hashmap[char] for char in word])
        if val > max_val:
            max_word, max_val = word, val

# Output the word with the max score.
print(max_word)
