# Required impport
import math

# Get required inputs and store primes in array.
inputs = input().split()
n = int(inputs[0])
k = int(inputs[1]) 
out = {}
primes = [int(i) for i in input().split()]

# Add individual numbers count
out = 0
for p in primes:
    out+=n//p


def comb(arr , i):
    """
    Function for getting all possible subsets of an array.

    Parameters:
    arr - Possible combination array - to be added to.
    int i - Position index.

    Return: None
    """
    if i<len(primes):
        if arr != []:
            combs.append(arr+[primes[i]])
        comb(arr+[primes[i]] , i+1)
        comb(arr , i+1)

# Get all combinations and store in combs.
combs = []
comb([],i:=0)

# Remove variables that have clashes. (e.g. 3 and 5 will clash at 15, 30 etc.)
clashes = 0
for combination in combs:
    if len(combination)%2==0:
        clashes += n // math.prod(combination)
    else:
        clashes -= (n // math.prod(combination))

# Return count of natural numbers not greater than n and divisible at least by one of the primes.
print(out-clashes)
