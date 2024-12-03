# Get length and size of contents page.
lengthofline = gets.to_i
n = gets.to_i

# Array of current levels.
counts = [0]

n.times do
  # Get title, page number and indent amount.
  title, page = gets.chomp.split(" ")
  indent = title.count(">")

  # Increment counter for directory/subdirectory.
  if counts.size <= indent
    counts << 1
  else
    counts[indent] += 1
  end

  # Reset subdirectory counts.
  tmp = indent+1
  while tmp < counts.size do
    counts[tmp] = 0
    tmp += 1
  end

  # Print correct contents.
  puts ("    "*indent + "" + counts[indent].to_s + " "+ title[indent..]).ljust(lengthofline - page.size,".") + page
end
