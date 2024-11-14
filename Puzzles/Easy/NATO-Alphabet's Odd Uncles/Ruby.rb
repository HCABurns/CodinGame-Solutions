# Get words to be changed.
a_word_spelled_out = gets.chomp.split

# Get alphabets.
year_1 = %w"Authority Bills Capture Destroy Englishmen Fractious Galloping High Invariably Juggling Knights Loose Managing Never Owners Play Queen Remarks Support The Unless Vindictive When Xpeditiously Your Zigzag"
year_2 = %w"Apples Butter Charlie Duff Edward Freddy George Harry Ink Johnnie King London Monkey Nuts Orange Pudding Queenie Robert Sugar Tommy Uncle Vinegar Willie Xerxes Yellow Zebra"
year_3 = %w"Amsterdam Baltimore Casablanca Denmark Edison Florida Gallipoli Havana Italia Jerusalem Kilogramme Liverpool Madagascar New-York Oslo Paris Quebec Roma Santiago Tripoli Uppsala Valencia Washington Xanthippe Yokohama Zurich"
year_4 = %w"Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-ray Yankee Zulu"
alphabets = [year_1, year_2, year_3, year_4]

# Create hashmap where each word links to the correct word in the next set.
hashmaps = []
(0..3).each do |i|
    hashmap = {}
    alphabets[i].zip(alphabets[(i+1)%4]).each{|word1 , word2| hashmap[word1] = word2}
    hashmaps << hashmap
end

# Get index of alphabet
idxs = []
hashmaps.each.with_index do |hashmap, i|
    a_word_spelled_out.each{|word| idxs.append(i) if hashmap.key?(word)}
end
idx = idxs.max_by{|x| idxs.count(x)}

# Shift words
out = []
a_word_spelled_out.each{|word|out << hashmaps[idx][word]}

# Output the shifted words.
puts out.join(" ")
