# Get input and convert from single string to array of strings splitting on \n.
s = gets.chomp.split("\\n")

# Create hashmaps for storing indexes that have been added to and size of added.
#NOTE: Strings are mutable in Ruby so no need to convert to list.
hashmap = {}
sizes = {}

# Get number of changes to be made.
change_count = gets.to_i
change_count.times do
  # Get change and convert ints.
  line, idx, change = gets.chomp.split("|")
  line ,idx = line.to_i, idx.to_i
  
  # Get length of chars that have been added before idx on current line.
  to_change = 0
  if hashmap[line]
    hashmap[line].each.with_index{|val,i| to_change += sizes[line][i] if val < idx}
  end
  
  # Insert to correct location.
  s[line].insert(idx+to_change, change)

  # Create empty array if not in hashmap.
  hashmap[line]=[] if hashmap[line] == nil
  sizes[line]=[] if hashmap[line] == []

  # Add line and size to hashmaps.
  sizes[line] << change.size
  hashmap[line] << idx
end

# Output the new string with the inserts.
s.each{|str| puts *str.split("\\n")}
