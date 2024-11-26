# Required imports.
import random

# Define ranges for x, y, z.
MIN_X = -250
MIN_Y = -250
MIN_Z = -250
MAX_X = 500
MAX_Y = 500
MAX_Z = 500

def generate_random_input(num_islands):
    """
    Function to generate num_islands amount of random coordinates.

    Parameter:
    num_islands - int: Integer of number of coordinates to generate.

    Return: 2D Array - Array of Arrays of 3 float representing x, y, z coordinates.
    """
    islands = []
    for _ in range(num_islands):
        x = round(random.uniform(MIN_X, MAX_X), 2)
        y = round(random.uniform(MIN_Y, MAX_Y), 2)
        z = round(random.uniform(MIN_Z, MAX_Z), 2)
        islands.append((x, y, z))
    return islands

# Generate random coordinates.
inputs = []
inputs.append(generate_random_input(10))

# Output the random coordinates.
for coords in inputs:
    print(len(coords))
    for j , k , l in coords:
        print(j,k,l)
    print()
