# Convert input into integers.
a = gets.chomp.split.map{|i| i.to_i}
b = gets.chomp.split.map{|i| i.to_i}

# Set up total and two pointers.
i = 0
j = 0
total = 0

# Dot Product Loop.
while i<a.size && j<b.size{} do
    # Get value and amount of the next values.
    a_val = a[i+1]
    a_count = a[i]

    b_val = b[j+1]
    b_count = b[j]

    # Increment the total by the dot product of a and b.
    # Multiply the dot product by the minumum count of a and b.
    # E.g. a = [4, 4, 4] b = [5, 5, 5] A•B = 4*5+4*5+4*5 ≡ (4*5)*3
    min_count = [a_count,b_count].min
    total += (a_val * b_val) * min_count
    
    # Adjust counts.
    a[i] -= min_count 
    b[j] -= min_count 

    # Move onto next value pair if required.
    i+=2 if a[i] == 0
    j+=2 if b[j] == 0
end

# Output the total dot product.
puts total
