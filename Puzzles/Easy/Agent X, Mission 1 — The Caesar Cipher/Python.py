# Get the encrypted text and the known word in the text.
ciphertext = input()
word = input()

# Define the splitter characters. 
splitter = " .,;:?!"
# Function to determine if the word has been found.
def word_found(text, word, splitter):
    for i in range(len(text) - len(word) + 1):
        if text[i:i+len(word)] == word:
            before = (i == 0) or (text[i-1] in splitter)
            after = (i + len(word) == len(text)) or (text[i + len(word)] in splitter)
            if before and after:
                return True
    return False

# Perform a reverse ceaser cipher until the word with a separator is found.
key = 0
while key < 100:
    if word_found(ciphertext, word, splitter):
        break
    key += 1
    tmp = []
    for i in ciphertext:
        o = ord(i) - 1
        if o < 32:
            o = 126
        tmp.append(chr(o))
    ciphertext = "".join(tmp)

# Output the key value and the plaintext.
print(key)
print(ciphertext)
