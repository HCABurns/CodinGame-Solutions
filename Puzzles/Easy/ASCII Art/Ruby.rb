# Get length of input
l=gets.to_i
# Get height of input.
h = gets.to_i

# Get string to be converted and use uppercase only.
t=gets.chop.upcase

# Get each row and print each characters ascii art equivalent.
h.times{
  r = gets.chop
  puts t.chars.map{|c| r[((c.ord)<65?26:c.ord-65)*l,l] }.join
}
