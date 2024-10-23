# Get size of inputs and store in a array.
arr = []
n = gets.to_i
n.times{arr << gets.to_i}

# Sort array
arr=arr.sort()

# Define difference variable
difference = 99999999;

# Check adjacent horses power and store minimum difference.
(n-1).times{|i|
  if arr[i+1] - arr[i] < difference
    difference = arr[i+1] - arr[i]
  end
}

# Output minimum distance
puts difference
