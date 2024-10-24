# Array for storing numbers.
s=[]

# For each numbers, add every substring starting from the first position to the array. 
gets.to_i.times{
    t=gets.chomp
    [*0..t.size].each{ |z| s << t[..z]}
}

# Print unique number of numbers in the array
p s.uniq.size
