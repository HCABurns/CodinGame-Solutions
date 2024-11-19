import math

# Get starting number.
n = int(input())+1

# Two variables to store primes.
p1 = None
p2 = None

# Continue until two primes that has a difference of 2 have been found.
while not p2:
    # Find if n is a prime.
    is_prime = True
    for i in range(2,math.ceil(n**0.5)+1):
        if n%i == 0:
            is_prime = False
            break
    
    # If prime, increment by 2 othewise reset variables and increment by 1.
    if is_prime:
        if not p1:
            p1 = n
            n+=2
        else:
            p2 = n
    else:
        p1 = None
        p2 = None
        n+=1

# Output the two primes with a difference of 2.
print(p1, p2)
