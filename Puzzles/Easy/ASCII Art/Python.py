# Get height and width of the characters
width = int(input())
height = int(input())

# Get the text to be converted
text=input().upper()

# Get each row and print each characters ascii art with no newline until all characters have been printed
for _ in range(height):

    # Get ascii art row.
    row = input()
    for char in text:
        # Convert character to ordinal and minus value of "A".
        j=ord(char)-65

        #If J is less than 0 - It's a special character so convert to 26 (end of input)
        if j<0:
            j=26

        # Multiply by the width to get to the correct position
        j=j*width

        # Output correct character, no newline.
        print(end=row[j:j+width])
    
    # Print newline for the next row.
    print()
