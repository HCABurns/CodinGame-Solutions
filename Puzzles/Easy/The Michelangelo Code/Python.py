# Get text, covert to lowercase and remove any non-alpha characters.
text = "".join([char.lower() for char in input() if char.isalpha()])

# Set array for max string and max word.
max_str = ["",""]

# Check text for given hidden words.
for _ in range(int(input())):
    word = input()

    # If current word length is less than max, continue as it can't be longer.
    if len(word) < len(max_str[0]):
        continue
    
    # Get possible starting positions.
    starts = [idx for idx,char in enumerate(text) if char == word[0]]
    
    # Check all starting positions for hidden word.
    for pos in starts:
        # Check evenly spaced positions for "word"
        for j in range(1,(len(text)-pos) // len(word)):
            txt = text[pos:pos+len(word)*j:j]
            # If found, add capitalization where required and set new max.
            if txt == word:
                txt = list(text[pos:pos+(len(word)-1)*j+1])
                for i in range(0,len(txt),j):
                    txt[i] = txt[i].upper()
                max_str = [word, "".join(txt)]

# Print max hidden code.
print(max_str[1])
