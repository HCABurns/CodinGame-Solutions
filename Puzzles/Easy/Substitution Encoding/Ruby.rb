# Form hashmap of characters and their positions.
chars = {}
rows = gets.to_i
rows.times do |i|
  row = gets.chomp.split(" ").each.with_index{|char, j| chars[char] = [i,j]}
end

# Output the coordinates of the message as a single string.
puts gets.chomp.each_char.map{|char|chars[char]}.join
