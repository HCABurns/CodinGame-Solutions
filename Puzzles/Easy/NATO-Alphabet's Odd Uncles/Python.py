# Get words to be changed.
a_word_spelled_out = input().split(" ")

# Get alphabets.
year_1 = "Authority, Bills, Capture, Destroy, Englishmen, Fractious, Galloping, High, Invariably, Juggling, Knights, Loose, Managing, Never, Owners, Play, Queen, Remarks, Support, The, Unless, Vindictive, When, Xpeditiously, Your, Zigzag"
year_2 = "Apples, Butter, Charlie, Duff, Edward, Freddy, George, Harry, Ink, Johnnie, King, London, Monkey, Nuts, Orange, Pudding, Queenie, Robert, Sugar, Tommy, Uncle, Vinegar, Willie, Xerxes, Yellow, Zebra"
year_3 = "Amsterdam, Baltimore, Casablanca, Denmark, Edison, Florida, Gallipoli, Havana, Italia, Jerusalem, Kilogramme, Liverpool, Madagascar, New-York, Oslo, Paris, Quebec, Roma, Santiago, Tripoli, Uppsala, Valencia, Washington, Xanthippe, Yokohama, Zurich"
year_4 = "Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu"
alphabets = [year_1.split(", "),year_2.split(", "),year_3.split(", "),year_4.split(", ")]

# Create hashmap where each word links to the correct word in the next set.
hashmaps = []
for i in range(4):
    hashmap = {}
    for word1 , word2 in zip(alphabets[i],alphabets[(i+1)%4]):
        hashmap[word1] = word2
    hashmaps.append(hashmap)

# Get index of alphabet
idxs = []
for i,hashmap in enumerate(hashmaps):
    for word in a_word_spelled_out:
        if word in hashmap:
            idxs.append(i)
idx = max(idxs,key=idxs.count)

# Shift words
out = []
for word in a_word_spelled_out:
    out.append(hashmaps[idx][word])

# Output the shifted words.
print(" ".join(out))
