# Get inputs.
r_1 = gets.to_i
r_2 = gets.to_i

# Ensure r_1 is the smaller value.
r_1 , r_2 = [r_1,r_2].min , [r_1,r_2].max

# Continue until equal values.
while r_1 != r_2 do

    # Compute algorithm until r_1 is larger or equal to r_2.
    while r_1 < r_2 do
        r_1 += r_1.to_s.chars.map(&:to_i).sum
    end
    
    # If r_2 is smaller than r_1, compute the next value.
    r_2 += r_2.to_s.chars.map(&:to_i).sum if r_2 < r_1
end

# Output the meeting point.
puts r_1
