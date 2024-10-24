# Declare required variables.
expression = gets.chomp
pairs = {")"=>"(","]"=>"[","}"=>"{"}
stack = []
valid = true

expression.each_char do |char| 
    # If char not a bracket -> ({[ then move on to next character
    if "(){}[]".include?(char) then
        # Check if char is a closing bracket or not.
        if pairs.keys.include?(char) then
            # If no character on stack or top of stack doesn't pair with char
            # set valid to false.
            if stack.size == 0 || pairs[char] != stack.pop then
                valid = false
            end  
        else
            # Append open bracket to the stack.
            stack << char
        end
    end
end

# Output true if valid otherwise false
if valid & stack.empty? then
    puts "true"
else
    puts "false"
end
