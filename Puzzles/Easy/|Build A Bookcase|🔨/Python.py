# Get the sizes of the bookcase.
height = int(input()) - 1
width = int(input())
number_of_shelves = int(input())

# Get the number of larger shelves.
no_of_bigger = height % number_of_shelves

# Find the height of a regular shelf.
size = (height - no_of_bigger) / number_of_shelves

# Print the top of the bookcase.
print("/"*(width//2) + "^"*(width%2) + "\\"*(width//2))

# Print the regular sized shelves.
for i in range(number_of_shelves - no_of_bigger):
    for j in range(int(size)-1):    
        print(f"|{' '*(width-2)}|")
    print(f"|{'_'*(width-2)}|")

# Print the larger shelves.
for i in range(no_of_bigger):
    for j in range(int(size)):    
        print(f"|{' '*(width-2)}|")
    print(f"|{'_'*(width-2)}|")
