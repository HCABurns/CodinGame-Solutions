# Get inputs.
r = gets.to_i
v = gets.to_i

# Get all bank combinations and add r banks to available.
banks = []
available = []
v.times do
  c, n = gets.split.map { |x| x.to_i }
  combination = (10**n) * (5**(c-n))
  banks << combination
  if r > 0
    r-=1
    available << combination
  end
end

# Get total and set next bank id.
total = 0
next_bank_idx = available.size

# Continue until all combinations have been cracked.
while available != []
  # Remove bank with least number of combinations remaining. Keep track of number of banks to add.
  min_val = available.min
  total += min_val
  to_add = 0
  available.each.with_index{|val , i|
    to_add += 1 if val == min_val 
    available[i] -= min_val
  }
  
  # Remove banks that have been cracked, add robber to new bank.
  available = available.select{|x| x!=0}
  while to_add>0 && next_bank_idx<banks.size
    available << banks[next_bank_idx]
    next_bank_idx += 1
    to_add -= 1
  end
end
# Output total time to crack all the banks.
p total
