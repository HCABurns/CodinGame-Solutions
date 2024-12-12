def is_prime(value):
    """
    Function for determining if a value is a prime or not.
    """
    i=2
    while i <= (value+1)//2:
        if value % i == 0:
            return  False
        i += 1
    return True

def derivative(value ,m , n):
    """
    Function used to find the derivative.
    """
    while is_prime(value) == False:
        while value % m != 0:
            m += 1
        n = value // m
        return n + m * derivative(n, 2, 4)
    return 1

# Print the derived number.
print(derivative(int(input()) , 2 , 0))
