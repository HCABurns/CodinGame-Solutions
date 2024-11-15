# Get size.
n = gets.to_i

# Print top half 
(1..n).each do |i|
    if i == 1
        puts "." + " "*(2*n-i-1) + "*"*(2*i-1)
    else
        puts " "*(2*n-i) + "*"*(2*i-1)
    end
end

# Print bottom half
(1..n).each do |i|
    left = " "*(n-i) + "*"*(2*i-1)
    right = "*"*(2*i-1)
    middle = " "*(2*(n-i)+1)
    puts left + middle + right
end
