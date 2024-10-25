# Get word and sentence (Conver to lower as case insensitive)
word = input().lower()
s = input().lower()

# Alter the sentence to remove punctuation and replace ! which spaces.
s = s.replace("!"," ")
s = s.replace("."," ")
s = s.replace(","," ")
s = s.replace(":"," ")
s = s.replace("?"," ")
tmp = []
for i in s.split(" "):
    if i != "":
        tmp.append(i)
s = tmp

def is_anagram(word1 , word2):
    """
    Helper function to determine is word1 is a anagram of word2. 
    Word can't be anagram if they're the same word.

    Parameters:
    word1 : string - Word to be checked for anagram.
    word2 : string - Word to be checked for anagram.

    Return : boolean - Boolean value: True if anagram otherwise False.
    """
    hashmap1 = {char:word1.count(char) for char in word1}
    hashmap2 = {char:word2.count(char) for char in word2}
    return hashmap1 == hashmap2 and word1 != word2

# Find the index of the key
word_idx = -1
i = 0
while i < len(s):
    if is_anagram(s[i], word):
        word_idx = i
        break
    i+=1

#Calcualte the required digits for code.
#(Possible to do position 0 and 2 while finding the key but put here for readability)
digits = [0,0,0,0]
digits[0] = i
digits[1] = len(s)-i-1
for word in s[:word_idx]:
    digits[2] += len(word)
for word in s[word_idx+1:]:
    digits[3] += len(word)

# Output the correct code. [Last digit of each value]
if word_idx==-1:
    print("IMPOSSIBLE")
else:
    print("{}.{}.{}.{}".format(*[i%10 for i in digits]))
