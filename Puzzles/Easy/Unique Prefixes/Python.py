# Get words and create prefix hashmap.
prefixes = {}
words = []
n = int(input())
for i in range(n):
    word = input()
    words.append(word)
    for i in range(len(word)):
        if word[:i+1] not in prefixes:
            prefixes[word[:i+1]] = 0
        prefixes[word[:i+1]] += 1

# For each word find the largest unique prefix. If none found print first character.
for word in words:
    prefix = word[0]
    for i in range(len(word)-1,-1,-1):
        if prefixes[word[:i+1]] > 1:
            prefix = word[:i+2]
            break
    print(prefix)

