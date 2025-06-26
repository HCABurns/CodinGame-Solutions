# Get target value.
n = gets.to_i

# Complete a BFS until target is found.
queue = [[1,1]]
seen = {}
while queue.size > 0 do 
    value, presses = queue.shift.map{|i| i.to_i}
    
    # Goal case.
    break if value == n

    # Prune useless branches.
    if (value > n+10 || value < 0)
        next
    end
    
    # Add to the queue.
    [value-1, value*2, value+1].each do |val|
        if !seen.include?(val)
            queue << [val,presses+1]
            seen[val] = true
        end
    end
end

# Print number of presses.
puts presses
