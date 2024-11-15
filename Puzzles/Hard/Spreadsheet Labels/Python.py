def number_to_column(value):
    """
    Helper function to convert from decimal to spreadsheet column.

    Parameter:
    value : int - Value to be converted.

    Return: String - String of corresponding spreadsheet column.
    """
    # Ensure not 0 input.
    if value==0:print("A");quit()

    # Set output.
    column_name = ""

    # Continue until converted from base 10 to base len(c)
    while value > 0:
        value -= 1
        # Regular base conversion
        rem = value % 26
        column_name += chr(ord("A") + rem)
        value //= 26
    return column_name


def column_to_number(column):
    """
    Helper function to convert from spreadsheet column to decimal.

    Parameter:
    column : String - Column to be converted.

    Return: int - Int of corresponding spreadsheet column.
    """
    # Set total variable.
    total = 0
    # Convert from base 26 to decimal.
    for i,j in enumerate(column):
        total += (ord(j)-ord("A")+1) * (26 ** i)
    return total

# Define array to store conversions.
conversions = []
n = int(input())
for label in input().split():
    # Select correct function to swap column and decmial.
    conversion = None
    if label.isnumeric():
        conversion = number_to_column(int(label))[::-1]
    else:
        conversion = column_to_number(label[::-1])
    
    # Add to array
    conversions.append(conversion)

# Output the conversions.
print(*conversions)
