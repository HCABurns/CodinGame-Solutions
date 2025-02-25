# Read in size
h = gets.to_i

# Define charaters, array for storing rows and length of row.
chars = ".O"
rows = []
rows_length = -1

# Check all rows are the same length and store.
h.times do
  row = gets.chomp.split.map(&:to_i)
  sum = row.sum
  rows_length = sum if rows_length == -1 
  break if rows_length != sum
  rows << row
end

# If all rows have been read in, convert to text and print. Otherwise, print invalid.
if rows.size == h
  rows.each do |row|
    out = ""
    row.each.with_index do |size, i|
      out += chars[i%2]*size.to_i
    end
    puts out
  end
else
  puts "INVALID" 
end
