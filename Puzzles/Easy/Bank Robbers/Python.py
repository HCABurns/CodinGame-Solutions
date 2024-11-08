# Get inputs.
r = int(input())
v = int(input())

# Get all banks combinations and add r banks to available.
banks = []
available = []
for i in range(v):
    c, n = [int(j) for j in input().split()]
    combination = 10**n * 5**(c-n)
    banks.append(combination)
    if r:
        r-=1
        available.append(combination)

# Get total and set next bank id.
total = 0
next_bank_idx = len(available)

# Continue until all combinations have been cracked.
while available != []:
    # Remove bank with least number of combinations remaining. Keep track of number of banks to add.
    min_val = min(available)
    total += min_val
    to_add = 0
    for i,val in enumerate(available):
        if val == min_val:
            to_add += 1
        available[i] -= min_val    
    
    # Remove banks that have been cracked, add robber to new bank.
    available = list(filter(lambda x : x!=0,available))
    while to_add and next_bank_idx<len(banks):
        available.append(banks[next_bank_idx])
        next_bank_idx+=1
        to_add-=1

# Output total time to crack all the banks.
print(total)
