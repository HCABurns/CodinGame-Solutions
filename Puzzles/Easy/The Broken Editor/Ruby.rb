# Get input string.
typed_keys = gets.chomp

# Create array 
arr = []

# Place charaters in the correct position, or remove charater if required..
i = 0
typed_keys.each_char do |char|
    if char == ">"
        i = [i+1, arr.size].min
    elsif char == "<"
        i = [i-1 , 0].max
    elsif char == "-"
        if i != 0
            i-=1
            arr.delete_at(i)
        end
    else
        arr.insert(i,char)
        i+=1
    end
end

# Output the new string.
puts arr.join("")
