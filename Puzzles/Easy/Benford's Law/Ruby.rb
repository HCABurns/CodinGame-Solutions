# Set percentages.
percentages = {1=> 30.1,
2=> 17.6,
3=> 12.5,
4=> 9.7,
5=> 7.9,
6=> 6.7,
7=> 5.8,
8=> 5.1,
9=> 4.6}

# Create empty count of 1..9
counts = {}
(1..9).each{|i| counts[i] = 0}

# Get the first non-zero digit in the transaction.
n = gets.to_i
n.times do
  transaction = gets.chomp
  transaction.chars do |char|
    if "123456789".include?(char)
      counts[char.to_i] += 1
      break
    end
  end
end

# Compare with percentages and if difference of more than 10, set to 
fraudulent = false
(1..9).each do |i|
  val = counts[i] / n.to_f / 0.01
  if percentages[i]-10 > val || val > percentages[i]+10
    fraudulent = true
    break
  end
end

# Output the "false" if not fraud and true if fraud.
puts !fraudulent ? "false" : "true"
