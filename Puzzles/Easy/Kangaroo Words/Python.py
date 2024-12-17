# Array for storing words and their joey words.
kangaroo_and_joeys = []

n = int(input())
for _ in range(n):
    # Get words.
    lines = input().split(", ")

    # Find all joey words for each word.
    for word in lines:
        matches = []
        for joey in lines:
            if joey == word:continue

            # Check if joey is a joey for word.
            i = j = 0
            while i < len(word) and j < len(joey):
                while i != len(word) and word[i] != joey[j]:
                    i+=1
                j += 1
                i += 1
            if j == len(joey) and i != len(word)+1:
                matches.append(joey)

        # If word is a kangaroo word, add to the array.
        if matches != []:
            kangaroo_and_joeys.append((word, matches))

# Print the word and their joey words. If none then print NONE.
if len(kangaroo_and_joeys) == 0:
    print("NONE")
else:
    for word, joeys in sorted(kangaroo_and_joeys):
        print(f"{word}: {', '.join(joeys)}")
