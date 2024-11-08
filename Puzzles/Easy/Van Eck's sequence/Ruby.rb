# Get inputs.
a1 = gets.to_i
n = gets.to_i

# Create hashmap for storing indexes.
hashmap = {}

# Complete sequence.
(0..n-2).each do |i|
    if !hashmap.key?(a1)
        hashmap[a1]=i
        a1=0
    else
        tmp = i - hashmap[a1]
        hashmap[a1] = i
        a1 = tmp
    end
end

# Output the correct result.
puts a1
