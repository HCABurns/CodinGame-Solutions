# Required variable. H[2]...H[-1] will also be used for an output.
encoded=["00","0"]
b=""

# Convert input to binary with exactly 7 characters (as required).
gets.chomp.chars.each do |c|
  b += "%07b" % c.ord
end
previous = nil
# Iterate over binary string and add correct value to array.
(0..b.size-1).each do |i|
  # If first value or current value is not equal to the previous (i.e previous was 1 and val is 0) add correct identifier.
  if i==0 || b[i] != previous
    previous = b[i]
    encoded << encoded[previous.to_i]
    encoded << ""
  end
  # Increment count by 1
  encoded[-1] += '0'
end

# Output the correct binary encoded message. 
puts encoded[2,encoded.size-2].join(" ")
