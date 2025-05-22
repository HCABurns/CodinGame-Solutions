# Create array for storing invalid.
invalid = []
n = int(input())
for i in range(n):
    # Get the inputs.
    isbn = input()

    # Remove any invalid without needing to check values.
    if any(1 if not char.isnumeric() else 0 for char in isbn[:-1]) or len(isbn) not in [10, 13]:
        invalid += [isbn]
        continue
    
    # Determine if isbn is valid or not.
    value = 0
    if len(isbn) == 10:
        i = 10
        for char in isbn[:-1]:
            value += int(char) * i
            i-=1
        check = 11 - [(value % 11),11][value%11 == 0]
        if check == 10:
            check="X"
        if str(check) != isbn[-1]:
            invalid.append(isbn)
    
    else:
        for j, char in enumerate(isbn[:-1]):
            if j % 2 == 0:
                value += 1 * int(char)
            else:
                value += 3 * int(char)
        if str(isbn[-1]) != str(10- [(value % 10),10][value%10 == 0]):
            invalid.append(isbn)

# Print number of invalid isbns and then print the invalid isbns.
print(f"{len(invalid)} invalid:")
print("\n".join(invalid))
