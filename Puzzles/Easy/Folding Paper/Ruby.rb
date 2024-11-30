# Get inputs.
order = gets.chomp
side = gets.chomp

# Hashmaps for storing: current number of sheets visible, opposite direction and adjacent sides. 
sheets = {"L"=>1,"U"=>1,"R"=>1,"D"=>1}
opposite = {"L"=>"R","R"=>"L","U"=>"D","D"=>"U"}
adjacent = {"L"=>"DU","R"=>"DU","D"=>"RL","U"=>"RL"}

# Complete the folds.
order.each_char do |move|
    # Add current sheets to the opposite side.
    sheets[opposite[move]] += sheets[move]

    # Double the values on the adjacent sides.
    adjacent[move].each_char do |direction|
        sheets[direction] = sheets[direction] * 2
    end
    
    # Set current move to new value.
    sheets[move] = 1
end

# Output the number of sheets visible from given side.
puts sheets[side]
