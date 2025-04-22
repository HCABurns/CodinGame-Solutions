# Get the sizes of the bookcase.
height = gets.to_i - 1
width = gets.to_i
number_of_shelves = gets.to_i

# Get the number of larger shelves.
no_of_bigger = height % number_of_shelves

# Find the height of a regular shelf.
size = (height - no_of_bigger) / number_of_shelves

# Print the top of the bookcase.
puts ("/"*(width/2) + "^"*(width%2) + "\\"*(width/2))

# Print the regular sized shelves.
(number_of_shelves - no_of_bigger).times do 
    ((size)-1).times do |i|    
        puts "|" + ' '*(width-2) + "|"
    end
    puts "|" + '_'*(width-2) + "|"
end

# Print the larger shelves.
(no_of_bigger).times do 
    ((size)).times do |i|    
        puts "|" + ' '*(width-2) + "|"
    end
    puts "|" + '_'*(width-2) + "|"
end
