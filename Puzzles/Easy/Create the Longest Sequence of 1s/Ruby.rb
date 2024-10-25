# Get input and split based on character 0.
b = gets.chomp.split("0")

# Define max size
max_size = 1

# Get addition of sizes of adjacent sets of 1s (Plus one for flip 0 bit)
(0..b.size-2).each{|i|
    size = b[i].length + b[i+1].length + 1
    max_size = [max_size , size].max
}

# Output the max size of consecutive 1s after flipping 0 bit.
puts max_size
