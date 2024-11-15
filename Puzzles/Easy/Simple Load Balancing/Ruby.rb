# Get inputs and store loads in array. (Sort loads for better efficiency)
gets
k = gets.to_i
servers = gets.split.map{|x| x.to_i}.to_a.sort

# Define required variables.
idx = 0
additional = 0
remainder = 0

# Continue until all same length or no more to add.
while k > 0 &&  idx < servers.size-1 do
    # Get difference and increment idx.
    diff = servers[idx+1] - servers[idx]
    idx += 1
    # If all minimums can be incremented to next unique minimum, do it.
    if k > idx * diff
        idx.times do |j|
            servers[j] += diff
            k -= diff
        end
    else
        # Add 1 to a item if remainder exists.
        additional = (k / idx).floor
        servers[0] += 1  if additional!=0 && k % additional > 0
            
        # Increment all 
        idx.times{|j| servers[j] += additional}
        k = 0
    end
end
  
# Add remainder to one item if needed.
additional =  (k / idx).floor
servers[-1] += 1  if (additional!=0) && (k % additional > 0)

# Output the minimum difference.
puts servers.max - servers.min + remainder
